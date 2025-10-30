# Grounding Instructions for AI Generation
## Anti-Hallucination Guidelines

**Version:** 1.0
**Purpose:** Prevent AI from inventing facts not present in input data

---

## Core Principle

**USE ONLY the provided project data.** When information is missing or insufficient, FLAG IT rather than inventing details.

---

## DO NOT INVENT (Strict Rules)

### ❌ Absolutely Forbidden

**Names & Identities:**
- ❌ People names (other than provided "Osoba odpowiedzialna")
- ❌ Company names (client, partner, supplier)
- ❌ Department or team names
- ❌ External collaborators or consultants

**Numbers & Quantities:**
- ❌ Specific costs (e.g., "500,000 PLN na personel")
- ❌ Budget breakdowns by category
- ❌ Team sizes (e.g., "5 inżynierów, 2 techników")
- ❌ Performance metrics not in input (e.g., "40% wzrost wydajności")
- ❌ Technical specifications not mentioned (e.g., "ciśnienie 150 bar")

**Dates & Timelines:**
- ❌ Specific milestones not derivable from start/end dates
- ❌ Intermediate deadlines
- ❌ Phase durations (unless logically derived from total timeline)

**Technologies & Tools:**
- ❌ Specific software names (e.g., "SAP", "Siemens NX")
- ❌ Equipment models (e.g., "Frezarka CNC Haas VF-2")
- ❌ Standards or certifications not mentioned (e.g., "ISO 9001")
- ❌ Vendor or technology partnerships

**Locations & Facilities:**
- ❌ Cities, regions, or addresses
- ❌ Laboratory or facility names
- ❌ Testing locations

---

## MAY INFER (Acceptable Generalizations)

### ✓ Allowed Inferences

**General R&D Methodology:**
- ✓ "Projekt wykorzystuje iteracyjne podejście badawcze" (iterative research approach)
- ✓ "Zastosowano metodę prototypowania" (prototyping method)
- ✓ "Prace obejmują analizę, projektowanie, testy" (analysis, design, testing)
- ✓ Standard R&D phases appropriate to project type

**Generic Tools & Techniques:**
- ✓ "narzędzia CAD" (CAD tools) - generic, not specific brand
- ✓ "oprogramowanie symulacyjne" (simulation software) - generic
- ✓ "stanowisko testowe" (test bench) - generic
- ✓ "komora klimatyczna" (climate chamber) - generic equipment type

**Typical Cost Categories (WITHOUT amounts):**
- ✓ "koszty osobowe pracowników B+R" (R&D personnel costs)
- ✓ "materiały i surowce zużyte w pracach B+R" (R&D materials)
- ✓ "amortyzacja aparatury badawczej" (depreciation of research equipment)
- ✓ "usługi zewnętrzne" (external services)

**Standard R&D Challenges (if relevant to project type):**
- ✓ "optymalizacja parametrów procesu" (process parameter optimization)
- ✓ "zapewnienie powtarzalności" (ensuring repeatability)
- ✓ "integracja komponentów" (component integration)
- ✓ Only if logically applicable to the described project

**Timeline Phases (derived from start/end dates):**
- ✓ For 1-year project: "faza planowania (miesiące 1-2), rozwoju (3-9), walidacji (10-12)"
- ✓ For multi-year: "rok 1: badania wstępne, rok 2: rozwój, rok 3: testy"
- ✓ Must be proportional to total duration

---

## Uncertainty Handling

### When Information is Insufficient

**Use Conditional Language:**
- ✓ "Przewiduje się..." (It is foreseen that...)
- ✓ "Zakłada się..." (It is assumed that...)
- ✓ "Planowane są..." (Planned are...)
- ✓ "W ramach projektu mogą być..." (Within the project may be...)

**Flag for Consultant Review:**
- ✓ [WYMAGA WERYFIKACJI: Szczegółowe kwoty kosztów]
- ✓ [WYMAGA WERYFIKACJI: Konkretne narzędzia i oprogramowanie]
- ✓ [WYMAGA WERYFIKACJI: Skład zespołu badawczego]
- ✓ [WYMAGA WERYFIKACJI: Szczegółowy harmonogram z kamieniami milowymi]

**Provide Framework, Not Details:**
```
Instead of:
❌ "Koszty osobowe: 300,000 PLN, materiały: 50,000 PLN"

Write:
✓ "Główne kategorie kosztów obejmują wynagrodzenia pracowników
   zaangażowanych w prace B+R, materiały zużyte podczas testów
   oraz amortyzację sprzętu badawczego. [WYMAGA WERYFIKACJI:
   Szczegółowe kwoty do uzupełnienia przez konsultanta]"
```

---

## Factual Consistency Rules

### Cross-Reference Validation

**Names:**
- ✓ Project name must match input EXACTLY (character-by-character)
- ✓ Responsible person name must match input EXACTLY

**Dates:**
- ✓ Start date must match input EXACTLY (format: YYYY-MM-DD)
- ✓ End date must match input EXACTLY
- ✓ All derived dates must fall within [start_date, end_date] range
- ✓ No events before start_date or after end_date

**Consistency Across Sections:**
- ✓ If Section 2 mentions "system składający się z 3 modułów", Section 5 (Problems) should discuss challenges related to these 3 modules
- ✓ If Section 4 mentions "testowanie w warunkach rzeczywistych", Section 6 (Results) should reference test outcomes
- ✓ If Section 8 mentions "projekt trzyletni", description should reflect multi-year scope

---

## Domain-Appropriate Generalizations

### IT/Software Projects

