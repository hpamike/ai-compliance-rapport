# Beslisbomen en verplichtingen

De vaste route: **inventaris → rol → risico → verplichtingen → maatregelen → bewijs**. Doorloop de stappen in deze volgorde; elke stap gebruikt de uitkomst van de vorige. Achtergrond per begrip staat in ai-act-kern.md.

## Inhoud
1. Stap A: inventaris per onderdeel
2. Stap B: rol(len) bepalen
3. Stap C: risico classificeren (Q1–Q6)
4. Stap D: verplichtingen per rol × risico
5. Stap E: van verplichting naar maatregel en bewijs

## 1. Stap A: inventaris per onderdeel

Maak een tabel met per onderdeel: naam en leverancier | AI-systeem / Geen AI-systeem / Onzeker | onderbouwing aan de hand van art. 3(1) ("leidt het af?") | welke informatie is gebruikt en welke ontbreekt.

Tips:
- Splits de oplossing op: model(len), spraak, beeld, aanbevelingen, scoring, maar ook de gewone onderdelen (database, mail, koppelingen). Gewone onderdelen horen wel binnen de systeemgrens.
- Vergeet AI in gekochte pakketten niet (CRM, HR-software, mail, kantoorsoftware), en AI-tools die medewerkers zelf gebruiken.
- Geplande uitbreidingen apart opnemen als "Onzeker" met de informatie die nodig is om ze te beoordelen.

## 2. Stap B: rol(len) bepalen

Stel per AI-systeem deze vragen in volgorde. Elk "ja" voegt een rol toe; meerdere rollen kunnen tegelijk gelden.

1. Brengt de organisatie een AI-systeem onder eigen naam of merk in de handel, of stelt zij het (ook voor eigen gebruik) in gebruik? → **Aanbieder**
2. Gebruikt de organisatie een AI-systeem onder eigen verantwoordelijkheid? → **Gebruiksverantwoordelijke**
3. Is de organisatie in de EU gevestigd en brengt zij een systeem van een aanbieder buiten de EU op de EU-markt? → **Importeur**
4. Maakt de organisatie een AI-systeem van een ander beschikbaar zonder de functie te wijzigen? → **Distributeur**
5. Brengt de organisatie een product met AI (bijlage I) onder eigen naam op de markt? → **Productfabrikant**
6. Is de organisatie aangewezen door een aanbieder buiten de EU om diens EU-plichten te vervullen? → **Gemachtigde**

Leg per rol vast: welk systeem, welke activiteit de rol bepaalt, en waar onzekerheid zit. Typische onzekerheden: contracten op naam van een persoon of andere entiteit; wie de inzet van een functie aanzet (de organisatie of de eindgebruiker op eigen toestel); plannen om het systeem aan derden aan te bieden (dan wordt "in gebruik stellen" ook "in de handel brengen").

Breng ook de keten in kaart: wie levert (aanbieder/leverancier), wie zet in (gebruiksverantwoordelijke), wie gebruikt de output, wie ondervindt de gevolgen.

## 3. Stap C: risico classificeren (Q1–Q6)

Beantwoord in deze volgorde. "Geen" bij een vraag betekent alleen dat die categorie niet van toepassing is, niet dat de beoordeling klaar is.

- **Q1 Verboden praktijk (art. 5)?** Loop (a) t/m (h) en de nieuwe verboden langs. Ja → STOP: herontwerp of juridisch advies; geen beheersmaatregelen als oplossing. Onzeker → vastleggen en juridisch laten toetsen vóór je verdergaat.
- **Q2 Bijlage I-product?** Ja → productwetgeving noemen en art. 6(1) toetsen (veiligheidscomponent, conformiteitsbeoordeling door derden).
- **Q3 Bijlage III-gebied?** Ja → exacte punt noemen en art. 6(3) toetsen (uitzondering, maar nooit bij profilering).
- **Q4 Profilering?** Leidt het systeem kenmerken, gedrag, voorkeuren of risico's van personen af? Ja → meewegen bij art. 6(3) en de AVG (art. 22).
- **Q5 Transparantie (art. 50)?** Communiceert het met mensen, maakt het synthetische inhoud, doet het emotieherkenning of biometrische categorisering, of publiceert het deepfakes of AI-tekst over zaken van algemeen belang? Ja → welk lid en wie is plichtig (aanbieder of gebruiksverantwoordelijke).
- **Q6 Rolwisseling (art. 25)?** Alleen bij hoog risico en als de organisatie nog geen aanbieder is: eigen naam erop, wezenlijke wijziging, of doelwijziging naar hoog risico? Ja → ook aanbiedersplichten.

