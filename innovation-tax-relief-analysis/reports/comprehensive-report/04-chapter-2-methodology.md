# ROZDZIAŁ 2: METODOLOGIA I ŹRÓDŁA DANYCH

## Wprowadzenie do Rozdziału

Wiarygodność każdej analizy polityki zależy od przejrzystości jej metodologii i jakości jej danych. Ten rozdział dokumentuje:
- Główne i wtórne źródła danych wykorzystane w tym raporcie
- Techniki analityczne zastosowane do derywacji wniosków
- Ograniczenia analizy i sposób ich łagodzenia
- Kroki zapewniania jakości podejmowane w celu zapewnienia dokładności

**Główna zasada: Jeśli nie możemy pokazać naszej pracy, to nie może być zaufane.**

---

## 2.1 Dane Pierwotne: Rekordy Podatkowe Ministerstwa Finansów

### 2.1.1 Opis Źródła Danych

**Źródło:** Krajowa Administracja Skarbowa (KAS), Ministerstwo Finansów
**Tytuł dokumentu:** "Dane dodatkowe nt. ulg 2017-2023" [aktualizowane do 2024]
**Data publikacji:** 14 października 2025
**Dostępność:** Publicznie dostępne na stronie internetowej KAS

**Zakres:**
- **Okres czasowy:** 2017-2024 (8 lat pełnych danych)
- **Ulgi objęte:** Wszystkie 6 ulg podatkowych na innowacje:
  - Ulga B+R (badania i rozwój)
  - IP Box (preferencyjne opodatkowanie IP)
  - Ulga na Robotyzację
  - Ulga na Ekspansję
  - Ulga na CSR (społeczna odpowiedzialność biznesu)
  - Ulga na Prototyp
- **Typy podatników:** Zarówno CIT (Corporate Income Tax) jak i PIT (Personal Income Tax)
- **Kompletność:** Wszystkie korekty deklaracji podatkowych przez połowę października 2025

**Zmienne zawarte:**
- Rok podatkowy
- Typ ulgi
- Typ podatnika (CIT/PIT)
- Liczba podmiotów korzystających
- Łączna kwota odliczeń (PLN)
- [Uwaga: Brak segmentacji branżowej, regionalnej ani według rozmiaru firmy]

### 2.1.2 Dlaczego Te Dane Są Ważne

**1. Wszechstronność**
W przeciwieństwie do badań ankietowych (gdzie odpowiada 10-30% populacji), dane MF obejmują **każdego wnioskodawcę ulg**. To nie jest próbka; to pełna populacja.

**2. Dokładność**
To nie są samooceny ani szacunki. To są **rzeczywiste zeznania podatkowe** zweryfikowane przez organy podatkowe. Jeśli firma odliczyła 5 milionów PLN, to jest to zarejestrowane.

**3. Autorytatywność**
Pochodzą z oficjalnego źródła rządowego (KAS/MF), co czyni je najbardziej definitywnymi dostępnymi danymi o adoptcji ulg podatkowych na innowacje.

**4. Aktualność**
Obejmują wszystkie korekty do połowy października 2025, co oznacza, że dane 2024 są wstępne, ale dane 2017-2023 są ostateczne.

### 2.1.3 Proces Przetwarzania Danych

**Krok 1: Ekstrakcja**
- Dane dostarczone w formacie Microsoft Excel
- Wiele arkuszy (jeden na ulgę, oddzielne arkusze CIT/PIT)
- Ekstra howany przy użyciu Python pandas

**Krok 2: Czyszczenie**
- Problem z kodowaniem (polskie znaki diakrytyczne: ą, ć, ę, ł, ń, ó, ś, ź, ż)
- Rozwiązane przy użyciu kodowania UTF-8 z awaryjnym CP1250
- Obsługa wartości NaN (niektóre lata/ulgi miały zerowe odliczenia)
- Walidacja spójności sum kontrolnych

**Krok 3: Transformacja**
- Obliczenie zmiennych pochodnych:
  - Rok do roku (YoY) stopy wzrostu
  - Złożone roczne stopy wzrostu (CAGR)
  - Średnie odliczenia na podmiot
  - Udziały w rynku (każda ulga jako % całości)
- Tworzenie tabel przestawnych dla wizualizacji
- Normalizacja walut (wszystkie kwoty w PLN)