**Allowed:**
- ✓ "technologie webowe" (web technologies)
- ✓ "bazy danych" (databases)
- ✓ "interfejsy API" (API interfaces)
- ✓ "architektura mikroserwisów" (microservices architecture)
- ✓ "testy jednostkowe i integracyjne" (unit and integration tests)

**Forbidden:**
- ❌ Specific frameworks (React, Angular, Django)
- ❌ Specific databases (PostgreSQL, MongoDB)
- ❌ Cloud providers (AWS, Azure, GCP)

### Manufacturing Projects

**Allowed:**
- ✓ "linia produkcyjna" (production line)
- ✓ "stanowisko obróbki" (processing station)
- ✓ "kontrola jakości" (quality control)
- ✓ "parametry procesu technologicznego" (process parameters)

**Forbidden:**
- ❌ Specific machine brands (Siemens, Haas, Trumpf)
- ❌ Specific material suppliers
- ❌ Exact production capacity numbers

### Construction Projects

**Allowed:**
- ✓ "normy budowlane" (building standards)
- ✓ "materiały konstrukcyjne" (construction materials)
- ✓ "obliczenia statyczne" (static calculations)
- ✓ "symulacje MES" (FEM simulations)

**Forbidden:**
- ❌ Specific construction sites or addresses
- ❌ Client building names
- ❌ Specific regulation numbers (unless in input)

### Energy/Industrial Projects

**Allowed:**
- ✓ "efektywność energetyczna" (energy efficiency)
- ✓ "normy emisji" (emission standards)
- ✓ "systemy automatyki" (automation systems)
- ✓ "procesy spalania" (combustion processes)

**Forbidden:**
- ❌ Specific power plant names
- ❌ Exact efficiency percentages (unless in input)
- ❌ Specific fuel types or suppliers

---

## Quality Assurance Checklist

Before finalizing generated content, verify:

### Factual Accuracy
- [ ] Project name matches input exactly
- [ ] Start date matches input exactly
- [ ] End date matches input exactly
- [ ] Responsible person matches input exactly
- [ ] No invented company, partner, or people names
- [ ] No invented specific costs or budget numbers
- [ ] No invented equipment models or software names
- [ ] No dates outside [start_date, end_date] range

### Appropriate Inference
- [ ] Generic terms used instead of specific brands/names
- [ ] R&D methodology appropriate to project type
- [ ] Cost categories described without amounts (or flagged)
- [ ] Timeline phases logically derived from duration
- [ ] Technical challenges relevant to described project

### Flagging
- [ ] Missing cost details flagged with [WYMAGA WERYFIKACJI]
- [ ] Missing team composition flagged
- [ ] Missing specific technologies flagged
- [ ] Missing detailed timeline flagged
- [ ] Any uncertain statements use conditional language

### Consistency
- [ ] All sections internally consistent
- [ ] No contradictions between sections
- [ ] References across sections align
- [ ] Terminology consistent throughout

---

## Example: Before & After

### ❌ WRONG (Hallucinated Content)

```
Projekt realizowany będzie przez zespół 8 osób, w tym 5 inżynierów
oprogramowania i 3 testerów. Wykorzystamy technologie React, Node.js,
PostgreSQL oraz AWS. Budżet projektu wynosi 500,000 PLN, w tym 350,000 PLN
na wynagrodzenia. Testy przeprowadzimy w laboratorium IT na ul. Piotrkowskiej
w Łodzi. Projekt będzie nadzorowany przez firmę konsultingową Deloitte.
```

**Problems:**
- Invented team size and composition
- Specific technologies not in input
- Specific budget numbers
- Location (ul. Piotrkowska, Łódź)
- External partner (Deloitte)

### ✓ CORRECT (Grounded Content)

```
Projekt realizowany będzie przez zespół pracowników B+R przedsiębiorstwa
[WYMAGA WERYFIKACJI: Skład zespołu]. Wykorzystane zostaną nowoczesne
technologie webowe, systemy bazodanowe oraz infrastruktura chmurowa
odpowiednie do budowy skalowalnych aplikacji. Główne kategorie kosztów
obejmują wynagrodzenia personelu B+R, licencje na narzędzia programistyczne,
oraz infrastrukturę serwerową [WYMAGA WERYFIKACJI: Szczegółowe kwoty].
Testy funkcjonalne i integracyjne przeprowadzone zostaną w środowisku
testowym przedsiębiorstwa zgodnie z ustaloną metodyką.
```

**Improvements:**
- Generic team description with verification flag
- Generic technology categories
- Cost categories without amounts, flagged
- Generic testing approach
- No invented names or locations

---

## Red Flags During Review

If you see these patterns, it's likely hallucination:

🚩 **Specific numbers** appearing suddenly (costs, team sizes, metrics)
🚩 **Brand names** or **product names** not in input
🚩 **Person names** other than "Osoba odpowiedzialna"
🚩 **Company names** (partners, suppliers, clients)
🚩 **Locations** (cities, addresses, facilities)
🚩 **Dates** with day-level precision not derivable from input
🚩 **Technical specifications** with exact values (unless in input)

**Action:** Remove and replace with generic description or [WYMAGA WERYFIKACJI] flag.

---

## Summary: The Golden Rule

> **"If you can't clearly trace it back to the input data, don't include it."**

When in doubt:
1. Use generic terms
2. Flag with [WYMAGA WERYFIKACJI]
3. Provide framework for consultant to complete

**Better to have gaps that consultant fills than invented facts that undermine credibility.**

---

**End of Grounding Instructions**
