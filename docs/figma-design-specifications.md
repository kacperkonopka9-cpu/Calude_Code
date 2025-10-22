# Figma Design Specifications
## R&D Tax Relief Project Card Generator - UI/UX Design Guide

**Project:** R&D Tax Relief Project Card Generation System
**Brand:** iNOV Research & Development
**Design System:** Material-UI v5 with Custom iNOV Branding
**Date:** 2025-10-22
**Version:** 1.0

---

## 🎨 Brand Identity

### Logo Usage

**Primary Logo:** iNOV Research & Development
- **Icon:** Light bulb with radiating rays (symbolizes innovation, ideas, R&D)
- **Wordmark:** "iNOV" in bold sans-serif
- **Tagline:** "RESEARCH & DEVELOPMENT" in uppercase on yellow baseline
- **File Location:** `docs/Branding/4.png` (full logo with tagline)

**Logo Variations:**
1. **Full Logo** (Image 4.png): Use in header, large screens
2. **Compact Logo** (Image 1.png): Use in mobile header, favicon
3. **Icon Only** (Image 2.png): Use for app icon, loading states

**Logo Placement:**
- **Desktop:** Top left of AppBar, 180px width
- **Mobile:** Top left, 120px width (compact version)
- **Favicon:** 32x32px, light bulb icon only

**Clear Space:** Minimum 16px clear space around logo on all sides

**Don't:**
- Change logo colors (always yellow + navy)
- Stretch or distort proportions
- Place on busy backgrounds (use white or light gray only)

---

## 🎨 Color Palette (Updated with iNOV Branding)

### Primary Colors

| Color Name | Hex Code | RGB | Usage | MUI Theme Key |
|------------|----------|-----|-------|---------------|
| **iNOV Yellow** | `#F5C344` | 245, 195, 68 | Primary brand color, CTAs, accents, focus states | `primary.main` |
| **iNOV Yellow Dark** | `#D9A827` | 217, 168, 39 | Hover states, active buttons | `primary.dark` |
| **iNOV Yellow Light** | `#F8D672` | 248, 214, 114 | Subtle backgrounds, highlights | `primary.light` |
| **iNOV Navy** | `#2C3E50` | 44, 62, 80 | Typography, navigation text, headings | `text.primary` |
| **Navy Light** | `#4A5F75` | 74, 95, 117 | Secondary text, less emphasis | `text.secondary` |

### Secondary Colors

| Color Name | Hex Code | RGB | Usage | MUI Theme Key |
|------------|----------|-----|-------|---------------|
| **Teal Accent** | `#4FC3DC` | 79, 195, 220 | Data visualization, info messages, charts | `info.main` |
| **Success Green** | `#2ECC71` | 46, 204, 113 | Success states, valid status, high quality scores | `success.main` |
| **Warning Orange** | `#F39C12` | 243, 156, 18 | Warning states, medium quality scores | `warning.main` |
| **Error Red** | `#E74C3C` | 231, 76, 60 | Error states, invalid status, failures | `error.main` |

### Neutral Colors

| Color Name | Hex Code | RGB | Usage | MUI Theme Key |
|------------|----------|-----|-------|---------------|
| **Background** | `#FAFAFA` | 250, 250, 250 | Page background | `background.default` |
| **Surface** | `#FFFFFF` | 255, 255, 255 | Cards, dialogs, elevated surfaces | `background.paper` |
| **Light Gray** | `#B8CFD9` | 184, 207, 217 | Subtle backgrounds, disabled states | - |
| **Divider** | `#E0E0E0` | 224, 224, 224 | Borders, dividers, table lines | `divider` |
| **Text Primary** | `#2C3E50` | 44, 62, 80 | Headings, body text | `text.primary` |
| **Text Secondary** | `#7F8C8D` | 127, 140, 141 | Secondary text, labels | `text.secondary` |

### Color Usage Guidelines

**Primary Actions:** iNOV Yellow (`#F5C344`)
- Download Template button
- Generate Batch button
- Primary CTAs

