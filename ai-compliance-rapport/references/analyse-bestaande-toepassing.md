# Analyse van een bestaande tool of pilot

Bij een toepassing die al bestaat, is wat de organisatie vertelt vaak niet hetzelfde als wat het systeem doet. Een melding "het is een AI" die in het plan staat maar niet in de app, persoonsgegevens die ongemerkt naar een leverancier gaan, een bewaartermijn die anders is ingesteld: dat soort afwijkingen vind je alleen door zelf te kijken. Wat je zelf hebt vastgesteld, is [Weten] met de bron erbij; wat alleen verteld is, blijft [Aannemen].

## Inhoud
1. Spelregels
2. Code en configuratie
3. Live tool of pilot
4. Leveranciersdocumenten
5. Pilotgegevens
6. Gekocht systeem zonder inzicht: vragenlijst leverancier
7. Verwerken in het rapport

## 1. Spelregels

- Kijk alleen in wat de gebruiker aanlevert of waar hij toegang toe geeft. Vraag niet om wachtwoorden of API-sleutels en open geen .env-bestanden met geheimen; noteer alleen dát er een sleutel voor een dienst is.
- Live testen alleen met toestemming van de gebruiker, en alleen met verzonnen testgegevens. Verstuur, bevestig of bestel niets in de tool zelf (geen formulieren, geen meldingen naar het team) tenzij de gebruiker dat expliciet vraagt.
- Citeer geen grote stukken code of documenten in het rapport; verwijs naar bestand en regel.
- Werk gericht: begin bij de plekken waar AI en persoonsgegevens samenkomen. Je hoeft niet de hele codebase te lezen.

## 2. Code en configuratie

Zoek gericht (bijv. met grep) en noteer per bevinding bestand:regel.

