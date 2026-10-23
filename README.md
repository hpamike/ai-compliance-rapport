# AI-compliance-rapport

Een Claude-skill die een AI-toepassing in een organisatie toetst aan de EU AI-verordening (AI Act), de AVG en andere wetgeving, en de ethiek, stakeholders en het menselijk toezicht beoordeelt. Het resultaat is een kort Word-rapport voor management.

> **Geen juridisch advies.** Een hulpmiddel om zelf een afweging te maken. Fouten zijn mogelijk: laat de uitkomsten altijd controleren door een specialist. / *Not legal advice. A tool to support your own assessment. Errors are possible: always have the results reviewed by a specialist.*

*English below.*

## Wat de skill doet

De skill werkt als juridisch adviseur en doorloopt vaste stappen:

1. **Stand van de wet controleren.** De skill is bijgewerkt tot en met de Digital Omnibus (Verordening (EU) 2026/1744) en controleert bij gebruik of er sindsdien iets is veranderd.
2. **Intake.** Maximaal acht vragen over de toepassing, leveranciers, gegevens en betrokkenen.
3. **Bestaande tool of pilot analyseren.** Code, live tool (alleen met toestemming), leveranciersdocumenten en pilotgegevens, met een tabel "zo bedoeld, zo werkt het".
4. **Inventaris.** Per onderdeel: AI-systeem, geen AI-systeem of onzeker (art. 3(1)).
5. **Rollen.** Aanbieder, gebruiksverantwoordelijke, importeur, distributeur.
6. **Risicoclassificatie.** Verboden praktijken, hoog risico (bijlage I en III), profilering, transparantie (art. 50).
7. **Verplichtingen → maatregelen → bewijs.** Inclusief AVG, arbeidsrecht en ondernemingsraad, consumentenrecht, beroepsregels en aansprakelijkheid.
8. **Ethiek, stakeholders en menselijk toezicht.** Wie heeft voordeel, wie draagt het risico, en kan een mens begrijpen, beoordelen, overrulen en escaleren?
9. **Rode vlaggen en herontwerp.** Het eenvoudigste verantwoorde ontwerp dat genoeg waarde behoudt.
10. **Rapport in Word**, met praktische handvatten als bijlage (zoals een gebruiksbeleid, een stoplichttabel, een tekst voor de AI-melding of een checklist voor leveranciers).

De hoofdstukken heten "Juridische & compliance-overwegingen" en "Ethiek, stakeholders & menselijk toezicht", zodat ze direct in een AI-businesscase passen. De skill schrijft in het Nederlands of Engels, en vertaalt naar de taal van de gebruiker.

## Installeren

- **Claude.ai of de Claude-app:** download `ai-compliance-rapport.skill` bij [Releases](../../releases) en upload hem in Claude bij de instellingen voor Skills.
- **Claude Code:** kopieer de map `ai-compliance-rapport/` naar `~/.claude/skills/`.

Het Word-rapport wordt gemaakt met `scripts/build_docx.py` in AI FiT-huisstijl (logo en AIFiT.nu in de koptekst, een disclaimer over mogelijke fouten door AI in de voettekst). Met `--neutraal` laat je logo en AIFiT.nu weg. Het script heeft `python-docx` nodig (`pip install python-docx`).

## Gebruik

Vraag bijvoorbeeld: *"Toets onze nieuwe HR-tool aan de AI Act en maak een rapport in Word"*, of geef de code of documentatie van een bestaande pilot en vraag om een analyse.

## Belangrijk: geen juridisch advies

Deze skill en de rapporten die hij maakt zijn **geen juridisch advies**. Ze zijn een hulpmiddel om zelf een afweging te maken over een AI-toepassing.

- De rapporten worden met AI gemaakt. **Fouten, onvolledigheden en verouderde informatie zijn mogelijk.**
- **Laat de uitkomsten altijd controleren door een specialist**, zoals een jurist of functionaris gegevensbescherming, voordat u er besluiten op baseert.
- Wetgeving en de uitleg ervan veranderen. Elk rapport vermeldt tot welke datum de stand van de wet is gecontroleerd.
- De skill wordt geleverd zoals hij is, zonder garantie. De makers aanvaarden geen aansprakelijkheid voor gevolgen van het gebruik ervan (zie ook artikel 5 van de [licentie](LICENSE)).

Elk rapport bevat deze boodschap bovenaan en in de slotzin, en de skill herhaalt hem bij het opleveren.

## Testcases

In `ai-compliance-rapport/evals/` staan drie verzonnen cases (hoog risico, verboden, minimaal risico) met controleerbare criteria. Met Claude Code kun je ze draaien met `claude plugin eval .` vanuit de skillmap.

## Licentie

[CC BY 4.0](LICENSE): vrij te gebruiken, delen en aanpassen, ook commercieel, met naamsvermelding: *AI-compliance-rapport, Mike Rijkers*.

---

## English

A Claude skill that assesses an AI application in an organisation against the EU AI Act, the GDPR and other laws, and evaluates ethics, stakeholders and human oversight. It produces a short Word report for management.

It works like a legal adviser: it checks the current state of the law (updated through the Digital Omnibus, Regulation (EU) 2026/1744), takes in the facts, analyses an existing tool or pilot (code, live tool with permission, vendor documents), classifies each component, determines roles and risk class, translates obligations into measures with owners and evidence, assesses ethics and human oversight, flags designs that drift towards high-risk or prohibited, and adds practical tools as annexes.

**Install:** download `ai-compliance-rapport.skill` from [Releases](../../releases) and upload it in Claude's Skills settings, or copy `ai-compliance-rapport/` to `~/.claude/skills/` for Claude Code. The Word export needs `python-docx`.

**Language:** Dutch or English by default; the skill translates to the user's language.

**Not legal advice:** the skill and its reports are a tool to support your own assessment, not legal advice. Reports are generated with AI, so errors, omissions and outdated information are possible. Always have the results reviewed by a specialist (a lawyer or data protection officer) before relying on them. Provided as is, without warranty; the authors accept no liability for consequences of its use (see also section 5 of the [license](LICENSE)).

**License:** [CC BY 4.0](LICENSE). Attribution: *AI-compliance-rapport, Mike Rijkers*.
