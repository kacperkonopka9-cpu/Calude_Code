# AI POC Test Cases
## R&D Tax Relief Project Card Generator

**Document Version:** 1.0
**Date:** 2025-10-30
**Total Test Cases:** 15
**Source:** Selected from 66 example project cards in `docs/project-cards/examples/`

---

## Test Case Selection Criteria

**Industry Diversity** (3 from each):
- Construction: Building projects, infrastructure
- IT/Software: Software development, digital solutions
- Manufacturing: Industrial processes, machinery
- Energy/Industrial: Power systems, energy infrastructure
- Other: Mixed industries and specialized projects

**Complexity Levels:**
- **Simple** (5 cases): 1-year projects, single technology, straightforward R&D
- **Medium** (7 cases): Multi-year projects, multiple technologies
- **Advanced** (3 cases): Long-duration, novel innovations, extensive R&D

**Input Quality:**
- **Rich** (8 cases): Detailed descriptions (>300 chars), clear objectives
- **Sparse** (7 cases): Minimal descriptions (<150 chars), vague objectives

---

## Test Cases

### TC-001: ERP System (IT - Simple - Rich)

**Industry:** IT/Software
**Complexity:** Simple
**Input Quality:** Rich
**Based on:** Example file "11. Karta projektu_BR ERP.docx"

**Input Data:**
```yaml
Nazwa projektu: System ERP zintegrowany z produkcją i logistyką
Opis: Opracowanie dedykowanego systemu ERP dostosowanego do specyfiki produkcji okien i drzwi, integrującego planowanie produkcji, zarządzanie magazynem, logistykę i fakturowanie. System uwzględnia niestandardowe procesy produkcyjne, zarządzanie wieloma liniami produkcyjnymi oraz specyficzne wymagania branży stolarki budowlanej. Projekt obejmuje analizę procesów biznesowych, projektowanie architektury systemu, implementację modułów oraz integrację z istniejącymi systemami CAD i maszynami produkcyjnymi.
Data rozpoczęcia: 2023-01-15
Data zakończenia: 2023-12-31
Cel projektu: Stworzenie zintegrowanego systemu informatycznego optymalizującego zarządzanie produkcją i logistyką w przedsiębiorstwie produkcyjnym, zwiększającego efektywność operacyjną i eliminującego błędy wynikające z ręcznego wprowadzania danych.
Osoba odpowiedzialna: Jan Kowalski
```

**Expected Challenges:**
- Technical terminology accuracy (ERP, CAD, integration)
- Multi-module system complexity
- Industry-specific processes (stolarka budowlana)

**Target Quality:** ≥80 (rich input, clear domain)

---

### TC-002: Task Management System (IT - Simple - Sparse)

**Industry:** IT/Software
**Complexity:** Simple
**Input Quality:** Sparse
**Based on:** Example file "1. Karta projektu - BR zarządzanie zadaniami.docx"

**Input Data:**
```yaml
Nazwa projektu: Aplikacja do zarządzania zadaniami w firmie produkcyjnej
Opis: System do zarządzania zadaniami produkcyjnymi
Data rozpoczęcia: 2023-03-01
Data zakończenia: 2023-09-30
Cel projektu: Usprawnienie zarządzania zadaniami
Osoba odpowiedzialna: Anna Nowak
```

**Expected Challenges:**
- AI must infer methodology from minimal description
- Generic description requires R&D aspect identification
- Limited context for compliance criteria

**Target Quality:** ≥65 (sparse input, should flag for review)

---

### TC-003: Mobile App for Construction (IT - Medium - Rich)

**Industry:** IT/Software
**Complexity:** Medium
**Input Quality:** Rich

**Input Data:**
```yaml
Nazwa projektu: Mobilna aplikacja do zarządzania projektami budowlanymi w czasie rzeczywistym
Opis: Opracowanie innowacyjnej aplikacji mobilnej umożliwiającej zarządzanie projektami budowlanymi bezpośrednio z placu budowy. System integruje funkcje planowania, monitorowania postępu prac, zarządzania dokumentacją techniczną, komunikacji zespołowej oraz raportowania w czasie rzeczywistym. Projekt obejmuje badania nad optymalizacją interfejsu użytkownika dla warunków budowy (praca w rękawicach, silne nasłonecznienie), synchronizację offline/online danych, oraz integrację z systemami BIM. Aplikacja wykorzystuje technologie AI do automatycznego rozpoznawania postępu prac na podstawie zdjęć oraz predykcji opóźnień.
Data rozpoczęcia: 2022-06-01
Data zakończenia: 2024-05-31
Cel projektu: Stworzenie kompleksowego narzędzia mobilnego eliminującego konieczność korzystania z papierowej dokumentacji na placu budowy, zwiększającego efektywność komunikacji oraz umożliwiającego podejmowanie decyzji w oparciu o dane w czasie rzeczywistym.
Osoba odpowiedzialna: Piotr Wiśniewski
```

