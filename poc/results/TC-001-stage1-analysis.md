# ANALIZA PROJEKTU: System ERP zintegrowany z produkcją i logistyką

## Dane wejściowe projektu

**Nazwa projektu:** System ERP zintegrowany z produkcją i logistyką

**Opis projektu:** Opracowanie dedykowanego systemu ERP dostosowanego do specyfiki produkcji okien i drzwi, integrującego planowanie produkcji, zarządzanie magazynem, logistykę i fakturowanie. System uwzględnia niestandardowe procesy produkcyjne, zarządzanie wieloma liniami produkcyjnymi oraz specyficzne wymagania branży stolarki budowlanej. Projekt obejmuje analizę procesów biznesowych, projektowanie architektury systemu, implementację modułów oraz integrację z istniejącymi systemami CAD i maszynami produkcyjnymi.

**Okres realizacji:** 2023-01-15 do 2023-12-31

**Cel projektu:** Stworzenie zintegrowanego systemu informatycznego optymalizującego zarządzanie produkcją i logistyką w przedsiębiorstwie produkcyjnym zwiększającego efektywność operacyjną i eliminującego błędy wynikające z ręcznego wprowadzania danych.

**Osoba odpowiedzialna:** Jan Kowalski

---

## 1. Identyfikacja Aspektów B+R

Projekt dotyczy opracowania dedykowanego systemu informatycznego klasy ERP dostosowanego do wysoce specyficznych wymagań branży stolarki budowlanej, w szczególności produkcji okien i drzwi. Charakterystyka tej branży obejmuje produkcję jednostkową i małoseryjną, gdzie każde zamówienie wymaga indywidualnej konfiguracji produktu, co generuje złożone wyzwania w zakresie planowania produkcji, zarządzania wieloma liniami produkcyjnymi o różnych technologiach oraz synchronizacji przepływu materiałów.

Kluczowym aspektem badawczo-rozwojowym jest konieczność stworzenia niestandardowych algorytmów integracyjnych łączących różnorodne systemy informatyczne: systemy CAD wykorzystywane do projektowania stolarki, systemy sterowania maszynami CNC, tradycyjne moduły ERP (magazyn, logistyka, finanse) oraz systemy produkcyjne. W branży stolarki budowlanej nie istnieją gotowe rozwiązania ERP uwzględniające specyfikę produkcji jednostkowej z rozbudowaną konfiguracją produktów, zmiennością materiałów (różne profile, okucia, szyby), oraz koniecznością śledzenia każdego zamówienia od etapu projektowania przez produkcję aż do montażu.

Projekt wykracza poza rutynową implementację gotowego oprogramowania, wymagając prowadzenia systematycznych prac badawczych nad opracowaniem dedykowanej architektury systemu, algorytmów optymalizacyjnych, mechanizmów synchronizacji danych między heterogenicznymi systemami oraz metod walidacji poprawności przepływu informacji w czasie rzeczywistym.

## 2. Kwalifikacja według Ulga B+R

### a) Celowość (Purposefulness)

Projekt charakteryzuje się wyraźnie określonym celem badawczo-rozwojowym: stworzenie zintegrowanego systemu ERP specyficznie dostosowanego do nierutynowych procesów produkcji stolarki budowlanej. Cel ten obejmuje systematyczne, zaplanowane prace obejmujące: analizę procesów biznesowych specyficznych dla branży, projektowanie dedykowanej architektury systemu uwzględniającej wielość wariantów produktowych, opracowanie algorytmów integracji z systemami CAD i maszynami produkcyjnymi, oraz implementację modułów zarządzania produkcją wieloliniową. Celowość projektu przejawia się w dążeniu do rozwiązania konkretnego problemu technicznego - braku na rynku systemów ERP dostosowanych do specyfiki produkcji jednostkowej i małoseryjnej w stolarce budowlanej, gdzie każde zamówienie stanowi unikatowy projekt produkcyjny.

### b) Element Twórczy (Creative Element)

