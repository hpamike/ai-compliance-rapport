# AI-verordening: kern voor de screening

Stand van de wet: verwerkt t/m Verordening (EU) 2026/1744 (Digital Omnibus on AI), in werking sinds 27 juli 2026. De wet en de uitleg ervan bewegen nog. Controleer bij elk rapport met een zoekopdracht of er sindsdien iets is veranderd (nieuwe richtsnoeren van de Commissie, uitstel, geharmoniseerde normen) en zet de datum van die check in het rapport.

Basistekst: Verordening (EU) 2024/1689 (AI-verordening, "AI Act"). Gebruik altijd de artikelnummering van de definitieve tekst. Lesmateriaal en oudere bronnen gebruiken soms conceptnummers: art. 29 (oud) = art. 26 (plichten gebruiksverantwoordelijke), art. 52 (oud) = art. 50 (transparantie).

## Inhoud
1. Is het een AI-systeem? (art. 3(1))
2. Buiten de reikwijdte (art. 2)
3. Rollen in de keten (art. 3, art. 25)
4. Risicoklassen
5. Verboden praktijken (art. 5)
6. Hoog risico (art. 6, bijlage I en III)
7. Transparantie (art. 50)
8. AI-geletterdheid (art. 4)
9. AI-modellen voor algemene doeleinden (GPAI)
10. Tijdlijn
11. Handhaving en boetes

## 1. Is het een AI-systeem? (art. 3(1))

Een AI-systeem is een machinegebaseerd systeem dat met een zekere mate van autonomie werkt, zich na ingebruikname kan aanpassen, en uit de input die het ontvangt *afleidt* hoe het output genereert (voorspellingen, inhoud, aanbevelingen of beslissingen) die fysieke of virtuele omgevingen kan beïnvloeden.

Het beslissende element is **afleiden**. De richtsnoeren van de Commissie over de definitie (februari 2025) sluiten systemen uit die alleen:
- regels volgen die volledig door mensen zijn vastgelegd (als-dan-logica, vaste drempels, regex, formules);
- eenvoudige gegevensverwerking doen (sorteren, filteren, tellen, opzoeken);
- klassieke heuristiek of wiskundige optimalisatie gebruiken zonder te leren;
- een eenvoudige voorspelling geven op basis van één statistische regel (bijvoorbeeld een gemiddelde).

Taalmodellen, spraakherkenning, spraaksynthese, beeldherkenning, aanbevelingssystemen en scoringsmodellen die op data getraind zijn, zijn vrijwel altijd AI-systemen.

**Werk per onderdeel, niet per oplossing.** Een toepassing bestaat meestal uit AI-onderdelen (bijv. een taalmodel, een spraakmodel) en gewone onderdelen (database, mail, dashboard). Benoem ze apart. Leg vervolgens de systeemgrens vast: welke onderdelen vormen samen één AI-systeem?

**Onzeker** is een volwaardig antwoord. Noteer dan welke informatie het beslist: "Is de drempel door een mens gekozen of geleerd uit data?", "Zit er een getraind model in het pakket van de leverancier?".

## 2. Buiten de reikwijdte (art. 2)

Onder meer: uitsluitend militaire en defensiedoeleinden; wetenschappelijk onderzoek en ontwikkeling vóór het in de handel brengen; puur persoonlijk, niet-professioneel gebruik door natuurlijke personen; AI-systemen onder vrije en open-sourcelicenties zolang ze niet verboden, hoog risico of art. 50-plichtig zijn. Toets dit kort en ga anders door.

## 3. Rollen in de keten (art. 3, art. 25)

Je rol volgt uit wat je **doet**, niet uit wat je kiest of in een contract zet. Eén organisatie kan meerdere rollen tegelijk hebben.