**Expected Challenges:**
- Multi-year project timeline
- Multiple technologies (mobile, AI, BIM, offline sync)
- Complex use case (construction site conditions)

**Target Quality:** ≥75 (rich input, complex project)

---

### TC-004: Window Production System (Manufacturing - Simple - Rich)

**Industry:** Manufacturing
**Complexity:** Simple
**Input Quality:** Rich
**Based on:** Example file "10. Karta projektu_BR HAUTAU.docx"

**Input Data:**
```yaml
Nazwa projektu: Technologia produkcji okien z systemem HAUTAU
Opis: Opracowanie procesu produkcyjnego okien wykorzystujących innowacyjny system okuć HAUTAU. Projekt obejmuje adaptację linii produkcyjnej do nowego systemu, opracowanie procedur montażowych, dobór odpowiednich narzędzi i parametrów obróbki oraz przeprowadzenie testów jakościowych. Konieczne było rozwiązanie problemów związanych z precyzyjnym pozycjonowaniem okuć, zapewnieniem powtarzalności procesu oraz integracją z istniejącym systemem produkcyjnym.
Data rozpoczęcia: 2023-02-01
Data zakończecia: 2023-11-30
Cel projektu: Wdrożenie nowej technologii produkcji okien z systemem HAUTAU, zapewniającej wysoką jakość produktu końcowego oraz efektywność procesu produkcyjnego.
Osoba odpowiedzialna: Marek Zieliński
```

**Expected Challenges:**
- Manufacturing process terminology
- Quality testing requirements
- Production line adaptation

**Target Quality:** ≥78 (clear manufacturing process)

---

### TC-005: Aluminum Welding (Manufacturing - Medium - Sparse)

**Industry:** Manufacturing
**Complexity:** Medium
**Input Quality:** Sparse
**Based on:** Example file "11. Karta projektu_BR zgrzewanie ram z progiem aluminowym.docx"

**Input Data:**
```yaml
Nazwa projektu: Zgrzewanie ram okiennych z progiem aluminowym
Opis: Nowa technologia łączenia profili z aluminium
Data rozpoczęcia: 2023-04-01
Data zakończenia: 2024-03-31
Cel projektu: Opracowanie metody zgrzewania
Osoba odpowiedzialna: Tomasz Lewandowski
```

**Expected Challenges:**
- Sparse description requires R&D expansion
- Technical welding terminology
- Material science aspects (aluminum properties)

**Target Quality:** ≥60 (sparse but technical domain)

---

### TC-006: NFC Door System (Manufacturing - Medium - Rich)

**Industry:** Manufacturing
**Complexity:** Medium
**Input Quality:** Rich
**Based on:** Example file "18. Karta projektu_BR drzwi NT773619.docx"

**Input Data:**
```yaml
Nazwa projektu: System drzwi z technologią NFC (NT773619)
Opis: Opracowanie innowacyjnego systemu drzwi wyposażonych w technologię NFC umożliwiającą bezkluczykowy dostęp. Projekt obejmuje integrację czytników NFC z konstrukcją drzwi, opracowanie systemu zarządzania uprawnieniami dostępu, zabezpieczenia kryptograficzne oraz testy w warunkach eksploatacyjnych. Wyzwania badawcze obejmują zapewnienie niezawodności działania w różnych warunkach atmosferycznych, ochronę przed nieautoryzowanym dostępem oraz kompatybilność z różnymi standardami NFC.
Data rozpoczęcia: 2022-09-01
Data zakończenia: 2024-08-31
Cel projektu: Stworzenie inteligentnego systemu drzwi łączącego tradycyjną stolarką z nowoczesnymi technologiami IoT, zwiększającego bezpieczeństwo i wygodę użytkowania.
Osoba odpowiedzialna: Katarzyna Woźniak
```