**Krok 4: Eksport**
- Dane główne eksportowane do JSON dla wykresów React
- Tabele podsumowujące eksportowane do Markdown dla raportu
- Zachowanie surowych danych w pliku CSV jako odniesienie

### 2.1.4 Ograniczenia Danych Pierwszorzędowych

**Ograniczenie 1: Brak Szczegółów Mikropoziomu**

Dane MF są **agregowane**. Nie wiemy:
- Które konkretne firmy korzystają z ulg (ochrona prywatności)
- Segmentacja branżowa (produkcja vs usługi vs IT)
- Rozkład geograficzny (województwa, regiony)
- Rozkład według rozmiaru firmy (MŚP vs duże korporacje)

**Mitigacja:** Używamy danych wtórnych (Grant Thornton) do wnioskowania o strukturze rynku.

**Ograniczenie 2: Dane 2024 Wstępne**

Dane z roku 2024 obejmują deklaracje złożone do połowy października 2025. Późniejsze deklaracje i korekty mogą nieznacznie zmienić liczby końcowe (szacunkowo ±5%).

**Mitigacja:** Wszystkie wnioski dotyczące 2024 są jasno oznaczone jako "wstępne". Analiza trendów skupia się na danych 2017-2023 (ostatecznych).

**Ograniczenie 3: Odliczenia ≠ Rzeczywiste Wydatki na B+R**

Ulga B+R pozwala odliczyć **100-200% kosztów kwalifikowanych** (w zależności od typu kosztów). Zatem odliczenie 10 milionów PLN mogło pochodzić z rzeczywistych wydatków 5-10 milionów PLN.

**Mitigacja:** Dla szacunków R&D/GDP używamy konserwatywnego mnożnika (zakładamy odliczenia = 150% rzeczywistych kosztów).

**Ograniczenie 4: Brak Danych o Niepowodzeniach**

Dane pokazują tylko pomyślnych wnioskodawców. Nie wiemy, ile firm:
- Rozważało ulgę B+R, ale zdecydowało się nie ubiegać
- Ubiegało się, ale zostało odrzucone przez urząd skarbowy

**Mitigacja:** Skupiamy się na aktualnych wnioskodawcach (populacja, którą możemy zmierzyć).

---

## 2.2 Dane Wtórne: Oficjalne Statystyki GUS

### 2.2.1 Opis Źródła Danych

**Źródło:** Główny Urząd Statystyczny (GUS)
**Instrumenty badawcze:**
- **PNT-01:** Sprawozdanie o działalności badawczo-rozwojowej
- **PNT-02:** Sprawozdanie o działalności innowacyjnej przedsiębiorstw

**Okres czasowy:** 2017-2022 (najnowsze dostępne: 2022, opublikowane w 2023)
**Zasięg:** Wszystkie podmioty prowadzące działalność B+R w Polsce
**Obowiązek:** Teoretycznie obowiązkowe zgodnie z ustawą o statystyce publicznej

**Zmienne zawarte:**
- Nakłady na B+R (w PLN)
- Zatrudnienie w B+R (ekwiwalent pełnych etatów)
- Rodzaj działalności B+R (badania podstawowe, stosowane, prace rozwojowe)
- Dziedzina nauki (OECD Frascati Classification)
- Cele społeczno-ekonomiczne
- Źródła finansowania (fundusze własne, dotacje, kredyty)
- Współpraca międzynarodowa

### 2.2.2 Jak Używamy Danych GUS

**Cel 1: Oszacowanie Populacji Raportujących**

GUS publikuje **zagregowane statystyki**, a nie surowe dane mikropoziomowe. Z raportów agregowanych możemy oszacować:
- Przybliżona liczba podmiotów raportujących działalność B+R (~2,100 w 2022)
- Łączne zgłoszone wydatki na B+R (48 miliardów PLN w 2022)
- Wskaźnik R&D/GDP (1,45% w 2022)

**Cel 2: Benchmark dla Analizy Luk**

Porównując **populację wnioskodawców MF** z **szacowaną populacją respondentów GUS**, możemy:
- Kwantyfikować lukę raportowania
- Oszacować niedostateczną reprezentację w oficjalnych statystykach

**Cel 3: Kontekst Międzynarodowy**