| Rol | Wanneer | Kernvraag |
|---|---|---|
| Aanbieder (provider), art. 3(3) | Ontwikkelt een AI-systeem (of laat het ontwikkelen) en brengt het onder eigen naam of merk in de handel of stelt het in gebruik. Ook bij uitsluitend eigen gebruik. | Bouwt of laat de organisatie het bouwen, en staat haar naam erop? |
| Gebruiksverantwoordelijke (deployer), art. 3(4) | Gebruikt een AI-systeem onder eigen verantwoordelijkheid, behalve puur persoonlijk gebruik. | Zet de organisatie het in haar eigen processen in? |
| Importeur, art. 3(6) | In de EU gevestigd en brengt een AI-systeem van een aanbieder buiten de EU onder diens naam op de EU-markt. | Verkoopt de organisatie een buitenlands systeem door onder de naam van de maker? |
| Distributeur, art. 3(7) | Maakt een AI-systeem beschikbaar in de keten zonder de eigenschappen te wijzigen (geen aanbieder of importeur). | Levert de organisatie het systeem van een ander door? |
| Productfabrikant | Brengt een product (bijlage I) met AI onder eigen naam op de markt. | Zit de AI in een gereguleerd product van de organisatie? |
| Gemachtigde, art. 3(5) | Schriftelijk aangewezen door een aanbieder buiten de EU. | Is de organisatie daartoe aangesteld? |

**Rolwisseling (art. 25):** een gebruiksverantwoordelijke, distributeur of importeur wordt aanbieder van een hoog-risicosysteem als hij (a) er zijn naam of merk op zet, (b) het wezenlijk wijzigt, of (c) het beoogde doel zo wijzigt dat het hoog risico wordt.

**Let op bij API-gebruik van een taalmodel:** de leverancier (bijv. OpenAI, Anthropic, Google, Mistral) is aanbieder van een *model voor algemene doeleinden*. Wie daarmee een eigen toepassing bouwt en onder eigen naam inzet, is aanbieder van dat *AI-systeem* en vaak ook gebruiksverantwoordelijke.

**Let op bij accounts en contracten:** check op wiens naam de contracten met leveranciers staan. Staan die privé op een medewerker of bij een andere entiteit, dan zijn rol, aansprakelijkheid en verwerkersovereenkomsten (AVG) niet sluitend.

## 4. Risicoklassen

1. **Onaanvaardbaar risico:** verboden (art. 5).
2. **Hoog risico:** zware eisen (art. 6 e.v.).
3. **Transparantierisico** ("beperkt risico"): informatieplichten (art. 50).
4. **Minimaal risico:** geen specifieke plichten uit de AI-verordening; wel art. 4 en andere wetgeving.

Labels sluiten elkaar niet uit: een hoog-risicosysteem kan ook onder art. 50 vallen.

## 5. Verboden praktijken (art. 5)

Gelden sinds 2 februari 2025. Verboden is AI die:
- (a) subliminale, doelbewust manipulatieve of misleidende technieken gebruikt die gedrag wezenlijk verstoren en aanzienlijke schade (kunnen) veroorzaken;
- (b) kwetsbaarheden uitbuit door leeftijd, handicap of een specifieke sociale of economische situatie, met aanzienlijke schade;
- (c) sociale scoring doet die leidt tot nadelige behandeling buiten de context of onevenredig;
- (d) het risico op strafbare feiten voorspelt uitsluitend op basis van profilering of persoonlijkheidskenmerken;
- (e) ongericht gezichtsafbeeldingen van internet of camerabeelden schraapt voor gezichtsherkenningsdatabanken;
- (f) emoties afleidt op de werkplek of in het onderwijs, behalve om medische of veiligheidsredenen;
- (g) personen biometrisch categoriseert naar ras, politieke opvattingen, vakbondslidmaatschap, religie, seksleven of seksuele geaardheid;
- (h) realtime biometrische identificatie op afstand in openbare ruimten gebruikt voor rechtshandhaving (op enkele strikte uitzonderingen na).

Nieuw via de Digital Omnibus, vanaf 2 december 2026: AI die zonder toestemming intieme beelden van echte personen genereert of manipuleert ("nudify"), en AI voor materiaal van seksueel kindermisbruik.

Richtsnoeren van de Commissie over verboden praktijken (februari 2025) geven voorbeelden. **Emotieherkenning** in de zin van de wet is afgeleid uit biometrische gegevens (gezicht, stem, lichaamstaal). Sentimentanalyse van getypte tekst valt daar volgens de richtsnoeren niet onder.