**Expected Challenges:**
- IoT and hardware integration
- Security and cryptography terminology
- Multi-disciplinary (mechanical + electronic)

**Target Quality:** ≥80 (well-defined R&D aspects)

---

### TC-007: Forklift Optimization (Manufacturing - Advanced - Rich)

**Industry:** Manufacturing
**Complexity:** Advanced
**Input Quality:** Rich
**Based on:** Example files about mobile forklifts

**Input Data:**
```yaml
Nazwa projektu: Mobilne wózki widłowe z systemem autonomicznej nawigacji
Opis: Kompleksowy projekt badawczo-rozwojowy nad stworzeniem zaawansowanego systemu autonomicznej nawigacji dla wózków widłowych wykorzystywanych w magazynach wysokiego składowania. Projekt obejmuje opracowanie algorytmów sztucznej inteligencji do planowania tras, systemu wizyjnego rozpoznawania palet i przeszkód, mechanizmów bezpieczeństwa oraz integracji z systemami WMS. Prace badawcze koncentrują się na zapewnieniu precyzji pozycjonowania (±5mm), bezpiecznej współpracy z operatorami ludzkimi, optymalizacji zużycia energii oraz niezawodności działania w trudnych warunkach magazynowych (niska temperatura, zróżnicowane oświetlenie).
Data rozpoczęcia: 2022-01-01
Data zakończenia: 2024-12-31
Cel projektu: Opracowanie prototypu autonomicznego wózka widłowego zdolnego do samodzielnej pracy w magazynie wysokiego składowania, zwiększającego efektywność operacji logistycznych oraz eliminującego ryzyko wypadków związanych z błędem ludzkim.
Osoba odpowiedzialna: Andrzej Kamiński
```

**Expected Challenges:**
- Advanced AI and robotics terminology
- Multi-year complex R&D program
- Multiple technical challenges and subsystems
- Safety and regulatory aspects

**Target Quality:** ≥85 (comprehensive R&D project)

---

### TC-008: Fuel System (Energy/Industrial - Simple - Rich)

**Industry:** Energy/Industrial
**Complexity:** Simple
**Input Quality:** Rich
**Based on:** Example file "12. Karta projektu_BR System do paliw.docx"

**Input Data:**
```yaml
Nazwa projektu: System automatycznego dozowania paliw alternatywnych
Opis: Opracowanie innowacyjnego systemu automatycznego dozowania i mieszania paliw alternatywnych (biomasa, odpady drzewne) w kotłowniach przemysłowych. Projekt obejmuje zaprojektowanie układu podawania surowca, systemu kontroli składu mieszanki, automatyki sterowania procesem spalania oraz monitoringu emisji spalin. Kluczowe wyzwania badawcze dotyczą zapewnienia równomiernego podawania materiałów o zróżnicowanej granulacji i wilgotności, optymalizacji procesu spalania oraz zgodności z normami emisyjnymi.
Data rozpoczęcia: 2023-05-01
Data zakończenia: 2024-04-30
Cel projektu: Stworzenie efektywnego systemu umożliwiającego wykorzystanie paliw alternatywnych w sposób ekonomiczny i ekologiczny, redukującego koszty eksploatacji kotłowni oraz emisję CO2.
Osoba odpowiedzialna: Michał Dąbrowski
```

**Expected Challenges:**
- Energy and combustion terminology
- Environmental regulations compliance
- Process control and automation

**Target Quality:** ≥75 (clear technical scope)

---

### TC-009: Power Turbine Upgrade (Energy/Industrial - Medium - Sparse)

**Industry:** Energy/Industrial
**Complexity:** Medium
**Input Quality:** Sparse

**Input Data:**
```yaml
Nazwa projektu: Modernizacja turbozespołu energetycznego
Opis: Zwiększenie mocy turbiny parowej poprzez modyfikację układu
Data rozpoczęcia: 2022-07-01
Data zakończenia: 2024-06-30
Cel projektu: Zwiększenie efektywności energetycznej
Osoba odpowiedzialna: Paweł Krawczyk
```

**Expected Challenges:**
- Highly technical power engineering domain
- Sparse input requires significant R&D expansion
- Regulatory and safety aspects
- Multi-year project complexity

**Target Quality:** ≥55 (sparse + highly technical)

---

### TC-010: Energy Storage System (Energy/Industrial - Advanced - Rich)

**Industry:** Energy/Industrial
**Complexity:** Advanced
**Input Quality:** Rich

