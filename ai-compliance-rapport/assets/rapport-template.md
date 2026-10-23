# Rapporttemplate

Gebruik de Nederlandse of Engelse versie, afhankelijk van de taal van de gebruiker. Voor een andere taal: vertaal de Engelse versie, inclusief de koppen. Houd de opbouw en de volgorde van de koppen gelijk; de hoofdstukken 2 en 3 volgen de vragen van een standaard AI-businesscase, zodat ze daar direct in passen.

Schrijf het rapport in Markdown volgens dit template en zet het om met `scripts/build_docx.py`. Tekst tussen [vierkante haken] is instructie, geen rapporttekst.

---

## Nederlandse versie

```markdown
# AI-toets: [naam toepassing]

**Organisatie:** [naam] · **Datum:** [datum] · **Stand van de wet gecontroleerd op:** [datum zoekcheck]
**Status toepassing:** [idee / pilot / in gebruik] · **Opgesteld met:** AI-ondersteunde eerste screening

> Dit rapport is een eerste juridische en ethische screening op basis van de informatie die de organisatie heeft verstrekt. Het is geen juridisch advies. Laat de conclusies toetsen door een jurist of functionaris gegevensbescherming voordat u er besluiten op baseert. Uitspraken zijn gemarkeerd als [Weten] (bevestigd), [Aannemen] (gebruikt, nog niet bevestigd) of [Niet weten] (informatie ontbreekt).

## 1. Samenvatting

[Begin met de conclusie in 3–5 zinnen: wat is de toepassing, is het een AI-systeem, welke rol heeft de organisatie, welke risicoklasse, en onder welke voorwaarden kan zij verder. Daarna maximaal 5 bullets met de belangrijkste voorwaarden of acties, met deadline.]

**Advies:** [Doorgaan / Doorgaan onder voorwaarden / Onderzoeken / Herontwerpen / Stoppen]

[Lengte: de hoofdtekst (hoofdstuk 1 t/m 3) blijft onder de 1.800 woorden; details naar de bijlagen.]

## 2. Juridische & compliance-overwegingen

### 2.1 De AI-verordening in het kort

[Standaardtekst van ca. 100–150 woorden in gewone taal: wat de AI-verordening regelt, de definitie van een AI-systeem, de rollen (aanbieder, gebruiksverantwoordelijke), de vier risicoklassen, AI-geletterdheid (art. 4), en de relevante datums uit de tijdlijn. Pas aan op wat voor deze lezer relevant is.]

### 2.2 Wat is AI in deze toepassing?

| Onderdeel | AI-systeem? | Onderbouwing (art. 3(1)) | Gebruikte of ontbrekende informatie |
|---|---|---|---|

[Leg in één zin de systeemgrens vast.]

[Alleen bij een bestaande tool of pilot die je zelf hebt geanalyseerd:]

| Kenmerk | Zo bedoeld (organisatie / businesscase) | Zo werkt het (vastgesteld, met bron) | Gevolg |
|---|---|---|---|

### 2.3 Rol- & risicoclassificatie

[Rol(len) met de activiteit die de rol bepaalt. Daarna de classificatie langs: verboden praktijken, bijlage I, bijlage III (incl. art. 6(3)), profilering, transparantie (art. 50). Eindclassificatie met deadline. Onzekerheden expliciet.]

### 2.4 Toepasselijke vereisten

[AI-verordening (per rol × risico), AVG, en andere wetgeving die waarschijnlijk geldt (arbeidsrecht/OR, consumentenrecht, IE, aansprakelijkheid, cyber, sector). Kort per kader: waarom het geldt.]

### 2.5 Compliancemaatregelen

| Verplichting (artikel) | Maatregel | Eigenaar | Bewijs | Status / deadline |
|---|---|---|---|---|

[Maximaal acht regels; voeg samenhangende plichten samen.]

### 2.6 Openstaande juridische punten

| Vraag | Wie valideert (Legal, FG/DPO, Compliance, Inkoop, OR) | Wanneer | Impact als het anders uitvalt |
|---|---|---|---|

## 3. Ethiek, stakeholders & menselijk toezicht

### 3.1 Stakeholders

| Belanghebbende | Voordeel | Risico | Maatregel |
|---|---|---|---|

[Eén alinea: waar botsen belangen, en wie draagt het risico zonder het voordeel?]

### 3.2 Mogelijke negatieve effecten

[Concreet, per effect: wat kan er gebeuren, bij wie, hoe waarschijnlijk, welke maatregel.]

### 3.3 Waarden & afwegingen

[Minstens twee spanningen, met de gemaakte keuze en waarom. Geen opsomming van principes zonder afweging.]

### 3.4 Menselijk toezicht

| Vermogen | Hoe geregeld | Wie | Zwakke plek |
|---|---|---|---|
| Begrijpen | | | |
| Kritisch beoordelen | | | |
| Overrulen | | | |
| Escaleren en stoppen | | | |

### 3.5 Transparantie & verantwoording

[Wie moet weten dat AI wordt gebruikt en hoe; hoe kunnen betrokkenen aanvechten of weigeren; wie is eigenaar en verantwoordelijk voor uitkomsten en escalatie. Plus AI-geletterdheid per rol.]

### 3.6 Herontwerpopties

[Alleen als er rode vlaggen zijn: welk onderdeel, welk alternatief, wat het kost aan waarde, welk nieuw risico.]

## Bijlage A. Feitenoverzicht

| Uitspraak | Weten / Aannemen / Niet weten | Bron of wie valideert |
|---|---|---|

## Bijlage B. AI-register

| Systeem | Doel | Eigenaar | Leverancier(s) | Rol(len) | Classificatie (datum) | Open verplichtingen | Volgende herbeoordeling |
|---|---|---|---|---|---|---|---|

## Bijlage C. Praktische handvatten

[Eén tot drie handvatten die passen bij deze toepassing, zie references/praktische-handvatten.md. Kort en direct bruikbaar.]

## Bijlage D. Bronnen

[Verordening (EU) 2024/1689; Verordening (EU) 2026/1744; Verordening (EU) 2016/679; richtsnoeren van de Europese Commissie (definitie AI-systeem, verboden praktijken); Ethische richtsnoeren voor betrouwbare AI (AI HLEG, 2019); en de bronnen van de zoekcheck met datum.]
```