Een pilot of test met echte mensen geeft geen vrijstelling: de verboden gelden ook dan, en ook voor de gebruiksverantwoordelijke, niet alleen voor de leverancier. De regeling voor testen onder reële omstandigheden (art. 60) is bedoeld voor hoog-risicosystemen en dekt geen verboden praktijken.

Als een verboden praktijk aan de orde is: stop. Beheersmaatregelen maken een verboden praktijk niet toelaatbaar; alleen een ander ontwerp.

## 6. Hoog risico (art. 6, bijlage I en III)

**Route 1, bijlage I:** het AI-systeem is (een veiligheidscomponent van) een product onder EU-productwetgeving waarvoor een conformiteitsbeoordeling door derden nodig is. Productgroepen: machines, speelgoed, pleziervaartuigen, liften, apparatuur voor explosieve omgevingen, radioapparatuur, drukapparatuur, kabelbanen, persoonlijke beschermingsmiddelen, gastoestellen, medische hulpmiddelen en in-vitrodiagnostiek, burgerluchtvaart, voertuigen, landbouw- en bosbouwvoertuigen, scheepsuitrusting, spoorwegen, drones. Sinds de Omnibus telt alleen een component met een veiligheidsdoel als veiligheidscomponent; puur gemak of efficiëntie niet.