**Eindclassificatie:** verboden / hoog risico / transparantie (art. 50) / minimaal risico / nader onderzoek nodig. Combinaties zijn mogelijk (hoog risico én art. 50). Vermeld de deadline die erbij hoort (zie tijdlijn).

## 4. Stap D: verplichtingen per rol × risico

| Rol | Hoog risico | Transparantie (art. 50) | Altijd |
|---|---|---|---|
| Aanbieder | Art. 9–15 (risicobeheer, data, documentatie, logging, instructies, menselijk toezicht, nauwkeurigheid en cyberveiligheid), 16 (o.a. identificatie, toegankelijkheid), 17 (kwaliteitsbeheer), 18–20 (documentatie bewaren, logs, corrigerende maatregelen), 43 (conformiteitsbeoordeling), 47 (EU-verklaring), 48 (CE), 49 (registratie), 72–73 (monitoring na het in de handel brengen, melden van ernstige incidenten) | 50(1) melden dat het een AI is; 50(2) synthetische inhoud machineleesbaar markeren | Art. 4 AI-geletterdheid |
| Gebruiksverantwoordelijke | Art. 26 (gebruik volgens instructies, menselijk toezicht, inputdata, monitoring en melden, logs ≥ 6 maanden, werknemers informeren, betrokkenen informeren, samenwerken met toezicht); art. 27 FRIA (overheid en bepaalde private partijen); art. 86 recht op uitleg; DPIA-afstemming | 50(3) informeren bij emotieherkenning of biometrische categorisering; 50(4) deepfakes en publieke AI-tekst kenbaar maken | Art. 4 AI-geletterdheid |
| Importeur | Art. 23 (conformiteit, documentatie en CE controleren, niet op de markt bij twijfel, eigen identificatie, 10 jaar bewaren, samenwerken) | Geen specifieke plichten | — |
| Distributeur | Art. 24 (CE, verklaring en instructies controleren, niet leveren bij twijfel, melden, corrigerende maatregelen, samenwerken) | Geen specifieke plichten | — |
| Gemachtigde | Art. 22 (mandaat, documentatie controleren en bewaren, contactpunt voor toezicht) | Geen specifieke plichten | — |
| Productfabrikant | Productwetgeving uit bijlage I; als het AI-systeem onder eigen naam meekomt, aanbiedersplichten | Algemene productveiligheid | — |

Combineer bij meerdere rollen de plichten zonder dubbelingen. Bij minimaal risico blijven art. 4 en de overige wetgeving (overige-wetgeving.md) gelden.

## 5. Stap E: van verplichting naar maatregel en bewijs

Schrijf per verplichting:
1. de verplichting en het artikel;
2. een concrete, toetsbare maatregel (wat wordt er gedaan, gebouwd of afgesproken);
3. de eigenaar (persoon of rol);
4. het bewijs dat een auditor kan controleren: een document, logbestand, testverslag, screenshot, contract, presentielijst of besluit. Nooit "compliant" als bewijs;
5. de status en de deadline.

Voorbeelden van goede regels:

| Verplichting | Maatregel | Eigenaar | Bewijs |
|---|---|---|---|
| 50(1) AI-melding | Zin in welkomsttekst en eerste gesproken zin: "Ik ben X, een AI-assistent"; releasechecklist controleert dit | Producteigenaar | Screenshot, versie in versiebeheer, ingevulde checklist |
| 26 menselijk toezicht (hoog risico) | Twee bevoegde beoordelaars, getraind; procedure voor overrulen en stoppen | Teamleider HR | Ondertekende procedure, presentielijst, steekproef uit override-log |
| 4 AI-geletterdheid | Instructie per rol (zie ethiek-en-toezicht.md) | AI-eigenaar | Handleiding, presentielijst, datum evaluatie |
| AVG art. 28 | Verwerkersovereenkomst met elke leverancier die persoonsgegevens verwerkt | Privacy officer / FG | Getekende overeenkomsten |

Sluit af met een **volledigheidscontrole**: heeft elke verplichting een maatregel, een eigenaar en herkenbaar bewijs? Bewijs dat nog gemaakt moet worden, is een open actie, niet "klaar".

**AI-register:** neem per AI-systeem op: naam en doel, eigenaar, leverancier(s), rol(len), classificatie met datum, verplichtingen met status, waar het bewijs staat, datum van de volgende herbeoordeling. Herbeoordeel bij elke wezenlijke wijziging of uitbreiding.