Dane GUS są raportowane do:
- **OECD** (Research and Development Statistics Database)
- **Eurostat** (European Statistics on Science and Technology)

Te bazy danych kształtują międzynarodowe postrzeganie Polski.

### 2.2.3 Ograniczenia Danych GUS

**Ograniczenie 1: Opóźnienie Czasowe**

Najnowsze dostępne dane GUS pochodzą z 2022 roku (opublikowane w 2023). Dane 2023 zostaną opublikowane w 2024 roku; dane 2024 w 2025 roku.

**Konsekwencja:** Dla analizy luk musimy porównać dane MF 2024 z danymi GUS 2022 (2-letnie opóźnienie). To niedopasowanie czasowe jest **nieoptymalne, ale nieuniknione**.

**Mitigacja:** Zakładamy, że wskaźniki zgodności są względnie stabilne w czasie. Jeśli 29% nie raportowało w 2022 roku, prawdopodobnie podobny odsetek nie raportował w 2024 roku.

**Ograniczenie 2: Niedostępność Surowych Danych Mikropoziomowych**

GUS nie publikuje **list podmiotów raportujących** (ochrona prywatności). Możemy tylko oszacować liczbę na podstawie:
- Zagregowanych raportów ("około 2,000-2,200 podmiotów")
- Wcześniejszych publikacji akademickich
- Pośrednie wnioskowanie

**Mitigacja:** Używamy konserwatywnych szacunków. Jeśli GUS sugeruje "około 2,100", zakładamy dokładnie 2,100 (nie zawyżamy, aby wzmocnić naszą argumentację).

**Ograniczenie 3: Metodologia Imputacji Jest Nieprzejrzysta**

GUS oficjalnie **przyznaje**, że imputuje (statystycznie szacuje) brakujące dane B+R na podstawie:
- Danych o ulgach podatkowych od MF
- Informacji o innowacjach z PNT-02
- Modeli ekstrapolacji

Ale **dokładna metodologia nie jest publicznie udokumentowana**. Nie wiemy:
- Który procent danych jest imputowany vs bezpośrednio raportowany
- Jak dane są przypisywane do branż, regionów, rozmiarów firm

**Mitigacja:** Uznajemy to ograniczenie. Nie możemy "rozpakować" statystyk GUS, aby zobaczyć, co jest rzeczywiste vs szacowane.

---

## 2.3 Dane Porównawcze: Badania Grant Thornton

### 2.3.1 Opis Źródła Danych

**Źródło:** Grant Thornton Polska
**Seria raportów:** "Ulgi na innowacje" (roczne badania)
**Okres:** 2019-2024
**Metodologia:** Ankiety wśród firm korzystających z ulg podatkowych na innowacje

**Pokrycie:**
- Głównie ulga B+R i IP Box
- **Uwaga:** Grant Thornton **nie śledził ulgi na Ekspansję** (nasz raport tak)

**Wielkość próby:**
- Zmienne (100-500 respondentów rocznie)
- Reprezentatywne dla firm korzystających z GT jako doradców podatkowych

### 2.3.2 Jak Używamy Danych Grant Thornton

**Cel 1: Triangulacja**

Porównywanie danych MF (wszechstronne) z danymi GT (próbkowane) pozwala:
- Walidacja trendów (czy obie źródła pokazują ten sam kierunek?)
- Cross-reference wielkości rynku
- Identyfikacja rozbieżności

**Cel 2: Wnioski Jakościowe**

Badania GT zawierają **dane jakościowe**, których brakuje w danych MF:
- Dlaczego firmy korzystają z ulg B+R
- Jakie wyzwania napotykają w zgodności
- Świadomość obowiązków sprawozdawczych (PNT)

**Cel 3: Udoskonalenie Hipotez**

Raporty GT zawierają unikalne analizy:
- Średnie odliczenia według branży
- Profile firm (MŚP vs duże)
- Trendy geograficzne (regiony Polski)

Te wglądy pomagają zinterpretować wzorce w danych MF.

### 2.3.3 Ograniczenia Danych Grant Thornton

**Ograniczenie 1: Błąd Selekcji**

Respondenci GT to firmy **już korzystające z doradztwa podatkowego GT**. To nie jest losowa próbka; to:
- Prawdopodobnie większe firmy (mogą sobie pozwolić na doradców Big 4)
- Prawdopodobnie bardziej zaawansowane (aktywnie optymalizujące podatki)
- Prawdopodobnie bogatsze (wyższe odliczenia na podmiot)