**Route 2, bijlage III:** het beoogde gebruik valt in een van deze gebieden:
1. Biometrie: biometrische identificatie op afstand (niet: verificatie dat iemand is wie hij zegt), biometrische categorisering op gevoelige kenmerken, emotieherkenning.
2. Kritieke infrastructuur: veiligheidscomponenten in digitale infrastructuur, verkeer, water, gas, warmte, elektriciteit.
3. Onderwijs en beroepsopleiding: toelating, beoordeling van leerresultaten, niveaubepaling, toezicht op examens.
4. Werkgelegenheid en personeelsbeheer: werving en selectie (vacatures richten, cv's filteren, kandidaten beoordelen), besluiten over arbeidsvoorwaarden, promotie, ontslag, taaktoewijzing op basis van gedrag of kenmerken, en monitoren en beoordelen van prestaties en gedrag.
5. Essentiële diensten: toegang tot overheidsuitkeringen en zorg, kredietwaardigheid en kredietscores (behalve fraudedetectie), risicobeoordeling en prijsstelling voor levens- en ziektekostenverzekeringen, triage van noodoproepen.
6. Rechtshandhaving.
7. Migratie, asiel en grenscontrole.
8. Rechtspleging en democratische processen (inclusief beïnvloeding van verkiezingen).

**Uitzondering art. 6(3):** een bijlage III-systeem is toch geen hoog risico als het geen significant risico vormt, bijvoorbeeld omdat het alleen een beperkte procedurele taak doet, een eerder menselijk besluit verbetert, patronen opspoort zonder het menselijk oordeel te vervangen, of een voorbereidende taak doet. **Maar:** een systeem dat profilering van natuurlijke personen uitvoert, is altijd hoog risico. Wie zich op de uitzondering beroept, moet dat documenteren.

**Plichten voor aanbieders van hoog-risico-AI:** risicobeheer (art. 9), datagovernance (10), technische documentatie (11), logging (12), transparantie en gebruiksinstructies (13), menselijk toezicht (14), nauwkeurigheid, robuustheid en cyberbeveiliging (15), kwaliteitsbeheersysteem (17), conformiteitsbeoordeling (43), EU-conformiteitsverklaring (47), CE-markering (48), registratie in de EU-databank (49), corrigerende maatregelen en meldplicht (20, 73).

**Plichten voor gebruiksverantwoordelijken van hoog-risico-AI (art. 26):** gebruik volgens instructies; menselijk toezicht door bekwame, bevoegde personen; relevante en representatieve inputdata waar zij daar zeggenschap over hebben; monitoring en melding van risico's en ernstige incidenten; logs minstens zes maanden bewaren; werknemers en hun vertegenwoordigers informeren vóór inzet op de werkplek; betrokkenen informeren bij besluiten door bijlage III-systemen; samenwerken met toezichthouders. Overheidsinstanties en bepaalde private partijen (o.a. kredietwaardigheid, levens- en zorgverzekering) voeren daarnaast een grondrechteneffectbeoordeling (FRIA) uit (art. 27). Betrokkenen hebben recht op uitleg bij besluiten die hen aanzienlijk raken (art. 86).

## 7. Transparantie (art. 50)

Geldt sinds 2 augustus 2026 (niet uitgesteld door de Omnibus).
- **50(1) aanbieder:** AI die rechtstreeks met mensen communiceert (chatbot, spraakassistent) zo ontwerpen dat mensen weten dat ze met een AI te maken hebben, tenzij dat voor een redelijk geïnformeerd persoon evident is. Uiterlijk bij de eerste interactie, duidelijk en toegankelijk (50(5)).
- **50(2) aanbieder:** synthetische audio, beeld, video of tekst machineleesbaar markeren als kunstmatig gegenereerd (bijv. watermerk, metadata, C2PA), voor zover technisch haalbaar. Voor generatieve systemen die vóór 2 augustus 2026 al op de markt waren: uiterlijk 2 december 2026.
- **50(3) gebruiksverantwoordelijke:** mensen informeren als emotieherkenning of biometrische categorisering op hen wordt toegepast.
- **50(4) gebruiksverantwoordelijke:** deepfakes als zodanig kenbaar maken; AI-gegenereerde tekst die wordt gepubliceerd om het publiek te informeren over zaken van algemeen belang kenbaar maken, tenzij er menselijke redactie en redactionele verantwoordelijkheid is.

## 8. AI-geletterdheid (art. 4)

Geldt voor alle aanbieders en gebruiksverantwoordelijken, ongeacht risicoklasse, sinds 2 februari 2025. Na de Omnibus: zij nemen maatregelen om de AI-geletterdheid van hun personeel en van anderen die namens hen met AI werken te bevorderen, rekening houdend met kennis, ervaring, context en de mensen op wie de AI wordt toegepast. Geen gegarandeerd niveau per persoon, wel aantoonbare, passende maatregelen. Goede praktijk: per rol bepalen wat iemand moet weten en kunnen, en bewijs bijhouden (zie ethiek-en-toezicht.md).

## 9. AI-modellen voor algemene doeleinden (GPAI)

Plichten voor aanbieders van GPAI-modellen (documentatie, auteursrechtbeleid, samenvatting trainingsdata; extra plichten bij systeemrisico) gelden sinds 2 augustus 2025. Een organisatie die een model via een API gebruikt, is daarvoor geen aanbieder, maar wel afhankelijk van de informatie die de modelaanbieder geeft. Noem in het rapport welke modelleverancier wordt gebruikt en of die de gedragscode voor GPAI heeft ondertekend, als dat relevant is.

## 10. Tijdlijn (na Digital Omnibus)

| Datum | Wat |
|---|---|
| 1 aug 2024 | AI-verordening in werking |
| 2 feb 2025 | Verboden praktijken (art. 5) en AI-geletterdheid (art. 4) |
| 2 aug 2025 | GPAI-plichten, governance, sancties |
| 27 jul 2026 | Digital Omnibus (Vo. 2026/1744) in werking |
| 2 aug 2026 | Transparantie (art. 50) |
| 2 dec 2026 | Markering (50(2)) voor bestaande generatieve systemen; nieuwe verboden (intieme deepfakes, CSAM) |
| 2 dec 2027 | Hoog risico, bijlage III |
| 2 aug 2028 | Hoog risico, bijlage I |

## 11. Handhaving en boetes (art. 99)

Verboden praktijken: tot €35 miljoen of 7% van de wereldwijde jaaromzet. Overige plichten: tot €15 miljoen of 3%. Onjuiste informatie aan toezichthouders: tot €7,5 miljoen of 1%. Voor mkb geldt het laagste van de twee bedragen. In Nederland zijn de Autoriteit Persoonsgegevens en de Rijksinspectie Digitale Infrastructuur (RDI) voorzien als centrale toezichthouders, naast sectortoezichthouders binnen hun domein; controleer de stand van de Nederlandse uitvoeringswet. Voor andere landen: noem de nationale markttoezichthouder als die bekend is, anders als open punt.