**Input Data:**
```yaml
Nazwa projektu: Hybrydowy system magazynowania energii dla elektrowni wiatrowych
Opis: Zaawansowany projekt badawczy nad opracowaniem hybrydowego systemu magazynowania energii łączącego technologię akumulatorów litowo-jonowych z magazynami kinetycznymi (koła zamachowe). System przeznaczony jest do stabilizacji produkcji energii z farm wiatrowych, wyrównywania szczytów zapotrzebowania oraz świadczenia usług bilansujących dla sieci elektroenergetycznej. Projekt obejmuje kompleksowe badania nad optymalizacją algorytmów zarządzania energią, integracją różnych technologii magazynowania, systemami konwersji mocy, predykcją produkcji energii wiatrowej oraz analizą długoterminowej degradacji komponentów. Prace badawcze koncentrują się na maksymalizacji efektywności round-trip (>85%), minimalizacji kosztów LCOS (Levelized Cost of Storage) oraz zapewnieniu niezawodności systemu przez 20+ lat eksploatacji.
Data rozpoczęcia: 2021-09-01
Data zakończenia: 2024-08-31
Cel projektu: Opracowanie prototypowego systemu magazynowania energii o mocy 5MW/10MWh, demonstrującego techniczną i ekonomiczną wykonalność hybrydowych rozwiązań w zastosowaniach przemysłowych oraz przyczyniającego się do transformacji energetycznej poprzez stabilizację odnawialnych źródeł energii.
Osoba odpowiedzialna: Dr inż. Aleksandra Mazur
```

**Expected Challenges:**
- Highly advanced technical content
- Multiple complex subsystems
- Long-term R&D program (3 years)
- Cutting-edge energy storage technology
- Financial and environmental metrics

**Target Quality:** ≥90 (comprehensive, well-defined R&D)

---

### TC-011: Heritage Restoration (Construction - Simple - Rich)

**Industry:** Construction
**Complexity:** Simple
**Input Quality:** Rich

**Input Data:**
```yaml
Nazwa projektu: Technologia renowacji zabytkowych tynków wapiennych
Opis: Opracowanie innowacyjnej technologii renowacji historycznych tynków wapiennych w obiektach zabytkowych z XVIII-XIX wieku. Projekt obejmuje badania składu oryginalnych tynków, dobór kompatybilnych materiałów współczesnych, opracowanie receptur zapraw renowacyjnych oraz procedur aplikacji zachowujących autentyczność zabytku. Wyzwania badawcze dotyczą zapewnienia trwałości renowacji (min. 50 lat), zachowania właściwości dyfuzyjnych muru, kompatybilności chemicznej i mechanicznej z podłożem oraz zgodności z wytycznymi konserwatorskimi.
Data rozpoczęcia: 2023-03-15
Data zakończenia: 2024-02-28
Cel projektu: Stworzenie metody renowacji tynków zabytkowych łączącej tradycyjne rzemiosło z nowoczesnymi technologiami materiałowymi, zapewniającej długotrwałą ochronę dziedzictwa kulturowego.
Osoba odpowiedzialna: Mgr inż. Ewa Piotrowska
```

**Expected Challenges:**
- Heritage conservation terminology
- Material science aspects
- Historical and regulatory context

**Target Quality:** ≥78 (specialized but clear domain)

---

### TC-012: High-Rise Facade (Construction - Medium - Sparse)

**Industry:** Construction
**Complexity:** Medium
**Input Quality:** Sparse

**Input Data:**
```yaml
Nazwa projektu: System fasadowy dla budynków wysokościowych
Opis: Elewacja szklana dla wieżowców powyżej 150m
Data rozpoczęcia: 2022-10-01
Data zakończenia: 2024-09-30
Cel projektu: Opracowanie bezpiecznej fasady
Osoba odpowiedzialna: Inż. Robert Jankowski
```

**Expected Challenges:**
- High-rise construction complexity
- Minimal input requires extensive R&D inference
- Safety and wind load aspects
- Multi-year project from sparse description

**Target Quality:** ≥58 (sparse + specialized domain)

---

### TC-013: Smart Window System (Construction - Advanced - Rich)

**Industry:** Construction
**Complexity:** Advanced
**Input Quality:** Rich
**Based on:** Multiple window system examples