Projekt wymaga oryginalnego myślenia technicznego i opracowania nowatorskich rozwiązań w kilku kluczowych obszarach. Po pierwsze, konieczne jest stworzenie niestandardowych mechanizmów integracji między systemami CAD (projektowanie produktu) a modułami ERP (planowanie produkcji, magazyn), co wymaga opracowania dedykowanych konwerterów danych, walidatorów konfiguracji produktów oraz algorytmów przeliczania specyfikacji projektowych na plany materiałowe i produkcyjne. Po drugie, zarządzanie produkcją wieloliniową dla produktów o zmiennej konfiguracji wymaga opracowania algorytmów optymalizacyjnych harmonogramowania uwzględniających ograniczenia technologiczne poszczególnych linii, dostępność materiałów o specyficznych parametrach (wymiary, kolory, właściwości techniczne) oraz priorytety zamówień. Po trzecie, integracja z maszynami produkcyjnymi wymaga stworzenia interfejsów komunikacyjnych dostosowanych do różnorodnych protokołów przemysłowych oraz mechanizmów synchronizacji stanu produkcji w czasie rzeczywistym. Rozwiązanie tych problemów nie jest oczywiste i wymaga specjalistycznej wiedzy z zakresu inżynierii oprogramowania, informatyki przemysłowej oraz głębokiego zrozumienia procesów produkcyjnych stolarki budowlanej.

### c) Nowa Wiedza (New Knowledge)

Realizacja projektu prowadzi do wygenerowania nowej wiedzy technicznej na kilku poziomach. Organizacja nabędzie wiedzę dotyczącą projektowania architektury systemów ERP dostosowanych do produkcji jednostkowej w branżach o wysokim stopniu konfiguracji produktów, opracowania algorytmów integracji heterogenicznych systemów informatycznych (CAD, ERP, systemy maszynowe), oraz metod zarządzania danymi w środowisku wielosystemowym wymagającym zachowania spójności informacji w czasie rzeczywistym. Powstaną nowe metody techniczne dotyczące automatycznej konwersji danych projektowych (CAD) na specyfikacje materiałowe i produkcyjne, algorytmy optymalizacji planowania produkcji wieloliniowej uwzględniające specyfikę zmiennej konfiguracji produktów, oraz mechanizmy walidacji poprawności danych przepływających między zintegrowanymi systemami. Dodatkowo, projekt wygeneruje nową wiedzę dotyczącą identyfikacji i eliminacji błędów wynikających z ręcznego wprowadzania danych w procesach produkcyjnych opartych na zamówieniach jednostkowych. W rezultacie powstanie unikalne know-how dotyczące budowy systemów informatycznych dla branży stolarki budowlanej, które może stanowić podstawę do dalszego rozwoju i komercjalizacji rozwiązania.

## 3. Wyzwania Badawcze

1. **Integracja systemów CAD z modułami ERP:** Opracowanie mechanizmów automatycznej konwersji danych projektowych (geometria, specyfikacje materiałowe, parametry techniczne) generowanych w systemach CAD na struktury danych ERP (kartoteki materiałowe, receptury produkcyjne, listy komponentów) z zachowaniem integralności i spójności informacji.

2. **Algorytmy optymalizacji planowania produkcji wieloliniowej:** Stworzenie algorytmów harmonogramowania produkcji uwzględniających ograniczenia technologiczne poszczególnych linii produkcyjnych, zmienną konfigurację produktów (różne profile, wymiary, okucia, szyby), dostępność materiałów w magazynie, priorytety zamówień oraz minimalizację czasu przestojów i przezbrojeń linii.

3. **Zarządzanie danymi w środowisku heterogenicznym:** Zaprojektowanie architektury danych i mechanizmów synchronizacji zapewniających spójność informacji między wieloma systemami (CAD, ERP, systemy sterowania maszynami, moduły logistyczne) działającymi na różnych platformach technologicznych i wykorzystującymi różne formaty danych.

4. **Integracja z maszynami produkcyjnymi w czasie rzeczywistym:** Opracowanie interfejsów komunikacyjnych dostosowanych do różnorodnych protokołów przemysłowych używanych przez maszyny CNC, systemy sterowania liniami produkcyjnymi oraz urządzenia automatyki, zapewniających dwukierunkowy przepływ danych (zlecenia produkcyjne do maszyn, raportowanie stanu realizacji do ERP) z minimalnymi opóźnieniami.

5. **Walidacja poprawności konfiguracji produktów:** Stworzenie mechanizmów automatycznej walidacji konfig uracji zamówień pod kątem wykonalności technicznej, dostępności komponentów, zgodności z ograniczeniami technologicznymi oraz wykrywania konfliktów konfiguracyjnych na możliwie wczesnym etapie procesu (etap projektowania/wprowadzania zamówienia), aby zapobiec błędom w produkcji.