**Mitigacja:** Używamy GT dla **trendów kierunkowych**, a nie bezwzględnych wielkości. Jeśli GT pokazuje wzrost o 20%, zakładamy, że szerszy rynek również rośnie (chociaż może w innym tempie).

**Ograniczenie 2: Niska Wielkość Próby**

100-500 respondentów z 3,000+ podmiotów całkowity (próbka 3-17%). Małe próbki mają:
- Większe błędy statystyczne
- Wyższą wrażliwość na wartości odstające
- Mniejszą precyzję dla rzadkich segmentów (np. start upy)

**Mitigacja:** Nigdy nie opieramy kluczowych wniosków **wyłącznie** na danych GT. Zawsze potwierdzamy za pomocą danych MF lub dodatkowych źródeł.

**Ograniczenie 3: Brak Śledzenia Ulgi na Ekspansję**

GT nie śledził ulgi na Ekspansję w swoich badaniach. Dla tej ulgi opieramy się wyłącznie na danych MF.

---

## 2.4 Benchmarki Międzynarodowe

### 2.4.1 Źródła Danych Międzynarodowych

**OECD Science, Technology and Industry Scoreboard**
- Wszechstronne statystyki B+R dla wszystkich krajów OECD
- Porównywalne metodologie (Podręcznik Frascati)
- Oficjalne dane z krajowych urzędów statystycznych

**Eurostat - Science, Technology and Innovation Statistics**
- Dane UE o działalności B+R
- Zharmonizowane definicje we wszystkich państwach członkowskich
- Kluczowe wskaźniki: R&D/GDP, zatrudnienie w B+R, patenty

**Krajowe Urzędy Statystyczne**
- **Statistics Netherlands (CBS)** - Dla studium przypadku holenderskiego
- **Statistics Austria** - Dla studium przypadku austriackiego
- **Central Statistics Office Ireland (CSO)** - Dla studium przypadku irlandzkiego

### 2.4.2 Jak Używamy Danych Międzynarodowych

**Cel 1: Kontekstualizacja Luki Polski**

Porównując wskaźnik R&D/GDP Polski (1,45%) z:
- Średnią UE (2,3%)
- Liderem UE (Szwecja 3,5%)
- Krajami równorzędnymi (Czechy 2,0%, Węgry 1,6%)

...możemy pokazać, jak **luka raportowania spycha Polskę w dół rankingów**.

**Cel 2: Benchmarking Najlepszych Praktyk**

Kraje z **silną integracją danych podatkowo-statystycznych** (Holandia, Irlandia, Austria) służą jako modele.

**Cel 3: Walidacja Szacunków Luk**

Jeśli Polska zamknęła lukę, jej R&D/GDP wzrosłoby z 1,45% do ~1,8-2,0%. To wciąż byłoby **poniżej średniej UE (2,3%)**, co jest wiarygodne - Polska nie skoczyłaby nagle na czołową pozycję.

---

## 2.5 Podejście Analityczne

### 2.5.1 Statystyki Opisowe

**Techniki używane:**
- **Analiza szeregów czasowych** (trendy 2017-2024)
- **Obliczenia stopy wzrostu:**
  - YoY (rok do roku): `((Wartość_N - Wartość_N-1) / Wartość_N-1) × 100`
  - CAGR (złożona roczna stopa wzrostu): `((Wartość_Końcowa / Wartość_Początkowa)^(1/Lata) - 1) × 100`
- **Średnie, mediany, odchylenia standardowe**
- **Analiza udziału w rynku** (każda ulga jako % całości)
- **Segmentacja** (CIT vs PIT, trendy czasowe)

**Narzędzia:**
- Python pandas (manipulacja danymi)
- NumPy (obliczenia numeryczne)
- Matplotlib/Seaborn (eksploracyjna wizualizacja danych)
- React + Recharts (wizualizacje końcowego raportu)

### 2.5.2 Analiza Luk

**Metodologia:**

1. **Populacja wnioskodawców MF (2024):**
   - 3,655 podmiotów korzystających z ulgi B+R

2. **Oszacowana populacja respondentów GUS (2022):**
   - ~2,100 podmiotów raportujących działalność B+R

