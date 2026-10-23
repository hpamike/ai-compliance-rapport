# Overige wetgeving naast de AI-verordening

De AI-verordening staat nooit alleen. Toets per toepassing welke van onderstaande kaders waarschijnlijk relevant zijn en noem ze in het rapport onder "Toepasselijke vereisten". Geef bij twijfel aan wie het moet valideren (Legal, FG/DPO, Compliance, Inkoop, HR, ondernemingsraad). Markeer Nederlandse regels als Nederlands; werkt de organisatie in een ander land, noem dan het equivalent als je het kent, of zet het als open punt.

## Inhoud
1. AVG (privacy)
2. Arbeidsrecht en medezeggenschap
3. Consumentenrecht en marketing
4. Intellectueel eigendom en vertrouwelijkheid
5. Aansprakelijkheid
6. Cyberbeveiliging en weerbaarheid
7. Sectorregels
8. Overheid

## 1. AVG (Verordening (EU) 2016/679)

Bijna elke AI-toepassing verwerkt persoonsgegevens: namen, vragen, spraak, cv's, klantgesprekken. Toets:
- **Rollen:** wie is verwerkingsverantwoordelijke, wie verwerker (leveranciers zoals model-, hosting- en spraakaanbieders)? Verwerkersovereenkomst per verwerker (art. 28). Controleer dat de contracten op naam van de juiste rechtspersoon staan.
- **Grondslag (art. 6):** meestal gerechtvaardigd belang of overeenkomst; bij medewerkers is toestemming zelden vrij gegeven.
- **Bijzondere persoonsgegevens (art. 9):** gezondheid, biometrie voor identificatie, religie, etniciteit enz. Verbod tenzij een uitzondering geldt. Stem- of gezichtsherkenning om iemand te identificeren valt hieronder.
- **Nationale aanvullingen (NL, UAVG):** het BSN mag alleen worden gebruikt waar een wet dat voorschrijft (art. 46 UAVG), dus niet in een AI-tool invoeren; art. 40 UAVG biedt een beperkte uitzondering op het verbod van geautomatiseerde besluitvorming, maar niet voor besluiten die iemand aanmerkelijk treffen zonder passende waarborgen.
- **Geautomatiseerde besluitvorming (art. 22):** besluiten die uitsluitend geautomatiseerd zijn en iemand aanmerkelijk treffen, zijn in beginsel verboden; anders recht op menselijke tussenkomst en uitleg. Volgens het Hof van Justitie kan al een score een "besluit" zijn als een ander er doorslaggevend op leunt (SCHUFA, C-634/21), en betrokkenen hebben recht op een begrijpelijke uitleg van de logica (Dun & Bradstreet Austria, C-203/22). Een mens die alleen op "akkoord" klikt, telt niet als menselijke tussenkomst. Zie ook de EDPB-richtsnoeren over geautomatiseerde besluitvorming en profilering (WP251).
- **Transparantie (art. 12–14):** privacyverklaring bijwerken: dat AI wordt gebruikt, welke gegevens, welke leveranciers, bewaartermijnen.
- **Dataminimalisatie en bewaartermijnen (art. 5):** stuur niet meer naar het model dan nodig (bijv. rol in plaats van naam), bewaar logs en transcripten kort.
- **DPIA (art. 35):** verplicht bij waarschijnlijk hoog risico, o.a. bij systematische monitoring, grootschalige bijzondere gegevens, profilering met aanzienlijke gevolgen, of nieuwe technologie in combinatie met andere criteria. Bij hoog-risico-AI vrijwel altijd. Gebruik de informatie van de aanbieder (art. 13 AI-verordening).
- **Doorgifte buiten de EER (hoofdstuk V):** veel modelleveranciers verwerken (ook) in de VS. Check adequaatheidsbesluit (EU-US Data Privacy Framework-certificering), standaardcontractbepalingen, regio- en bewaaropties (bijv. geen training op klantdata, korte retentie).
- **Rechten van betrokkenen:** inzage, correctie, verwijdering. Zorg dat er een contactpunt is.
- **Omnibus:** de Digital Omnibus geeft een grondslag om bijzondere gegevens te verwerken voor het opsporen en corrigeren van bias, onder strikte voorwaarden; het schept geen plicht.

## 2. Arbeidsrecht en medezeggenschap