## 4. Kluczowe Obszary Innowacji

Nowatorski charakter projektu przejawia się przede wszystkim w kompleksowym podejściu do integracji różnorodnych systemów informatycznych specyficznych dla branży stolarki budowlanej w jeden spójny ekosystem cyfrowy. W przeciwieństwie do standardowych implementacji systemów ERP, które zazwyczaj obsługują produkcję seryjną lub masową z ograniczoną wariantywnością produktów, niniejsze rozwiązanie musi uwzględniać produkcję jednostkową, gdzie każde zamówienie stanowi unikalny projekt wymagający indywidualnej konfiguracji. Innowacyjność polega na opracowaniu mechanizmów pozwalających na płynne przekształcenie danych z etapu projektowania (systemy CAD) w specyfikacje produkcyjne i materiałowe (system ERP), a następnie automatyczne generowanie zleceń produkcyjnych dla maszyn uwzględniających szczegółowe parametry techniczne każdego elementu.

Dodatkowym obszarem innowacji jest opracowanie algorytmów dynamicznego planowania produkcji wieloliniowej dostosowanych do specyfiki branży. W stolarce budowlanej występuje duża zmienność materiałów (profile aluminiowe/PVC/drewniane, różne systemy okuć, typy szyb o zróżnicowanych właściwościach), co wymaga elastycznego zarządzania liniami produkcyjnymi o różnych możliwościach technologicznych oraz inteligentnego przydzielania zamówień do linii w oparciu o dostępność materiałów, priorytet zamówień i minimalizację czasu przestojów.

Istotnym ryzykiem technicznym jest zapewnienie niezawodności i spójności danych w środowisku wielosystemowym działającym w czasie rzeczywistym. Błędy w synchronizacji danych między systemami mogą prowadzić do produkcji wadliwych elementów, błędów w gospodarce magazynowej lub problemów logistycznych. Projekt wymaga opracowania mechanizmów transakcyjności, rollback w przypadku błędów oraz monitoringu integralności danych przepływających między systemami o różnych architekturach technologicznych.

## 5. Ocena Kompletności Danych

**Dane wystarczające:** TAK (z zastrzeżeniami)

**Uwagi:** Dostarczone dane zawierają wystarczającą charakterystykę projektu do opracowania karty B+R na poziomie ogólnym, obejmującą cele, zakres prac badawczo-rozwojowych oraz identyfikację kluczowych wyzwań technicznych. Opis projektu jasno wskazuje na systematyczne prace badawcze wykraczające poza rutynową implementację standardowego oprogramowania. Jednakże, w celu maksymalizacji wartości merytorycznej karty projektowej oraz wzmocnienia argumentacji dla celów Ulgi B+R, przydatne byłyby szczegółowe informacje dotyczące: konkretnych technologii i narzędzi programistycznych planowanych do zastosowania (języki programowania, framework), specyfikacji systemów CAD i maszyn produkcyjnych, z którymi następuje integracja, szacunkowej wielkości zespołu projektowego oraz podziału kompetencji, oraz ewentualnie planowanych kosztów kwalifikowanych i ich struktury. Brak tych informacji nie uniemożliwia jednak stworzenia pełnowartościowej karty projektu B+R.

**Sekcje wymagające weryfikacji:**

- **Sekcja 7: Koszty Kwalifikowane** - wymagać będzie użycia ogólnych sformułowań i przykładowych kategorii kosztowych bez podawania konkretnych kwot (zastosowanie formuł typu "koszty osobowe zespołu programistycznego", "koszty infrastruktury IT", "koszty licencji na narzędzia deweloperskie") oraz flag [WYMAGA WERYFIKACJI: szczegółowe koszty należy uzupełnić na podstawie dokumentacji księgowej].

- **Sekcja 8: Harmonogram** - harmonogram będzie musiał być przedstawiony w formie ogólnych faz projektu (analiza, projektowanie, implementacja, testy, wdrożenie) z przybliżonymi przedziałami czasowymi, z flagą [WYMAGA WERYFIKACJI: szczegółowy harmonogram prac należy doprecyzować w oparciu o dokumentację projektową].

---

**STATUS ANALIZY:** Projekt spełnia wszystkie trzy kryteria kwalifikacji Ulga B+R (celowość, element twórczy, nowa wiedza). Dane wystarczające do przejścia do Stage 2: Generowanie pełnej karty projektu B+R.