**Secondary Actions:** iNOV Navy (`#2C3E50`)
- Cancel buttons (outlined)
- Navigation links
- Secondary CTAs

**Status Colors (Must include icons for accessibility):**
- ✅ **Valid/Success:** Green + checkmark icon
- ⚠️ **Warning:** Orange + warning icon
- ❌ **Error/Invalid:** Red + error icon
- 💡 **Info:** Teal + info icon

---

## 🔤 Typography

### Font Families

**Primary Font:** `'Roboto', sans-serif` (MUI default)
- **Rationale:** Professional, excellent readability, Polish character support
- **Use:** All UI text, headings, body copy

**Accent Font (Optional):** For marketing/hero sections, consider bold sans-serif similar to iNOV logo
- **Alternative:** `'Montserrat', sans-serif` (700 weight for headings)
- **Use:** Large hero headings, marketing pages only

### Type Scale & Styles

| Element | Font | Size | Weight | Line Height | Color | Usage |
|---------|------|------|--------|-------------|-------|-------|
| **Display 1** | Roboto | 48px | 700 (Bold) | 1.2 | Navy `#2C3E50` | Marketing hero headlines |
| **H1** | Roboto | 32px | 400 (Regular) | 1.3 | Navy `#2C3E50` | Page titles |
| **H2** | Roboto | 28px | 500 (Medium) | 1.4 | Navy `#2C3E50` | Section headers |
| **H3** | Roboto | 24px | 500 (Medium) | 1.5 | Navy `#2C3E50` | Subsection headers |
| **H4** | Roboto | 20px | 500 (Medium) | 1.5 | Navy `#2C3E50` | Card titles |
| **H5** | Roboto | 18px | 500 (Medium) | 1.5 | Navy `#2C3E50` | Component headings |
| **Body 1** | Roboto | 16px | 400 (Regular) | 1.5 | Navy `#2C3E50` | Primary body text |
| **Body 2** | Roboto | 14px | 400 (Regular) | 1.43 | Navy Light `#4A5F75` | Secondary body text |
| **Button** | Roboto | 14px | 500 (Medium) | 1.75 | White (on yellow) | Button labels |
| **Caption** | Roboto | 12px | 400 (Regular) | 1.66 | Text Secondary `#7F8C8D` | Help text, metadata |

### Polish Language Support

- All fonts must support Polish diacritics: ą, ć, ę, ł, ń, ó, ś, ź, ż, Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż
- Roboto has excellent Polish character support
- Test all UI copy with Polish text samples

---

## 🖼️ Visual Style

### Image Treatment (iNOV Style)

**Photo Frames:**
- **Border:** 8px solid iNOV Yellow (`#F5C344`)
- **Corner Radius:** 16px (rounded corners)
- **Shadow:** `0px 4px 12px rgba(245, 195, 68, 0.25)` (yellow-tinted shadow)
- **Usage:** All photos, illustrations, preview thumbnails

**Example Implementation:**
```css
.inov-image-frame {
  border: 8px solid #F5C344;
  border-radius: 16px;
  box-shadow: 0px 4px 12px rgba(245, 195, 68, 0.25);
  overflow: hidden;
}
```

**Document Preview Cards:**
- Use yellow-framed images for project card previews
- Thumbnail size: 280x200px (landscape) or 200x280px (portrait)

### Geometric Accents

**Circles:**
- Use yellow circles for bullet points, step indicators
- Diameter: 40px (small), 60px (medium), 100px (large)
- Fill: iNOV Yellow `#F5C344`

**Rectangles/Bars:**
- Horizontal yellow bars for section dividers
- Height: 4px, full width or accent width
- Color: iNOV Yellow `#F5C344`

**Light Bulb Icon:**
- Use throughout app as decorative accent
- Color: iNOV Yellow `#F5C344`
- Size: 24px (inline), 48px (feature highlights)

---

## 📐 Layout & Spacing

### Grid System

