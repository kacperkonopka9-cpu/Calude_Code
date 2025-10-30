# Instrukcja Publikacji Raportu na cyber-folks.pl

## Spis Treści
1. [Przegląd](#przegląd)
2. [Krok 1: Logowanie do Panelu](#krok-1-logowanie-do-panelu)
3. [Krok 2: Utworzenie Katalogu](#krok-2-utworzenie-katalogu)
4. [Krok 3: Upload Plików](#krok-3-upload-plików)
5. [Krok 4: Weryfikacja](#krok-4-weryfikacja)
6. [Rozwiązywanie Problemów](#rozwiązywanie-problemów)
7. [Przyszłe Aktualizacje](#przyszłe-aktualizacje)

---

## Przegląd

Twój raport jest gotowy do publikacji jako strona HTML na serwerze cyber-folks.pl.

**Struktura URL:**
- Główna strona raportu: `https://inovgroup.pl/raport-ulgi-br/`
- Lub: `https://www.inovgroup.pl/raport-ulgi-br/`

**Co musisz wgrać:**
- Folder: `website-upload` (zawiera wszystkie pliki HTML, CSS i obrazy)

---

## Krok 1: Logowanie do Panelu

### 1.1 Otwórz Panel Kontrolny cyber-folks.pl

1. Otwórz przeglądarkę (Chrome, Firefox, Edge)
2. Przejdź do: **https://panel.cyber-folks.pl** (lub adres podany przez hosting)
3. Zaloguj się używając:
   - **Login:** Twój login do panelu (zwykle email lub nazwa użytkownika)
   - **Hasło:** Twoje hasło do panelu

**Gdzie znaleźć dane logowania:**
- Email powitalny od cyber-folks.pl po zakupie hostingu
- Może być w zakładce "Konta hostingowe" lub podobnej

---

## Krok 2: Utworzenie Katalogu

### 2.1 Znajdź Menedżer Plików (File Manager)

W panelu kontrolnym znajdź jedną z tych opcji:
- **"Menedżer plików"**
- **"File Manager"**
- **"Pliki"**
- Lub szukaj ikony folderu 📁

### 2.2 Przejdź do Katalogu Głównego Twojej Strony

Typowe lokalizacje:
- `/public_html/` (najczęściej)
- `/httpdocs/`
- `/www/`
- Lub katalog o nazwie Twojej domeny: `/inovgroup.pl/`

**Jak sprawdzić:**
- Jeśli widzisz pliki WordPress (wp-admin, wp-content, wp-includes), jesteś we właściwym miejscu!

### 2.3 Utwórz Nowy Katalog

1. Kliknij **"Nowy folder"** lub **"Create Folder"** lub **"+"**
2. Nazwa folderu: `raport-ulgi-br`
3. Kliknij **"Utwórz"** / **"Create"**

**Ważne:** Użyj dokładnie tej nazwy (małe litery, myślniki zamiast spacji)

---

## Krok 3: Upload Plików

### 3.1 Przygotuj Pliki

Na swoim komputerze:
1. Przejdź do folderu:
   ```
   innovation-tax-relief-analysis/reports/comprehensive-report/website-upload/
   ```
2. Zaznacz **WSZYSTKIE** pliki i foldery w środku:
   - Wszystkie pliki .html (14 plików)
   - Plik report-styles.css
   - Folder "images" z zawartością

**Opcja A - Zaznacz wszystko:**
- Windows: `Ctrl + A`
- Mac: `Cmd + A`

### 3.2 Wgraj Pliki do Serwera

Masz **dwie metody** - wybierz łatwiejszą:

#### METODA 1: Upload przez Przeglądarkę (Łatwiejsza)

1. W menedżerze plików **otwórz** folder `raport-ulgi-br`
2. Kliknij **"Upload"** lub **"Wgraj pliki"** lub ikonę strzałki ⬆️
3. Przeciągnij i upuść wszystkie pliki z `website-upload/` na stronę
   - LUB kliknij **"Wybierz pliki"** i zaznacz wszystkie
4. Poczekaj aż upload się zakończy (może zająć 1-3 minuty)
5. **Ważne:** Upewnij się, że folder "images" został wgrany z zawartością

#### METODA 2: Upload przez ZIP (Szybsza dla wielu plików)

1. Na swoim komputerze:
   - Zaznacz wszystkie pliki w `website-upload/`
   - Kliknij prawym → **"Skompresuj do archiwum ZIP"** / **"Compress"**
   - Nazwij: `raport-upload.zip`

2. W menedżerze plików:
   - Otwórz folder `raport-ulgi-br`
   - Kliknij **"Upload"** i wgraj plik `raport-upload.zip`
   - Po zakończeniu uploadu kliknij prawym na `raport-upload.zip`
   - Wybierz **"Rozpakuj"** / **"Extract"** / **"Uncompress"**
   - Po rozpakowaniu możesz usunąć plik .zip

---

## Krok 4: Weryfikacja

### 4.1 Sprawdź Strukturę Plików

W folderze `raport-ulgi-br/` powinieneś widzieć:

```
raport-ulgi-br/
├── index.html                          ← Strona główna raportu
├── report-styles.css                   ← Style CSS
├── 00-cover.html
├── 00-press-summary.html
├── 01-executive-summary-PL.html
├── 02-executive-summary-EN.html
├── 03-chapter-1-introduction.html
├── 04-chapter-2-methodology.html
├── 05-chapter-3-ecosystem-analysis.html
├── 06-chapter-4-statistical-gap.html
├── 07-chapter-5-international-comparisons.html
├── 08-chapter-6-solutions-analysis.html
├── 09-chapter-7-implications-recommendations.html
├── 10-chapter-8-conclusions.html
├── 11-appendices.html
└── images/
    ├── innovation index map.png
    └── innovation index poland.png
```

**Jeśli czegoś brakuje:** Powtórz upload dla brakujących plików

### 4.2 Testuj Stronę w Przeglądarce

1. Otwórz przeglądarkę
2. Wpisz: `https://inovgroup.pl/raport-ulgi-br/`
3. Powinieneś zobaczyć stronę tytułową raportu z:
   - Nagłówkiem: **"Analiza Ulg Proinnowacyjnych w Polsce: Luka raportowa"**
   - Złotym tłem nagłówka (kolor Inov)
   - Listą rozdziałów do kliknięcia

### 4.3 Testuj Nawigację

Kliknij na kilka rozdziałów:
- ✅ Strona powinna się załadować
- ✅ Powinieneś widzieć sformatowany tekst (nie kod HTML)
- ✅ Tabele powinny być czytelne
- ✅ Kolory Inov (złoty, granatowy) powinny być widoczne

### 4.4 Testuj na Telefonie

Otwórz `https://inovgroup.pl/raport-ulgi-br/` na telefonie:
- ✅ Strona powinna się dostosować do małego ekranu
- ✅ Tekst powinien być czytelny bez przewijania w poziomie

---

## Rozwiązywanie Problemów

### Problem 1: "404 Not Found" lub "Strona nie istnieje"

**Przyczyna:** Nieprawidłowa struktura folderów

**Rozwiązanie:**
1. Sprawdź czy folder nazywa się **dokładnie** `raport-ulgi-br` (nie `raport_ulgi_br` ani `Raport-Ulgi-Br`)
2. Sprawdź czy jest w katalogu głównym (obok folderów WordPress)
3. Sprawdź czy plik `index.html` jest bezpośrednio w `raport-ulgi-br/` (NIE w podfolderze!)

### Problem 2: Strona pokazuje kod HTML zamiast sformatowanego tekstu

**Przyczyna:** Nieprawidłowa konfiguracja serwera dla plików .html

**Rozwiązanie:**
1. Upewnij się, że pliki mają rozszerzenie `.html` (nie `.txt`)
2. Sprawdź czy w adresie URL wpisujesz pełną ścieżkę z `index.html`:
   - Spróbuj: `https://inovgroup.pl/raport-ulgi-br/index.html`

### Problem 3: Brak stylowania (strona jest czarno-biała, bez kolorów Inov)

**Przyczyna:** Plik CSS nie został wgrany lub jest w złej lokalizacji

**Rozwiązanie:**
1. Sprawdź czy plik `report-styles.css` jest w tym samym folderze co `index.html`
2. Nazwa musi być **dokładnie** `report-styles.css` (z myślnikiem, nie spacją)
3. Odśwież przeglądarkę: `Ctrl+F5` (Windows) lub `Cmd+Shift+R` (Mac)

### Problem 4: Obrazy nie wyświetlają się

**Przyczyna:** Folder images nie został wgrany lub jest pusty

**Rozwiązanie:**
1. Sprawdź czy istnieje folder `images/` wewnątrz `raport-ulgi-br/`
2. Sprawdź czy w środku są pliki .png
3. Sprawdź czy nazwy plików obrazów są DOKŁADNIE takie jak w oryginalnym folderze (spacje, wielkie/małe litery)

### Problem 5: Nie mogę znaleźć Menedżera Plików w panelu

**Rozwiązanie:**
1. Szukaj w menu: "Hosting", "Strony WWW", "Zarządzanie plikami"
2. Jeśli używasz cPanel: Szukaj ikony "File Manager"
3. Skontaktuj się z helpdesk cyber-folks.pl: support@cyber-folks.pl
   - Zapytaj: "Jak dostać się do menedżera plików dla mojej strony inovgroup.pl?"

---

## Przyszłe Aktualizacje

### Gdy Edytujesz Raport (Markdown)

1. Edytuj pliki `.md` (markdown) w swoim projekcie
2. Uruchom skrypt generowania HTML:
   ```bash
   ./generate-html.sh
   ```
3. Wgraj TYLKO zmienione pliki .html z `html-output/` do serwera

**Przykład - edycja Rozdziału 4:**
- Edytujesz: `06-chapter-4-statistical-gap.md`
- Generujesz HTML: `./generate-html.sh`
- Wgrywasz tylko: `06-chapter-4-statistical-gap.html` do folderu `raport-ulgi-br/` na serwerze

### Wgranie Logo Inov (Opcjonalne)

Jeśli masz logo Inov:
1. Nazwij je: `Inov logo (1800 x 1000 px) (10).png` LUB zmień nazwę w `index.html`
2. Wgraj do folderu `images/` na serwerze
3. Odśwież stronę - logo pojawi się na górze

---

## Wsparcie

Jeśli masz problemy:

**1. Techniczne problemy z hostingiem:**
- Email: support@cyber-folks.pl
- Telefon: (znajdź w panelu lub na stronie cyber-folks.pl)

**2. Problemy z raportem (HTML/CSS):**
- Opisz problem szczegółowo
- Zrób screenshot pokazujący błąd
- Podaj URL strony z problemem

---

## Podsumowanie Szybkie

**3-minutowa instrukcja:**

1. **Zaloguj się** → panel.cyber-folks.pl
2. **Menedżer plików** → otwórz `/public_html/`
3. **Nowy folder** → nazwa: `raport-ulgi-br`
4. **Upload** → przeciągnij wszystkie pliki z `website-upload/`
5. **Testuj** → otwórz `https://inovgroup.pl/raport-ulgi-br/`

**Gotowe!** ✅

---

**Tworzenie raportu:** Inov Research & Development
**Data:** Październik 2025
**Kontakt:** kkonopka@inovgroup.pl