- **Ondernemingsraad (NL):** instemmingsrecht bij een personeelsvolgsysteem (art. 27 lid 1 sub l WOR), bij regelingen over verwerking van personeelsgegevens (sub k) en bij een beloningssysteem (sub c, bijv. als een AI-score meetelt voor bonussen). AI die prestaties, gedrag of aanwezigheid van medewerkers kan volgen, valt hier al snel onder, ook als dat niet het hoofddoel is. Een OR is verplicht vanaf 50 medewerkers; daaronder kan er een personeelsvertegenwoordiging zijn.
- **Arbeidsomstandigheden (NL: Arbowet):** AI die tempo, stress of gedrag meet of stuurt, raakt psychosociale arbeidsbelasting; neem het mee in de risico-inventarisatie (RI&E).
- **Informeren van werknemers:** verplicht vóór inzet van hoog-risico-AI op de werkplek (art. 26(7) AI-verordening).
- **Gelijke behandeling:** AI in werving, beoordeling of beloning mag niet discrimineren (NL: Algemene wet gelijke behandeling, Wet gelijke behandeling op grond van leeftijd bij de arbeid, en EU-richtlijnen). Toets op bias. Een model dat leert van eerdere aannamebeslissingen neemt de vooroordelen daarin over.
- **Werving en selectie (NL):** de NVP Sollicitatiecode is de gangbare norm (o.a. uitleg aan kandidaten over gebruikte methoden). Intermediairs en uitzendbureaus mogen geen discriminerende verzoeken van opdrachtgevers uitvoeren (Waadi).
- **Platformwerk:** de EU-richtlijn platformwerk (2024/2831) stelt eisen aan algoritmisch management; omzetting uiterlijk december 2026.

## 3. Consumentenrecht en marketing

- **Oneerlijke handelspraktijken (Richtlijn 2005/29, NL: Boek 6 BW afd. 3A):** AI die verkoop stuurt (upsell, dynamische prijzen, persuasive design) mag niet misleiden of agressief zijn. Let op druk bij kwetsbare klanten en dark patterns.
- **Consumentenbescherming bij chatbots:** informatie moet juist zijn; een fout antwoord over prijs of voorwaarden kan de organisatie binden.
- **Digital Services Act:** relevant voor online platforms (aanbevelingssystemen, transparantie, geen dark patterns).
- **Toegankelijkheid (European Accessibility Act, sinds juni 2025):** digitale diensten voor consumenten moeten toegankelijk zijn, ook AI-interfaces.

## 4. Intellectueel eigendom en vertrouwelijkheid

- **Auteursrecht op input en output:** mag de organisatie de data gebruiken die zij in het model stopt? Wie is eigenaar van de output (AI-output is vaak niet auteursrechtelijk beschermd)? Check de voorwaarden van de leverancier.
- **Bedrijfsgeheimen en geheimhouding:** stuur geen vertrouwelijke klant- of bedrijfsinformatie naar diensten zonder passende contractuele afspraken (geen training op data, retentie).
- **Beroepsgeheim en beroepsregels:** accountants (VGBA), advocaten (Advocatenwet, gedragsregels), notarissen, artsen en andere beroepen met een geheimhoudingsplicht mogen cliëntgegevens alleen in een AI-dienst stoppen als de vertrouwelijkheid contractueel en technisch is geborgd. Gegevens uit een Wwft-onderzoek hebben een eigen geheimhoudingsplicht. Check ook de beroepsaansprakelijkheidsverzekering.
- **Merk en naam:** een AI-assistent met een eigen naam of stem: geen imitatie van bestaande personen (ook art. 50(4) en portretrecht).

## 5. Aansprakelijkheid

- **Productaansprakelijkheid:** de herziene richtlijn (2024/2853) behandelt software, waaronder AI, als product; omzetting uiterlijk 9 december 2026. Gebrekkige AI kan tot risicoaansprakelijkheid leiden.
- **Contractuele aansprakelijkheid:** leg in contracten met leveranciers en klanten vast wie verantwoordelijk is voor fouten, uitval en updates.
- **Onrechtmatige daad:** foute adviezen van een AI-assistent kunnen de organisatie aansprakelijk maken.

## 6. Cyberbeveiliging en weerbaarheid

- **NIS2 (NL: Cyberbeveiligingswet):** voor essentiële en belangrijke entiteiten; zorgplicht en meldplicht, ook voor AI-leveranciers in de keten.
- **Cyber Resilience Act:** voor producten met digitale elementen; meldplichten vanaf september 2026, volledige eisen vanaf december 2027.
- **DORA:** voor de financiële sector, inclusief ICT-derdepartijrisico van AI-leveranciers.
- Robuustheid wordt doorgaans apart beoordeeld (bijvoorbeeld met het NIST CSF 2.0); noem hier alleen de juridische kaders en verwijs door.

## 7. Sectorregels (voorbeelden)

- Zorg: MDR/IVDR (medische hulpmiddelen), WGBO, Wet kwaliteit, klachten en geschillen zorg.
- Financieel: kredietwaardigheid (CRD, Consumentenkredietrichtlijn), verzekeringen, Wft-zorgplicht, toezicht AFM en DNB.
- Onderwijs: toetsing en beoordeling, gelijke kansen.
- Werving en selectie: zie arbeidsrecht.
- Mobiliteit, energie, kritieke infrastructuur: productveiligheid en sectortoezicht.

## 8. Overheid

- Algemene wet bestuursrecht: motiveringsbeginsel, zorgvuldigheid, uitleg van besluiten.
- Algoritmeregister (NL): publicatie van impactvolle algoritmes wordt verwacht.
- Grondrechteneffectbeoordeling (FRIA, art. 27) bij hoog-risico-AI; in NL vaak met het IAMA-instrument.