**Container Max Width:** 1200px
**Gutters:** 24px between columns
**Columns:** 12-column grid

### Spacing Scale (8px base unit)

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 4px | Icon gaps, tight spacing |
| `sm` | 8px | Small padding, element gaps |
| `md` | 16px | Standard padding, card content |
| `lg` | 24px | Section spacing, card margin |
| `xl` | 32px | Large section gaps |
| `2xl` | 48px | Page section separators |
| `3xl` | 64px | Major layout divisions |

### Component Spacing

**Cards:**
- Padding: 24px (lg)
- Margin between cards: 16px (md)
- Border radius: 8px
- Elevation: `elevation={2}`

**Buttons:**
- Padding: 10px vertical, 24px horizontal
- Border radius: 4px (MUI default)
- Minimum touch target: 44x44px

**Forms:**
- Field spacing: 16px (md) between fields
- Label to input: 8px (sm)
- Form section spacing: 32px (xl)

---

## 🎨 Figma File Structure

### Pages to Create

1. **🎨 Design System**
   - Color palette swatches
   - Typography samples
   - Component library
   - Icon set

2. **📱 Screens - Desktop (1440px)**
   - Dashboard
   - Upload & Preview
   - Processing Status
   - Results Overview
   - Review Carousel
   - History
   - Settings

3. **📱 Screens - Tablet (768px)**
   - Key screens adapted for tablet

4. **📱 Screens - Mobile (375px)**
   - Simplified mobile views

5. **🔄 User Flows**
   - Flow diagrams with annotations
   - Edge cases and error states

6. **🧩 Components**
   - BatchProgressIndicator
   - QualityScoreCard
   - ProjectPreviewTable
   - DocumentCarousel
   - ExcelTemplateDownloadButton

---

## 🖥️ Screen Designs - Detailed Specifications