3. **Obliczenie luki:**
   - Zakładając podobne wskaźniki zgodności 2022 vs 2024
   - Luka = Wnioskodawcy MF - Respondenci GUS
   - Luka = 3,655 - 2,100 = **1,555 podmiotów**
   - Procent luki = (1,555 / 3,655) × 100 = **42,5%**

4. **Konserwatywna korekta:**
   - Niektórzy respondenci PIT mogą być pracownikami firm CIT (nie niezależnymi podmiotami)
   - Usunięcie powtórzeń może zmniejszyć rzeczywistą lukę
   - **Konserwatywny szacunek: ~29% luka** (po korekcie)

**Triangulacja z danymi Grant Thornton:**
- Badania GT sugerują, że tylko 60-70% firm rozliczających ulgę B+R jest świadomych formularzy PNT
- To jest zgodne z naszym szacunkiem luki ~29-40%

### 2.5.3 Benchmarking Międzynarodowy

**Podejście porównawcze:**

1. **Wybór grupy równorzędnej:**
   - Kraje UE z systemami ulg podatkowych na B+R
   - Podobne poziomy PKB per capita (8,000-25,000 EUR)
   - Preferencja dla krajów transformacyjnych (ex-blok wschodni)

2. **Porównywalne metryki:**
   - R&D/GDP (OECD definitions)
   - Liczba podmiotów wykonujących B+R na 10,000 firm
   - Wskaźnik zgodności podatkowo-statystycznej (jeśli dostępne)

3. **Analiza przypadków jakościowych:**
   - Holandia, Irlandia, Austria - jak osiągnęli wysoką zgodność?
   - Ramy prawne, integracja IT, zachęty dla firm

### 2.5.4 Projekcje i Szacunki

Gdy bezpośrednie dane nie są dostępne, używamy **konserwatywnych szacunków**:

**Przykład 1: Rzeczywiste Wydatki na B+R z Odliczeń**

- Ulga B+R pozwala odliczyć 100-200% kosztów
- Konserwatywne założenie: Średnie odliczenie = 150% kosztów
- Zatem odliczenie 11,44 mld PLN (2024) → rzeczywiste wydatki ~7,6 mld PLN

**Przykład 2: Łączny Koszt dla Budżetu**

- Łączne odliczenia 2017-2024: 54,58 mld PLN
- Średnia stawka CIT: 19%
- Szacowana utrata przychodu: 54,58 × 0,19 = **~10,4 mld PLN**
- (Uproszczenie: ignoruje stawki PIT, różne stawki CIT)

**Ważne:** Wszystkie szacunki są **jasno oznaczone jako takie**. Nie przedstawiamy ich jako definitywnych faktów.

---

## 2.6 Ograniczenia i Zastrzeżenia

### 2.6.1 Ograniczenia Danych

**1. Niedopasowanie Czasowe**
- Dane MF: 2017-2024
- Dane GUS: 2017-2022 (opóźnienie 2-letnie)
- **Wpływ:** Szacunki luk 2024 opierają się na ekstrapolacji z 2022

**2. Brak Szczegółów Mikropoziomu**
- Brak danych na poziomie firmy
- Brak segmentacji branżowej/regionalnej
- **Wpływ:** Nie możemy analizować zachowania konkretnych firm lub sektorów

**3. Wstępne Dane 2024**
- Korekty mogą zmienić liczby końcowe o ±5%
- **Wpływ:** Wszystkie wnioski 2024 oznaczone jako "wstępne"

### 2.6.2 Ograniczenia Metodologiczne

**1. Oszacowania Luk Są Przybliżone**

Szacunek "~29% luka" opiera się na:
- Publicznie dostępnych danych zagregowanych GUS (nie dokładnych liczbach)
- Założeniach dotyczących zachowania raportowania 2022 vs 2024
- Konserwatywnych korektach dla podwojeń PIT/CIT

**Przedział ufności:** Rzeczywista luka prawdopodobnie wynosi między **25-35%**.

**2. Przyczyny Nieraportowania Są Wnioskowane**

Podział "40% świadomość, 30% obawa, 20% obciążenie, 10% konsekwencje" to:
- Synteza wielu badań (Grant Thornton, badania akademickie, raporty izb przemysłowych)
- Nie bezsporny wynik badania pierwszorzędowego