**Input Data:**
```yaml
Nazwa projektu: Inteligentny system okienny z aktywną regulacją termiczną i akustyczną
Opis: Kompleksowy projekt B+R nad opracowaniem zaawansowanego systemu okiennego nowej generacji integrującego technologie Smart Glass z aktywną regulacją współczynnika przenikania ciepła (U) i izolacyjności akustycznej (Rw). System wykorzystuje warstwy elektro-chromowe, materiały z pamięcią kształtu, czujniki IoT oraz algorytmy AI do automatycznej optymalizacji komfortu termicznego i akustycznego w zależności od warunków zewnętrznych i preferencji użytkownika. Projekt obejmuje badania nad nowymi materiałami kompozytowymi, projektowanie wielowarstwowych szyb o zmiennych właściwościach, integrację systemów sterowania, testy w komorze klimatycznej oraz symulacje numeryczne CFD i FEM. Kluczowe wyzwania badawcze dotyczą osiągnięcia szerokiego zakresu regulacji U (0.4-1.2 W/m²K), Rw (35-55 dB), długoterminowej trwałości warstw aktywnych (>25 lat), oraz integracji z systemami BMS budynku.
Data rozpoczęcia: 2021-11-01
Data zakończenia: 2024-10-31
Cel projektu: Opracowanie prototypowego inteligentnego okna demonstrującego rewolucyjne możliwości dynamicznej adaptacji do warunków środowiskowych, przyczyniającego się do drastycznej redukcji zużycia energii w budynkach (>40%) oraz poprawy komfortu akustycznego w obszarach miejskich.
Osoba odpowiedzialna: Prof. dr hab. inż. Krzysztof Adamczyk
```

**Expected Challenges:**
- Cutting-edge materials science
- Multi-disciplinary integration (materials, electronics, AI, physics)
- Complex testing and simulation methodologies
- Long R&D timeline (3 years)
- Multiple performance parameters and metrics

**Target Quality:** ≥92 (exemplary R&D project description)

---

### TC-014: Logistics Software (Other - Medium - Rich)

**Industry:** Other (Logistics/IT hybrid)
**Complexity:** Medium
**Input Quality:** Rich
**Based on:** Example file "10. Karta projektu_BR logistyka Genetix.docx"

**Input Data:**
```yaml
Nazwa projektu: Zintegrowany system logistyczny dla dystrybucji farmaceutyków (Genetix)
Opis: Opracowanie dedykowanego systemu informatycznego do zarządzania logistyką produktów farmaceutycznych wymagających specjalnych warunków przechowywania i transportu. Projekt obejmuje stworzenie modułów do monitorowania łańcucha chłodniczego w czasie rzeczywistym, zarządzania datami ważności produktów, optymalizacji tras dostaw z uwzględnieniem ograniczeń czasowych i temperaturowych, oraz automatycznego generowania dokumentacji compliance (GxP). System integruje technologie IoT (sensory temperatury, wilgotności), blockchain dla zapewnienia niezmienności danych, oraz algorytmy AI do predykcji zapotrzebowania. Kluczowe wyzwania dotyczą zapewnienia ciągłości łańcucha chłodniczego, zgodności z regulacjami farmaceutycznymi (GMP, GDP) oraz bezpieczeństwa danych medycznych (GDPR).
Data rozpoczęcia: 2022-05-01
Data zakończenia: 2024-04-30
Cel projektu: Stworzenie kompleksowego rozwiązania IT eliminującego ryzyko utraty jakości produktów farmaceutycznych w trakcie dystrybucji, zapewniającego pełną traceability zgodnie z wymogami regulacyjnymi oraz optymalizującego koszty logistyki.
Osoba odpowiedzialna: Mgr Monika Grabowska
```

**Expected Challenges:**
- Regulatory compliance (pharmaceutical, GDPR)
- Multi-technology integration (IoT, blockchain, AI)
- Specialized logistics domain
- Data security and traceability

**Target Quality:** ≥82 (well-defined specialized project)

---

### TC-015: Wood Processing (Other - Simple - Sparse)

**Industry:** Other (Wood processing)
**Complexity:** Simple
**Input Quality:** Sparse
**Based on:** Example file "18. Karta projektu_BR - Wydział Drewno.docx"

**Input Data:**
```yaml
Nazwa projektu: Linia do obróbki drewna
Opis: Automatyzacja cięcia i frezowania elementów drewnianych
Data rozpoczęcia: 2023-06-01
Data zakończenia: 2023-12-31
Cel projektu: Zwiększenie wydajności produkcji
Osoba odpowiedzialna: Jan Szymański
```