| Zoek naar | Waarom | Zoektermen (voorbeelden) |
|---|---|---|
| AI-leveranciers en modellen | Bepaalt de AI-onderdelen, rollen en leveranciers | `openai`, `anthropic`, `claude`, `gpt`, `gemini`, `mistral`, `elevenlabs`, `whisper`, `azure`, `bedrock`, `huggingface`, `model=`, `SpeechRecognition`, `speechSynthesis` |
| Systeeminstructies en kennisbank | Wat de AI wordt opgedragen; of hij zegt een AI te zijn; grenzen en escalatie | `system`, `prompt`, `instructions`, `kennisbank`, `knowledge` |
| Wat er naar het model gaat | Dataminimalisatie, persoonsgegevens, doorgifte | de functie die de API-aanroep opbouwt: welke velden (naam, e-mail, telefoon, vrije tekst, audio) |
| Tools en acties van de AI | Wat de AI zelf kan doen (mailen, wijzigen, boeken) en of een mens bevestigt | `tools`, `function`, `tool_use`, acties die mails of wijzigingen versturen |
| Melding aan gebruikers | Art. 50(1): staat er in de interface dat het een AI is? | welkomstteksten, UI-strings, eerste gesproken zin |
| Opslag en bewaartermijnen | AVG art. 5; wat er waar en hoe lang blijft | database-aanroepen, `TTL`, `expire`, `retention`, logbestanden, analytics |
| Hosting en regio | Doorgifte buiten de EER | configuratie (bijv. `vercel.json` regions, cloudregio's), leveranciers in de code |
| Accounts en afzenders | Rol en verwerkersovereenkomsten | omgevingsvariabelen en hun namen (zonder waarden), afzenderadressen, privé-accounts |
| Toegang en beveiliging | Misbruik, kosten, datalekken (AVG art. 32; bij hoog risico art. 15) | openbare endpoints zonder authenticatie of limiet; vertrouwt de server wat de browser stuurt (rol, context, "bevestigd")?; komt vrije invoer van gebruikers in de systeeminstructie terecht (prompt-injectie)?; geheimen of namen in publieke code |
| Eerlijk gedrag bij fouten | Misleiding van gebruikers, gemiste meldingen | zegt de interface "verzonden" of "doorgegeven" zonder te controleren of dat lukte?; wat doet een terugvalmodus? |
| Synthetische inhoud | Art. 50(2): markering | aanroepen voor spraak, beeld of tekstgeneratie; watermerk- of metadata-instellingen |

Vergelijk elke bevinding met wat de organisatie zegt of wat in de businesscase staat.

**Wees precies over gegevensstromen.** Volg een gegeven tot waar het werkelijk terechtkomt. Dat een veld naar de eigen server gaat, betekent niet dat het in de prompt voor het model of in de database belandt: kijk in de functie die de prompt of het record opbouwt. Schrijf "gaat naar de server, maar niet naar het model" als dat zo is. Een overdreven bevinding ondermijnt het vertrouwen in de rest van het rapport.

Grondige beveiligingstests horen in een aparte robuustheidstoets. Noem hier de bevindingen met juridische gevolgen (datalek, misleiding, misbruik) en verwijs voor de rest door.

## 3. Live tool of pilot

Alleen met toestemming en testgegevens. Loop na en maak screenshots of noteer letterlijk:
1. Eerste contact: ziet of hoort de gebruiker dat het een AI is, en wanneer?
2. Wordt duidelijk wat er wordt bewaard en waar je met vragen terechtkunt?
3. Is er altijd een route naar een mens? Hoe snel?
4. Twee of drie testvragen: een gewone vraag, een vraag waarop het antwoord niet in de kennis staat (verzint hij iets?), en een vraag met een gevoelig gegeven (wat doet hij ermee?).
5. Wat gebeurt er bij een fout, storing of geen netwerk?

## 4. Leveranciersdocumenten

Lees (of vraag om): verwerkersovereenkomst, lijst van subverwerkers, datalocatie en doorgiftemechanisme, bewaartermijnen, of klantdata wordt gebruikt voor training, beveiligingscertificeringen, en bij hoog-risico-AI de gebruiksinstructies (art. 13), CE-markering, EU-conformiteitsverklaring en registratie. Noteer wat ontbreekt als open punt.

## 5. Pilotgegevens

Als er gebruiksgegevens of logs zijn (zonder namen): hoe vaak wordt het gebruikt, welke soorten vragen, hoeveel fouten of escalaties, reactietijden van mensen. Toets daarmee de aannames uit de businesscase. Neem geen persoonsgegevens over in het rapport.

## 6. Gekocht systeem zonder inzicht: vragenlijst leverancier

Kan de organisatie niet in het systeem kijken, zet dan deze vragen als bijlage (praktisch handvat) en de antwoorden als open punten:
1. Welke AI-modellen gebruikt het systeem, van wie, en waar draaien ze?
2. Welke gegevens van ons gaan naar welke (sub)verwerkers, en in welke landen?
3. Wordt onze data gebruikt om modellen te trainen, ook voor andere klanten?
4. Welke bewaartermijnen gelden, en hoe verwijderen we data?
5. Wat is uw rol onder de AI-verordening, en welke risicoklasse kent u het systeem toe? Waarop gebaseerd?
6. Bij hoog risico: gebruiksinstructies, CE-markering, conformiteitsverklaring, registratie, logging?
7. Hoe is nauwkeurigheid en bias getest, op welke groepen, en mogen wij de resultaten zien?
8. Leidt het systeem emoties, kenmerken of gedrag van personen af? Zo ja, waaruit?
9. Hoe meldt u wezenlijke wijzigingen en incidenten?
10. Welke markering past u toe op gegenereerde inhoud (art. 50(2))?

## 7. Verwerken in het rapport

- Voeg in hoofdstuk 2.2 een tabel **"Zo bedoeld, zo werkt het"** toe: kenmerk | volgens de organisatie of businesscase | vastgesteld in code, tool of documenten (met bron) | gevolg.
- Afwijkingen met juridische gevolgen gaan naar de maatregelen (2.5) of de open punten (2.6).
- Vermeld in de samenvatting dat de toets is gebaseerd op eigen analyse van [code / live tool / documenten] per [datum], en wat niet is bekeken.