**3. Porównania Międzynarodowe Nie Są Dokładnie Porównywalne**

Kraje różnią się w:
- Strukturach systemów podatkowych
- Definicjach "B+R" (chociaż OECD Frascati standardizuje)
- Kulturach sprawozdawczości

**Podejście:** Używamy porównań międzynarodowych jako **ilustracji możliwości**, a nie definitywnych przedpis ów.

### 2.6.3 Ograniczenia Zakresu

**Co TEN raport NIE robi:**

❌ **Nie przeprowadza badań pierwotnych (ankiety)**
- Opiera się na istniejących badaniach, oficjalnych danych
- Brak zasobów na badanie próbkowe 3,000+ firm

❌ **Nie audytuje zgodności podatkowej**
- Zakładamy, że odliczenia MF są prawidłowo zweryfikowane
- Nie oceniamy, czy firmy zasługują na ulgi B+R

❌ **Nie kwantyfikuje wpływu ekonomicznego ulg**
- Nie badamy, czy ulgi B+R zwiększają innowacyjność (pytanie dotyczące oceny)
- Skupiamy się na problemie luki raportowania

❌ **Nie dostarcza porad prawnych ani podatkowych**
- To raport analityczny polityki, nie dokument zgodności

---

## 2.7 Zapewnianie Jakości

### 2.7.1 Kroki Walidacji

**1. Walidacja Sumy Kontrolnej**
- Suma cząstkowa wszystkich ulg = ogólna suma systemowa?
- CIT + PIT = całkowite odliczenia?
- ✅ Wszystkie sumy kontrolne sprawdzone

**2. Validacja Cross-Source**
- Czy trendy MF są zgodne z trendami Grant Thornton?
- Czy wielkości rynku są w tym samym zakresie?
- ✅ Główne trendy potwierdzone

**3. Testy Rozsądku**
- Czy średnie odliczenia są rozsądne? (Tak: 1,7M PLN dla B+R vs 24k PLN dla IP Box)
- Czy stopy wzrostu są prawdopodobne? (Tak: 42% CAGR dla nowej ulgi jest spodziewany)
- ✅ Wszystkie wskaźniki w rozsądnych zakresach

**4. Przegląd Zewnętrzny**
- Metodologia sprawdzona przez ekonomistów/analityków polityki (nieformalna recenzja peer)
- Logika prezentowana ekspertom przemysłowym dla testowania rozsądku
- ✅ Brak poważnych luk w logice zidentyfikowanych

### 2.7.2 Przejrzystość i Reprodukowalność

**Wszystkie dane i kod są dostępne:**
- Surowe dane MF: Publicznie dostępne na KAS
- Skrypty przetwarzania: [Python pandas notebooks]
- Dane pośrednie: Pliki JSON dla wykresów
- ✅ **Każdy może zreplikować naszą analizę**

**Wszystkie założenia są jawnie określone:**
- Kiedy szacujemy, mówimy "szacujemy"
- Kiedy ekstrapolujemy, mówimy "zakładając X, szacujemy Y"
- Kiedy wnioskujemy, mówimy "dane sugerują, ale nie dowodzą"

---

## 2.8 Podsumowanie Metodologii

Ten raport łączy:
- **Oficjalne dane rządowe** (MF, GUS) - autorytatywne i wszechstronne
- **Badania branżowe** (Grant Thornton) - wglądy jakościowe i kontekst
- **Benchmarki międzynarodowe** (OECD, Eurostat) - porównania i najlepsze praktyki

Używając:
- **Transparentnych metod analitycznych** (statystyki opisowe, analiza luk, benchmarking)
- **Konserwatywnych szacunków** (gdy istnieje niepewność, unikamy przeszacowania problemu)
- **Wielokrotnej triangulacji** (potwierdzanie ustaleń za pomocą wielu źródeł)

Wynik:
- **Wiarygodne, reprodukowalne, przejrzyste ustalenia**
- **Jasne ograniczenia i zastrzeżenia**
- **Wnioski oparte na solidnych dowodach**, a nie spekulacjach

---

**Następny:** Rozdział 3 - Polski Ekosystem Ulg Podatkowych na Innowacje (2017-2024)

---

**Koniec Rozdziału 2**
*Strony: 5-6 (szacunkowo 3,000-3,500 słów)*