---

## English version

```markdown
# AI Assessment: [name of application]

**Organisation:** [name] · **Date:** [date] · **Legal status checked on:** [date of search check]
**Status of application:** [idea / pilot / in use] · **Prepared with:** AI-assisted initial screening

> This report is an initial legal and ethical screening based on the information provided by the organisation. It is not legal advice. Have the conclusions reviewed by a lawyer or data protection officer before relying on them. Statements are marked [Known] (confirmed), [Assumed] (used but not yet confirmed) or [Unknown] (information missing).

## 1. Summary

**Recommendation:** [Proceed / Proceed with conditions / Investigate / Redesign / Stop]

## 2. Legal & compliance considerations

### 2.1 The AI Act in brief
### 2.2 What is AI in this application?
| Component | AI system? | Rationale (Art. 3(1)) | Information used or missing |
|---|---|---|---|
[Existing tool or pilot only:]
| Feature | As intended (organisation / business case) | As it actually works (verified, with source) | Consequence |
|---|---|---|---|
### 2.3 Role & risk classification
### 2.4 Applicable requirements
### 2.5 Compliance measures
| Obligation (article) | Measure | Owner | Evidence | Status / deadline |
|---|---|---|---|---|
### 2.6 Open legal questions
| Question | Who validates (Legal, DPO, Compliance, Procurement, works council) | When | Impact if it turns out differently |
|---|---|---|---|

## 3. Ethics, stakeholders & human oversight

### 3.1 Stakeholders
| Stakeholder | Benefit | Risk | Measure |
|---|---|---|---|
### 3.2 Potential negative effects
### 3.3 Values & trade-offs
### 3.4 Human oversight
| Capability | How it is arranged | Who | Weak point |
|---|---|---|---|
| Understand | | | |
| Critically assess | | | |
| Override | | | |
| Escalate and stop | | | |
### 3.5 Transparency & accountability
### 3.6 Redesign options

## Annex A. Fact base
| Statement | Known / Assumed / Unknown | Source or who validates |
|---|---|---|

## Annex B. AI system register
| System | Purpose | Owner | Supplier(s) | Role(s) | Classification (date) | Open obligations | Next review |
|---|---|---|---|---|---|---|---|

## Annex C. Practical tools
[One to three ready-to-use tools that fit this application.]

## Annex D. Sources
```

The instructions in square brackets in the Dutch version apply equally to the English version.