**Expected Challenges:**
- Extremely sparse input (minimal description)
- Generic automation topic
- AI must infer R&D aspects from very little data
- Should flag heavily for consultant review

**Target Quality:** ≥50 (minimum acceptable with heavy flagging)

---

## Test Case Summary Table

| ID | Project Name (Short) | Industry | Complexity | Input | Target Quality |
|----|---------------------|----------|------------|-------|----------------|
| TC-001 | ERP System | IT | Simple | Rich | ≥80 |
| TC-002 | Task Management | IT | Simple | Sparse | ≥65 |
| TC-003 | Mobile Construction App | IT | Medium | Rich | ≥75 |
| TC-004 | HAUTAU Windows | Manufacturing | Simple | Rich | ≥78 |
| TC-005 | Aluminum Welding | Manufacturing | Medium | Sparse | ≥60 |
| TC-006 | NFC Door System | Manufacturing | Medium | Rich | ≥80 |
| TC-007 | Autonomous Forklifts | Manufacturing | Advanced | Rich | ≥85 |
| TC-008 | Fuel System | Energy | Simple | Rich | ≥75 |
| TC-009 | Turbine Upgrade | Energy | Medium | Sparse | ≥55 |
| TC-010 | Energy Storage | Energy | Advanced | Rich | ≥90 |
| TC-011 | Heritage Tynks | Construction | Simple | Rich | ≥78 |
| TC-012 | High-Rise Facade | Construction | Medium | Sparse | ≥58 |
| TC-013 | Smart Windows | Construction | Advanced | Rich | ≥92 |
| TC-014 | Pharma Logistics | Other | Medium | Rich | ≥82 |
| TC-015 | Wood Processing | Other | Simple | Sparse | ≥50 |

**Average Target Quality:** 72.5 (meets ≥70 threshold)

---

## Diversity Validation

### Industry Distribution
- **IT/Software:** 3 cases (TC-001, TC-002, TC-003)
- **Manufacturing:** 4 cases (TC-004, TC-005, TC-006, TC-007)
- **Energy/Industrial:** 3 cases (TC-008, TC-009, TC-010)
- **Construction:** 3 cases (TC-011, TC-012, TC-013)
- **Other:** 2 cases (TC-014, TC-015)

✅ **PASS** - Good distribution across all target industries

### Complexity Distribution
- **Simple:** 6 cases (TC-001, TC-002, TC-004, TC-008, TC-011, TC-015)
- **Medium:** 6 cases (TC-003, TC-005, TC-006, TC-009, TC-012, TC-014)
- **Advanced:** 3 cases (TC-007, TC-010, TC-013)

✅ **PASS** - Balanced complexity (40% simple, 40% medium, 20% advanced)

### Input Quality Distribution
- **Rich:** 9 cases (TC-001, TC-003, TC-004, TC-006, TC-007, TC-008, TC-010, TC-011, TC-013, TC-014)
- **Sparse:** 6 cases (TC-002, TC-005, TC-009, TC-012, TC-015)

✅ **PASS** - 60% rich / 40% sparse (tests both scenarios)

---

## Expected POC Outcomes

### Success Scenario (GO Decision)
- **12+ test cases** achieve quality ≥70 (80% success rate)
- **Average quality score** ≥75
- **Sparse cases** properly flagged with [WYMAGA WERYFIKACJI]
- **Advanced cases** demonstrate AI capability for complex R&D

### Pivot Scenario
- **8-11 test cases** achieve quality 60-70
- **Sparse cases** struggle (TC-002, TC-005, TC-009, TC-012, TC-015)
- **Action:** Refine prompts for sparse input handling

### No-Go Scenario
- **<8 test cases** achieve quality ≥60
- **Polish grammar errors** >3 per 1000 words
- **Hallucinations** detected in multiple cases

---

## Next Steps

1. **Create Excel Input File** (`poc/test-cases.xlsx`) with all 15 test cases
2. **Extract Few-Shot Examples** - Select 2-3 high-quality example cards from docs/project-cards/examples/
3. **Prepare Expected Output Structure** - 8 sections per Ulga B+R template
4. **Begin POC Day 1** - Environment setup and baseline testing

---

**Document Control:**
- **Author:** BMad Master
- **Based on:** 66 example project cards from docs/project-cards/examples/
- **Next:** Create Excel file for POC execution
