# Automatyczny Upload Raportu przez FTP

## Spis Treści
1. [Przegląd](#przegląd)
2. [Krok 1: Pobierz Dane FTP](#krok-1-pobierz-dane-ftp)
3. [Krok 2: Konfiguracja Skryptu](#krok-2-konfiguracja-skryptu)
4. [Krok 3: Automatyczny Upload](#krok-3-automatyczny-upload)
5. [Rozwiązywanie Problemów](#rozwiązywanie-problemów)
6. [Bezpieczeństwo](#bezpieczeństwo)

---

## Przegląd

Ten przewodnik pokazuje jak automatycznie wgrać raport na serwer **bez używania przeglądarki**.

**Co robi skrypt:**
- Łączy się z serwerem FTP cyber-folks.pl
- Automatycznie wgrywa wszystkie pliki z `website-upload/`
- Tworzy potrzebne katalogi
- Pokazuje postęp uploadu

**Jeden raz:**
```bash
./upload-to-server.sh
```

---

## Krok 1: Pobierz Dane FTP

### 1.1 Zaloguj się do Panelu cyber-folks

1. Otwórz: **https://panel.cyber-folks.pl**
2. Zaloguj się swoimi danymi

### 1.2 Znajdź Dane FTP

**Opcja A: Sekcja "Konta FTP"**

1. W menu znajdź: **"Konta FTP"** lub **"FTP Accounts"** lub **"Hosting"**
2. Powinieneś zobaczyć tabelę z kontami FTP
3. Zapisz następujące informacje:

```
Host FTP: ftp.cyber-folks.pl (lub ftp.inovgroup.pl)
Użytkownik: twoj_login
Hasło: [kliknij "Pokaż" lub "Change Password" aby zobaczyć]
Port: 21
Katalog główny: /public_html/ (lub /httpdocs/)
```

**Opcja B: Email Powitalny**

1. Szukaj emaila od cyber-folks.pl z tytułem: "Dane dostępowe do hostingu"
2. W emailu powinny być dane FTP

**Opcja C: Utwórz Nowe Konto FTP (jeśli potrzeba)**

1. Kliknij **"Dodaj konto FTP"** / **"Add FTP Account"**
2. Nazwa użytkownika: `inovgroup_upload` (lub dowolna)
3. Hasło: Wygeneruj silne hasło
4. Katalog domowy: `/public_html/`
5. Zapisz dane!

### 1.3 Sprawdź Strukturę Katalogów

**Ważne:** Musisz wiedzieć gdzie znajduje się katalog główny Twojej strony.

Typowe struktury:

**Struktura A (najczęstsza):**
```
/
├── public_html/              ← Katalog główny strony
│   ├── wp-admin/             ← WordPress
│   ├── wp-content/
│   └── raport-ulgi-br/       ← Tu wgrywamy raport
```

**Struktura B:**
```
/
├── httpdocs/                 ← Katalog główny strony
│   ├── wp-admin/
│   └── raport-ulgi-br/
```

**Struktura C:**
```
/
├── domains/
│   └── inovgroup.pl/
│       ├── public_html/      ← Katalog główny strony
│       └── raport-ulgi-br/
```

**Jak sprawdzić:**
Zaloguj się przez File Manager i zobacz gdzie znajdują się pliki WordPress.

---

## Krok 2: Konfiguracja Skryptu

### 2.1 Skopiuj Szablon Konfiguracji

W terminalu (w folderze raportu):

```bash
cd innovation-tax-relief-analysis/reports/comprehensive-report/
cp .ftp-credentials.template .ftp-credentials
```

### 2.2 Edytuj Plik z Danymi FTP

**Metoda A: Nano (w terminalu)**
```bash
nano .ftp-credentials
```

**Metoda B: Visual Studio Code**
```bash
code .ftp-credentials
```

**Metoda C: Dowolny edytor tekstu**
- Otwórz plik `.ftp-credentials` w edytorze

### 2.3 Wypełnij Dane

Zamień wartości na swoje rzeczywiste dane:

```bash
# FTP Server Details
FTP_HOST="ftp.cyber-folks.pl"          # Lub ftp.inovgroup.pl
FTP_PORT="21"
FTP_USER="twoj_login_ftp"              # ZMIEŃ NA SWÓJ!
FTP_PASS="twoje_haslo_ftp"             # ZMIEŃ NA SWOJE!

# Remote path - WAŻNE!
REMOTE_PATH="/public_html/raport-ulgi-br/"
```

**Uwaga do REMOTE_PATH:**
- Sprawdź gdzie znajduje się katalog główny Twojej strony
- Jeśli to `/httpdocs/`, użyj: `REMOTE_PATH="/httpdocs/raport-ulgi-br/"`
- Jeśli to `/domains/inovgroup.pl/public_html/`, użyj tego
- **Slash na końcu jest WAŻNY:** `/raport-ulgi-br/` ✅ nie `/raport-ulgi-br` ❌

### 2.4 Zapisz i Zabezpiecz Plik

```bash
# Zapisz plik (w nano: Ctrl+O, Enter, Ctrl+X)

# Ustaw restrykcyjne uprawnienia (tylko Ty możesz odczytać)
chmod 600 .ftp-credentials
```

### 2.5 Sprawdź Plik

```bash
# Zobacz czy dane są poprawne (bez pokazywania hasła)
grep -v "FTP_PASS" .ftp-credentials
```

---

## Krok 3: Automatyczny Upload

### 3.1 Upewnij się, że HTML jest Wygenerowany

```bash
# Jeśli jeszcze nie generowałeś HTML:
./generate-html.sh
```

### 3.2 Nadaj Uprawnienia Skryptowi

```bash
chmod +x upload-to-server.sh
```

### 3.3 Uruchom Upload

```bash
./upload-to-server.sh
```

### 3.4 Co Zobaczysz

```
========================================
Inov Report - Automated Upload
========================================

Upload Configuration:
  Host: ftp.cyber-folks.pl
  User: inovgroup_upload
  Remote path: /public_html/raport-ulgi-br/
  Local directory: website-upload/

Upload files to server? (y/n):
```

Wpisz: **y** i naciśnij Enter

### 3.5 Postęp Uploadu

Zobaczysz coś takiego:

```
Using lftp for upload...
Uploading: index.html
Uploading: report-styles.css
Uploading: 00-cover.html
...
Uploading: images/innovation index map.png
...

========================================
✓ Upload successful!
========================================

Your report is now live at:
  https://inovgroup.pl/raport-ulgi-br/
```

### 3.6 Weryfikacja

1. Otwórz: **https://inovgroup.pl/raport-ulgi-br/**
2. Sprawdź czy strona się ładuje
3. Kliknij kilka rozdziałów
4. Sprawdź na telefonie

---

## Rozwiązywanie Problemów

### Problem 1: "Credentials file not found!"

**Przyczyna:** Nie utworzyłeś pliku `.ftp-credentials`

**Rozwiązanie:**
```bash
cp .ftp-credentials.template .ftp-credentials
nano .ftp-credentials
# Wypełnij dane i zapisz
```

### Problem 2: "Connection refused" lub "Login incorrect"

**Przyczyna:** Nieprawidłowe dane FTP

**Rozwiązanie:**
1. Sprawdź dane w panelu cyber-folks
2. Sprawdź czy wpisałeś poprawnie:
   - Host: `ftp.cyber-folks.pl` lub `ftp.inovgroup.pl`
   - User: bez spacji, dokładnie jak w panelu
   - Password: dokładnie jak ustawione (uwaga na wielkie/małe litery!)

**Test połączenia ręcznego:**
```bash
# Zainstaluj lftp jeśli potrzeba
sudo apt-get install lftp

# Test połączenia
lftp -u twoj_user,twoje_haslo ftp.cyber-folks.pl
# Jeśli się połączy, zobaczysz prompt: lftp twoj_user@ftp.cyber-folks.pl:~>
# Wpisz: ls
# Powinieneś zobaczyć listę katalogów
# Wpisz: quit
```

### Problem 3: "No such directory" lub upload do złego miejsca

**Przyczyna:** Nieprawidłowa ścieżka `REMOTE_PATH`

**Rozwiązanie:**
1. Połącz się ręcznie przez FTP:
   ```bash
   lftp -u twoj_user,twoje_haslo ftp.cyber-folks.pl
   ```
2. Sprawdź strukturę:
   ```
   ls
   cd public_html  # lub httpdocs
   ls
   pwd   # Pokaże pełną ścieżkę
   ```
3. Zaktualizuj `REMOTE_PATH` w `.ftp-credentials`

### Problem 4: "No FTP client found!"

**Przyczyna:** Brak zainstalowanego klienta FTP

**Rozwiązanie:**
```bash
# Ubuntu/Debian/Codespace
sudo apt-get update
sudo apt-get install lftp

# macOS
brew install lftp

# Potem uruchom ponownie:
./upload-to-server.sh
```

### Problem 5: Upload działa, ale strona nie jest dostępna

**Przyczyna:** Pliki są w złym katalogu

**Rozwiązanie:**
1. Zaloguj się do panelu → File Manager
2. Przejdź do `/public_html/` (lub `/httpdocs/`)
3. Sprawdź czy istnieje folder `raport-ulgi-br`
4. Otwórz `raport-ulgi-br` - czy widzisz `index.html`?
   - **NIE:** Sprawdź `REMOTE_PATH` w `.ftp-credentials`
   - **TAK:** Sprawdź czy możesz otworzyć URL: https://inovgroup.pl/raport-ulgi-br/index.html

### Problem 6: "Permission denied"

**Przyczyna:** Konto FTP nie ma uprawnień do zapisu w tym katalogu

**Rozwiązanie:**
1. W panelu cyber-folks sprawdź uprawnienia konta FTP
2. Upewnij się, że katalog domowy FTP to `/public_html/` (nie `/`)
3. Jeśli potrzeba, utwórz nowe konto FTP z pełnymi uprawnieniami

---

## Bezpieczeństwo

### ✅ Dobre Praktyki

**1. Nigdy nie commituj `.ftp-credentials` do git**
- Plik jest już w `.gitignore` ✓
- Sprawdź: `git status` - nie powinno pokazywać `.ftp-credentials`

**2. Restrykcyjne uprawnienia**
```bash
chmod 600 .ftp-credentials
```
- Tylko Ty możesz odczytać plik

**3. Silne hasło FTP**
- Minimum 12 znaków
- Mix liter, cyfr, symboli
- Nie używaj tego samego hasła co do panelu

**4. Po uploadzie możesz usunąć plik**
```bash
rm .ftp-credentials
```
- Później odtworzysz z template gdy będzie potrzeba

**5. Używaj SFTP zamiast FTP (jeśli dostępne)**
- Sprawdź w panelu czy cyber-folks oferuje SFTP/SSH
- Jeśli tak, zmień `FTP_HOST` i `FTP_PORT`:
  ```bash
  FTP_HOST="ssh.cyber-folks.pl"  # lub sftp.cyber-folks.pl
  FTP_PORT="22"
  ```

### ❌ Czego NIE robić

- ❌ Nie wysyłaj `.ftp-credentials` emailem
- ❌ Nie wklejaj hasła na Slack/Discord/Messenger
- ❌ Nie commituj do GitHub/GitLab
- ❌ Nie pozostawiaj pliku z prawami 777

---

## Przyszłe Aktualizacje

### Proces Aktualizacji Raportu

**Gdy edytujesz markdown:**

```bash
# 1. Edytuj pliki .md
nano 06-chapter-4-statistical-gap.md

# 2. Wygeneruj nowy HTML
./generate-html.sh

# 3. Automatyczny upload
./upload-to-server.sh

# Gotowe! Strona zaktualizowana w ~30 sekund
```

### Tylko Wybranych Plików

Jeśli chcesz wgrać tylko jeden plik (np. po małej zmianie):

```bash
# Wgraj tylko jeden rozdział
curl -T website-upload/06-chapter-4-statistical-gap.html \
  "ftp://ftp.cyber-folks.pl/public_html/raport-ulgi-br/06-chapter-4-statistical-gap.html" \
  --user "twoj_user:twoje_haslo"
```

---

## Podsumowanie

**Setup (raz):**
1. Pobierz dane FTP z panelu cyber-folks
2. Skopiuj `.ftp-credentials.template` → `.ftp-credentials`
3. Wypełnij dane FTP
4. `chmod 600 .ftp-credentials`

**Upload (za każdym razem):**
```bash
./generate-html.sh      # Wygeneruj HTML
./upload-to-server.sh   # Wgraj na serwer
```

**URL raportu:**
```
https://inovgroup.pl/raport-ulgi-br/
```

---

## Wsparcie

**Problemy z FTP/hostingiem:**
- Support cyber-folks: support@cyber-folks.pl
- Panel: https://panel.cyber-folks.pl

**Problemy ze skryptem:**
- Opisz błąd który widzisz
- Pokaż output terminala
- Sprawdź sekcję "Rozwiązywanie problemów" powyżej

---

**Autor:** Inov Research & Development
**Data:** Październik 2025
**Kontakt:** kkonopka@inovgroup.pl