### Screen 1: Dashboard (1440x900px)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ ┌──────┐  Download Template  New Batch  History  👤User       │ <- AppBar (64px height)
│ │ iNOV │                                                        │    Background: #FFFFFF
│ └──────┘                                                        │    Border-bottom: 1px #E0E0E0
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  👋 Witaj z powrotem, Anna!                    [Light Bulb]│ │ <- Hero Card
│  │                                                            │ │    Background: Linear gradient
│  │  [🎯 Nowa Partia]  [📄 Pobierz Szablon]                  │ │    Yellow to Light Yellow
│  └──────────────────────────────────────────────────────────┘ │    Height: 200px, Radius: 16px
│                                                                 │
│  Ostatnie Partie                                                │ <- Section Header (H2)
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ Data      │ Projektów │ Status        │ Akcje            │ │ <- Table
│  ├──────────────────────────────────────────────────────────┤ │    Background: #FFFFFF
│  │ 2025-10-20│    18     │ ✅ Ukończono  │ [Zobacz][Pobierz]│ │    Elevation: 1
│  │ 2025-10-18│    12     │ ✅ Ukończono  │ [Zobacz][Pobierz]│ │
│  │ 2025-10-15│    20     │ ⚠️ 2 Błędy    │ [Przegląd][Ponów]│ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  W tym miesiącu: 142 karty | Średnia jakość: 87% | 38h saved  │ <- Stats Bar
│                                                                 │    Background: #F5C344
└────────────────────────────────────────────────────────────────┘    Height: 60px
```

**Components:**
- **AppBar:**
  - Height: 64px
  - Background: `#FFFFFF`
  - Logo: 180px width
  - Nav buttons: Yellow (#F5C344) for primary, Navy outlined for secondary

- **Hero Card:**
  - Background: Linear gradient `#F5C344` → `#F8D672`
  - Padding: 32px
  - Buttons: White text on Navy background (#2C3E50)
  - Light bulb icon: 80px, positioned top right

- **Recent Batches Table:**
  - Header: Navy (#2C3E50), 14px, 500 weight
  - Rows: Alternate white / light gray (#FAFAFA)
  - Status icons: Color-coded with text labels

- **Stats Bar:**
  - Background: Yellow (#F5C344)
  - Text: Navy (#2C3E50)
  - Height: 60px
  - Font: 16px, 500 weight

---

### Screen 2: Upload & Preview (1440x900px)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ Dashboard > Nowa Partia                                         │ <- Breadcrumb
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📄 Pobierz Szablon Excel (v1.0)                 [Pobierz]     │ <- Template Section
│  Użyj tego szablonu aby zapewnić poprawny format danych        │    Background: Light Yellow
│                                                                 │    Height: 80px
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                                                            │ │
│  │         📂 Przeciągnij i upuść plik Excel tutaj           │ │ <- Upload Zone
│  │                  lub [Przeglądaj Pliki]                   │ │    Border: 2px dashed #F5C344
│  │                                                            │ │    Border radius: 16px
│  │     Akceptowane: .xlsx | Max 20 projektów | 10MB          │ │    Background: #FAFAFA
│  └──────────────────────────────────────────────────────────┘ │    Height: 240px
│                                                                 │
│  ─── Po przesłaniu ───                                          │
│                                                                 │
│  ✅ Walidacja zakończona: 15 projektów wykrytych                │ <- Validation Result
│                                                                 │    Color: Success Green
│  Podgląd Projektów          [Zaznacz Wszystkie][Tylko Poprawne]│
│  ┌──────────────────────────────────────────────────────────┐ │
│  │☑│Nazwa Projektu  │Opis     │Zakres Dat│Status            │ │ <- Preview Table
│  ├──────────────────────────────────────────────────────────┤ │    Yellow-framed
│  │☑│Budowa A        │Zabytki..│2024-01-..│ ✅ Poprawny      │ │
│  │☑│System IT B     │ERP impl.│2024-03-..│ ✅ Poprawny      │ │
│  │☐│Produkcja C     │Okna pr..│2024-02-..│ ❌ Błąd          │ │ <- Error Row
│  │ │                │         │          │ Brak Celu        │ │    Background: Light Red
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  [Powrót do Przesyłania]              [Generuj Wybrane (12/15)]│
└────────────────────────────────────────────────────────────────┘
```

**Components:**

- **Template Download Section:**
  - Background: `#FFF9E6` (very light yellow)
  - Border-left: 4px solid `#F5C344`
  - Padding: 20px
  - Button: Yellow (#F5C344) with download icon

- **Upload Zone (Drag & Drop):**
  - **Default State:**
    - Border: `2px dashed #F5C344`
    - Background: `#FAFAFA`
    - Text: Navy (#2C3E50)
    - Icon: 48px upload file icon, yellow

  - **Hover State (file dragged over):**
    - Border: `3px solid #F5C344` (animated pulse)
    - Background: `#FFF9E6` (light yellow)
    - Scale: 1.02 (subtle grow)

  - **Uploading State:**
    - Show linear progress bar (yellow)
    - Text: "Przesyłanie... 45%"

- **Preview Table:**
  - Frame: 8px solid #F5C344 (iNOV style)
  - Border radius: 16px
  - Header: Navy background, white text
  - Checkbox column: 40px width
  - Status column: Icon + text (120px width)
  - Error rows: `background: #FFEBEE` (light red)
  - Valid rows: `background: #E8F5E9` (light green)

- **Generate Button:**
  - Background: Yellow (#F5C344)
  - Text: Navy (#2C3E50)
  - Height: 48px
  - Icon: Play arrow
  - Show project count: "Generuj Wybrane (12/15)"

---

### Screen 3: Processing Status (1440x900px)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ Dashboard > Partia #47 > Przetwarzanie                         │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Generowanie Kart Projektów...                                  │ <- Header (H1)
│                                                                 │
│  ██████████████████░░░░░░░░░░░░ 60%                            │ <- Progress Bar
│                                                                 │    Color: Yellow gradient
│  Przetwarzanie projektu 9 z 15                                  │    Height: 12px
│  Szacowany czas pozostały: 2 minuty                             │    Radius: 6px
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Aktualnie Przetwarzane:                                  │ │ <- Progress Detail Card
│  │  💡 Projekt F - Proces Produkcyjny    [●●●●●○○○] 65%     │ │    Background: #FFFFFF
│  │  💡 Projekt G - System Bezpieczeństwa [●●●○○○○○] 40%     │ │    Border: 1px #E0E0E0
│  │  💡 Projekt H - System Energetyczny   [●●○○○○○○] 30%     │ │    Yellow accents
│  │  💡 Projekt I - Technologia Budowlana [●○○○○○○○] 15%     │ │
│  │  💡 Projekt J - Narzędzie Logistyczne [○○○○○○○○] 0%      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ✅ Ukończono: 8  |  ⏳ Przetwarzanie: 5  |  ⏸️ W kolejce: 2   │ <- Status Summary
│                                                                 │    Background: Light Gray
│  [Anuluj Partię]                                                │
│                                                                 │
│  💡 Wskazówka: Możesz zamknąć to okno. Wyślemy Ci email,       │ <- Info Box
│     gdy partia będzie gotowa.                                   │    Background: Teal Light
└────────────────────────────────────────────────────────────────┘
```

**Components:**

- **Main Progress Bar:**
  - Background: `#E0E0E0` (gray)
  - Fill: Linear gradient `#F5C344` → `#D9A827`
  - Height: 12px
  - Border radius: 6px
  - Animated shimmer effect

- **Progress Detail Card:**
  - Each row shows:
    - Light bulb icon (💡) - Yellow, 24px
    - Project name - Navy, 14px
    - Mini progress bar - 8 dots, filled/empty
    - Percentage - Navy, 500 weight
  - Row spacing: 12px
  - Yellow left border accent

- **Status Summary Bar:**
  - Background: `#F5F5F5`
  - Icons: Colored (green checkmark, yellow clock, gray pause)
  - Font: 16px, 500 weight
  - Height: 50px

- **Info Box:**
  - Background: `#E0F7FA` (light teal)
  - Border-left: 4px solid `#4FC3DC` (teal)
  - Icon: Light bulb, yellow
  - Padding: 16px

---

### Screen 4: Results Overview (1440x900px)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ Dashboard > Partia #47 > Wyniki                                │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✅ Partia Ukończona!                                           │ <- Success Header
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │ <- Metric Cards
│  │     13     │  │      0     │  │      2     │               │    Yellow accents
│  │ Udane      │  │ Ostrzeżenia│  │  Błędne    │               │
│  └────────────┘  └────────────┘  └────────────┘               │
│       ✅              ⚠️              ❌                         │
│                                                                 │
│  Udane Projekty                            [Pobierz Wszystkie]│
│  ┌──────────────────────────────────────────────────────────┐ │
│  │Nazwa Projektu  │Jakość│Wygenerowano│Akcje               │ │ <- Success Table
│  ├──────────────────────────────────────────────────────────┤ │    Green accents
│  │Budowa A        │ 92% 🟢│2025-10-22  │[Przegląd][⬇]      │ │
│  │System IT B     │ 88% 🟡│2025-10-22  │[Przegląd][⬇]      │ │
│  │Produkcja D     │ 95% 🟢│2025-10-22  │[Przegląd][⬇]      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ❌ Projekty Błędne (2)                                         │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │Produkcja C     │ Błąd: Brak wymaganego pola - Cel      │ │ <- Error Section
│  │                │ [Zobacz Szczegóły][Edytuj][Ponów]     │ │    Red accents
│  │────────────────────────────────────────────────────────│ │
│  │Logistyka E     │ Błąd: Nieprawidłowy format daty       │ │
│  │                │ [Zobacz Szczegóły][Edytuj][Ponów]     │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  [Eksportuj Błędne do Excel]  [Ponów Wszystkie Błędne]         │
└────────────────────────────────────────────────────────────────┘
```

**Components:**

- **Metric Cards (Hero):**
  - Size: 200px x 150px
  - Background: `#FFFFFF`
  - Border: 2px solid (green/yellow/red based on status)
  - Top accent bar: 4px solid (status color)
  - Number: 48px, 700 weight
  - Label: 16px, 400 weight
  - Icon: 64px below number
  - Yellow frame effect on hover

- **Success Table:**
  - Quality Score Badge:
    - 🟢 **90-100%:** Green circle, "Doskonała"
    - 🟡 **70-89%:** Yellow circle, "Wymaga Przeglądu"
    - 🔴 **<70%:** Red circle, "Wymaga Uwagi"
  - Badge size: 60px x 28px
  - Border radius: 14px

- **Error Section:**
  - Background: `#FFEBEE` (light red)
  - Border-left: 4px solid `#E74C3C` (error red)
  - Padding: 16px
  - Expandable accordion for details
  - Action buttons: Outlined, error color

---

### Screen 5: Review Carousel (1440x900px)

**Layout:**
```
┌────────────────────────────────────────────────────────────────┐
│ Dashboard > Partia #47 > Przegląd                              │
├──┬───────────────────────────────────────────────────────┬────┤
│  │                                                        │    │
│📃││  Karta 5 z 13                   ← [5/13] →          ││🚩  │
│  ││                                                        ││    │
│#1││  ┌────────────────────────────────────────────────┐ ││Jako││
│92││  │ [Yellow-framed document preview]               │ ││ść: ││
│🟢││  │                                                │ ││87% ││
│  ││  │ Tytuł projektu:                                │ ││🟡  ││
│#2││  │ "Innowacyjny system..."                        │ ││    ││
│88││  │                                                │ ││Flag││
│🟡││  │ Cel/Opis:                                      │ ││ged:││
│  ││  │ Lorem ipsum dolor sit amet consectetur...     │ ││    ││
│#3││  │                                                │ ││• Se││
│95││  │ Podstawowe etapy:                              │ ││ c3 ││
│🟢││  │ 1. Analiza wymagań...                          │ ││    ││
│  ││  │ 2. Projektowanie rozwiązania...                │ ││• Se││
│#4││  │                                                │ ││ c5 ││
│88││  │ Problemy badawcze:                             │ ││    ││
│🟡││  │ Problem 1: Optymalizacja...                    │ ││Nav:││
│  ││  │                                                │ ││    ││
│#5││  │ Poziom innowacyjności:                         │ ││[S1]││
│87││  │ Projekt charakteryzuje się wysokim...          │ ││[S2]││
│🟡││  │                                                │ ││[S3]││
│  ││  └────────────────────────────────────────────────┘ ││[S4]││
│...││                                                      ││[S5]││
│  ││  [⬇ Pobierz] [🚩 Oznacz] [✓ Oznacz jako Przegląd] ││    │
│  │└──────────────────────────────────────────────────────┴────┘│
└────────────────────────────────────────────────────────────────┘
```

**Components:**

- **Left Sidebar (Thumbnails):**
  - Width: 100px
  - Cards: 80px x 100px each
  - Yellow frame around active card (4px)
  - Quality badge on each: Small circle (20px)
  - Scrollable list
  - Background: `#FAFAFA`

- **Main Document Area:**
  - Width: 700px
  - Background: `#FFFFFF`
  - Document preview in yellow frame (8px border)
  - Polish text formatting
  - Scrollable content

- **Right Panel (Quality Info):**
  - Width: 240px
  - Background: `#FAFAFA`
  - Quality score badge: Large (100px x 100px)
  - Flagged sections list:
    - Yellow warning icons
    - Click to jump to section
  - Section navigation buttons

- **Action Buttons (Bottom):**
  - Download: Yellow background, navy text
  - Flag: Outlined, warning color
  - Mark Reviewed: Outlined, success color

---

## 🎨 Component Library Specifications

### 1. BatchProgressIndicator

**Variants:**

**A. Detailed (Processing Page):**
```
┌──────────────────────────────────────────────────┐
│ Generowanie...                                    │
│ ██████████████████░░░░░░░░░░░░ 60%              │
│ Projekt 9 z 15 | ~2 minuty pozostało             │
│                                                   │
│ Aktualnie:                                        │
│ 💡 Projekt F [●●●●●○○○] 65%                     │
│ 💡 Projekt G [●●●○○○○○] 40%                     │
└──────────────────────────────────────────────────┘
```
- Progress bar: Yellow gradient, 12px height
- Light bulb icons: Yellow, 20px
- Mini bars: Yellow filled dots, gray empty dots

**B. Compact (Dashboard):**
```
┌────────────────────────────────┐
│ ⏳ Przetwarzanie 5/15 (33%)   │
│ ██████░░░░░░░░░░░░░░░░░░      │
└────────────────────────────────┘
```
- Height: 60px
- Yellow progress bar
- Clock icon

---

### 2. QualityScoreCard

**Variants:**

**A. Large (Results Page):**
```
┌────────────────┐
│      92%       │ <- 48px, 700 weight
│                │
│  Doskonała     │ <- 16px, 500 weight
│                │
│ [Zobacz Szcze- │ <- Link
│  góły]         │
└────────────────┘
```
- Size: 150px x 150px
- Background: Gradient based on score
  - 90-100%: Green gradient
  - 70-89%: Yellow gradient
  - <70%: Red gradient
- Border radius: 16px
- Yellow frame (8px) on hover

**B. Compact (Thumbnail):**
```
┌──────┐
│ 92%  │
│  🟢  │
└──────┘
```
- Size: 60px x 60px
- Circle badge
- Just score + colored dot

**C. Inline (Table Cell):**
```
92% 🟢
```
- Font: 14px, 500 weight
- Colored circle: 12px

---

### 3. ProjectPreviewTable

**Style:**
- Yellow frame: 8px solid #F5C344
- Border radius: 16px
- Header: Navy background, white text, 14px, 500 weight
- Rows: Striped (white / #FAFAFA)
- Hover: Yellow tint (#FFF9E6)
- Checkbox: Yellow when checked
- Status icons: 24px, colored
- Error rows: Light red background (#FFEBEE)

---

### 4. DocumentCarousel

**Layout:**
- Left sidebar: 100px (thumbnails)
- Main area: 700px (document)
- Right panel: 240px (quality info)
- All panels: Yellow accents
- Active thumbnail: Yellow frame (4px)
- Navigation: Yellow arrow buttons

---

### 5. ExcelTemplateDownloadButton

**Variants:**

**A. Primary (Large):**
```
┌─────────────────────────────────┐
│  📄  Pobierz Szablon (v1.0)     │
└─────────────────────────────────┘
```
- Background: Yellow (#F5C344)
- Text: Navy (#2C3E50)
- Icon: Download, 24px
- Size: 240px x 56px
- Border radius: 8px

**B. Secondary (Header):**
```
┌────────────────────┐
│ 📄 Szablon (v1.0)  │
└────────────────────┘
```
- Background: White
- Border: 2px solid Yellow
- Text: Navy
- Size: 180px x 44px

---

## 📱 Responsive Breakpoints

### Desktop (1440px+)
- All features, full layout
- 3-column review carousel

### Tablet (768px - 1439px)
- 2-column review (document + quality combined)
- Slightly condensed tables

### Mobile (< 768px)
- Single column
- Hamburger menu
- Card-based preview instead of table
- Simplified carousel (swipe)

---

## ✨ Animations & Micro-interactions

### Button Hover (Yellow Primary)
```
Default: background: #F5C344
Hover:   background: #D9A827, scale: 1.02, shadow: 0 4px 12px rgba(245,195,68,0.4)
Active:  background: #C08A1F, scale: 0.98
```
Duration: 150ms, easing: ease-out

### Card Hover
```
Default: elevation: 1, border: 1px solid #E0E0E0
Hover:   elevation: 3, border: 2px solid #F5C344, scale: 1.01
```
Duration: 200ms, easing: ease-in-out

### Progress Bar Animation
```
Shimmer effect: Linear gradient moving left-to-right
Colors: #F5C344 → #FFF9E6 → #F5C344
Duration: 1.5s infinite
```

### Upload Zone Drag-over
```
Border pulse: 2px dashed → 3px solid (yellow)
Background: #FAFAFA → #FFF9E6
Duration: 300ms loop
```

---

## 🔧 MUI Theme Configuration (React)

```javascript
import { createTheme } from '@mui/material/styles';

const inovTheme = createTheme({
  palette: {
    primary: {
      main: '#F5C344',      // iNOV Yellow
      dark: '#D9A827',
      light: '#F8D672',
      contrastText: '#2C3E50',  // Navy text on yellow
    },
    secondary: {
      main: '#2C3E50',      // iNOV Navy
      dark: '#1A252F',
      light: '#4A5F75',
      contrastText: '#FFFFFF',
    },
    success: {
      main: '#2ECC71',
    },
    warning: {
      main: '#F39C12',
    },
    error: {
      main: '#E74C3C',
    },
    info: {
      main: '#4FC3DC',      // Teal
    },
    background: {
      default: '#FAFAFA',
      paper: '#FFFFFF',
    },
    text: {
      primary: '#2C3E50',   // Navy
      secondary: '#7F8C8D',
    },
    divider: '#E0E0E0',
  },
  typography: {
    fontFamily: "'Roboto', sans-serif",
    h1: {
      fontSize: '2rem',
      fontWeight: 400,
      color: '#2C3E50',
    },
    h2: {
      fontSize: '1.75rem',
      fontWeight: 500,
      color: '#2C3E50',
    },
    // ... rest of type scale
  },
  shape: {
    borderRadius: 8,
  },
  spacing: 8,  // 8px base unit
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',  // No uppercase transform
          borderRadius: 8,
          padding: '10px 24px',
        },
        containedPrimary: {
          backgroundColor: '#F5C344',
          color: '#2C3E50',
          '&:hover': {
            backgroundColor: '#D9A827',
          },
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          padding: '24px',
        },
      },
    },
    // ... more component overrides
  },
});

export default inovTheme;
```

---

## 📦 Figma Plugins to Use

1. **Material Design Kit** - For MUI components
2. **Stark** - For accessibility contrast checking
3. **Autoflow** - For user flow diagrams
4. **Content Reel** - For Polish text generation
5. **Unsplash** - For placeholder images (use yellow frames!)

---

## 🎯 Design Handoff Checklist

- [ ] All screens designed at 1440px, 768px, 375px
- [ ] Color palette documented with hex codes
- [ ] Typography specs complete with Polish examples
- [ ] Component library with all 5 custom components
- [ ] Logo assets exported (SVG, PNG @1x, @2x, @3x)
- [ ] Icon set compiled (all Material Icons used)
- [ ] Animations documented with timing/easing
- [ ] Accessibility notes for each component
- [ ] Developer handoff notes in Figma comments
- [ ] Export all assets to /assets folder
- [ ] Create Figma dev mode specs

---

## 📁 Asset Export Guide

### Logo Exports

**From:** `docs/Branding/`

Export as:
- `logo-full.svg` (Image 4 - full logo with tagline)
- `logo-compact.svg` (Image 1 - iNOV with light bulb)
- `logo-icon.svg` (Image 2 - light bulb only)
- `logo-icon-32.png` (32x32 favicon)
- `logo-icon-192.png` (192x192 PWA icon)
- `logo-icon-512.png` (512x512 PWA icon)

### Color Swatches
Export color palette as CSS variables file.

### Icons
Export all custom icons as 24x24 SVG.

---

**End of Figma Design Specifications**

Next Steps:
1. Create Figma account and start new project
2. Import logo assets from `/docs/Branding/`
3. Set up color styles and typography styles
4. Build component library
5. Design 5 key screens using these specifications
6. Share Figma link with development team for handoff

Questions? Reference this document for all design decisions!
