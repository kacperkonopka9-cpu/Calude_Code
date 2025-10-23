# 3. User Interface Design Goals

## 3.1 UX Vision

The user interface shall embody the **iNOV Research & Development** brand identity while delivering a streamlined, professional workflow for Polish R&D tax consultants. The design prioritizes **speed over polish** and **clarity over features**, reflecting the consultant's need to process batches efficiently under tight deadlines.

**Core Design Principles** (from front-end specification):
1. **Speed First** - Minimize clicks and cognitive load; default paths for common workflows
2. **Clarity of Understanding** - Transparent AI process with quality scores and edit tracking
3. **Transparency** - Clear status, progress indicators, and error messages
4. **Professional Polish** - Clean, uncluttered interface with iNOV branding

**Design Decision Protocol**: When principles conflict, resolve in priority order: **Speed > Clarity > Transparency > Polish**

## 3.2 Target Personas

The interface serves three primary user types (detailed in `docs/front-end-spec.md`):

1. **Agnieszka (Primary: Time-Pressed Consultant)** - 32, senior R&D tax consultant, processes 20+ cards per deadline, needs fastest possible workflow
2. **Marcin (Secondary: Quality Guardian)** - 28, junior consultant, focuses on compliance accuracy, needs confidence-building transparency
3. **Beata (Tertiary: Inbound Accountant)** - 45, limited R&D tax knowledge, needs clear guidance and error prevention

## 3.3 Key Interaction Paradigms

**Workflow Model**: **Linear Pipeline with Exit Ramps**
- Primary flow: Upload → Validate → Generate → Review → Download
- Exit ramps: Save draft, retry failed, regenerate sections, download template
- No complex navigation trees; Dashboard serves as home base

**Status Visibility**: **Glanceable Progress**
- Real-time batch processing grid showing all 20 projects simultaneously
- Color-coded states: Gray (queue), Yellow (generating), Green (complete), Red (error)
- Estimated time remaining updates every 2 seconds

**Quality Feedback**: **Numeric + Visual**
- Quality score (0-100%) displayed prominently per project
- Yellow highlight for AI-generated content, white for edited
- Score recalculates in real-time as consultant edits

**Error Handling**: **Inline + Actionable**
- Validation errors shown in-context (red border on upload, row-level messages)
- Failed generation shows "Spróbuj ponownie" button
- Excel template download link embedded in error messages

## 3.4 Core Screens and Views

Detailed wireframes and component specifications are available in `docs/front-end-spec.md` (Section 4) and visual design specifications in `docs/figma-design-specifications.md`. Summary:

### 3.4.1 Dashboard (Home)
- **Purpose**: Entry point showing recent batches and status overview
- **Key Elements**:
  - "Nowa partia" (New Batch) prominent CTA button
  - Recent batches table (10 rows) with status, date, project count
  - "Pobierz szablon Excel" (Download Template) link in header
- **Interactions**: Click batch row to resume/view; click "Nowa partia" to start upload

### 3.4.2 Upload Screen
- **Purpose**: Excel file upload with validation
- **Key Elements**:
  - Drag-and-drop upload zone (fallback: file picker)
  - Real-time validation with row-level error display
  - "Pobierz szablon" link if validation fails
  - "Rozpocznij generowanie" (Start Generation) button enabled only after successful validation
- **Interactions**: Upload → Validate → Proceed or Download Template → Fix → Re-upload

### 3.4.3 Processing Screen
- **Purpose**: Real-time batch generation monitoring
- **Key Elements**:
  - Grid of project cards (1-20) showing status per project
  - Each card displays: Project name, status (Oczekuje/Generowanie/Gotowe/Błąd), progress bar
  - Overall batch progress: "12/20 gotowych, ~8 minut pozostało"
  - "Anuluj" (Cancel) button to stop remaining generations
- **Interactions**: Auto-refresh every 2s; click completed project to preview; retry failed projects

### 3.4.4 Results & Review Screen
- **Purpose**: Review generated content and make edits
- **Key Elements**:
  - Left sidebar: List of all projects in batch with quality scores
  - Main panel: Selected project's 8 sections with inline editing
  - Quality score badge (0-100%) updates as edits are made
  - "Regeneruj sekcję" button per section
  - Yellow highlight for AI content, white for edited
  - "Pobierz projekt" (Download) and "Pobierz wszystko" (Download All) buttons
- **Interactions**: Click project in sidebar to switch; edit inline; regenerate sections; download individually or as ZIP

### 3.4.5 Error Recovery Screen
- **Purpose**: Handle validation failures and generation errors
- **Key Elements**:
  - Clear error message in Polish explaining issue
  - Specific row numbers and field names for validation errors
  - "Pobierz szablon Excel" button
  - "Spróbuj ponownie" (Retry) button for generation failures
  - "Wróć do panelu" (Back to Dashboard) link
- **Interactions**: Download template → fix data → re-upload; or retry failed generation

## 3.5 Visual Design System

**Brand Identity**: iNOV Research & Development
- **Primary Color**: Yellow (#F5C344) - used for primary CTAs, highlights, accents
- **Secondary Color**: Navy (#2C3E50) - used for text, headers, navigation
- **Logo**: Light bulb icon with "iNOV" wordmark (3 variants: horizontal, stacked, icon-only)
- **Typography**: Inter (UI), Roboto Slab (headings) - see Figma specs for exact weights

**Component Library** (Material-UI v5 customization):
- **inovTheme**: Custom MUI theme with iNOV color palette
- **ProjectCardGrid**: Grid layout for batch processing display
- **QualityScoreBadge**: 0-100% score with color-coded background (red <50, yellow 50-69, green ≥70)
- **InlineEditor**: Rich text editor with AI highlight toggle
- **UploadZone**: Drag-and-drop with validation state

**Detailed specifications**: See `docs/figma-design-specifications.md` for:
- Complete color palette (primary, secondary, semantic colors)
- Typography scale (heading levels, body text, captions)
- Component anatomy (dimensions, spacing, states)
- Screen layouts with ASCII diagrams and measurements
- MUI theme configuration code snippet

## 3.6 Accessibility Requirements

**WCAG 2.1 Level AA Compliance**:
- **Keyboard Navigation**: All interactive elements (buttons, links, form fields) must be keyboard accessible with visible focus indicators (2px yellow outline)
- **Screen Reader Support**: All images have alt text, form fields have labels, status updates announced via ARIA live regions
- **Color Contrast**: Minimum 4.5:1 ratio for text (Navy #2C3E50 on white backgrounds meets this)
- **Focus Management**: Logical tab order, focus trapped in modals, focus restored after actions
- **Error Identification**: Validation errors announced to screen readers with `role="alert"`

**Testing**: Manual testing with NVDA/JAWS screen readers and keyboard-only navigation required before launch.

## 3.7 Responsive Design Strategy

**Primary Platform**: Desktop Web (1366×768 minimum, optimized for 1920×1080)
- Full feature set including upload, real-time processing, inline editing, export

**Secondary Platform**: Tablet (768px-1365px)
- View-only Dashboard and Results screens
- Upload and editing require desktop (show "Użyj komputera do edycji" message)

**Tertiary Platform**: Mobile (≤767px)
- Dashboard list view only
- No upload, processing, or editing functionality
- "Ta funkcja wymaga komputera" message for restricted features

**Rationale**: Consultants perform primary work on desktop computers. Mobile/tablet support enables checking status on-the-go but not full workflow (per user research in brief).

## 3.8 Platform and Browser Support

**Supported Browsers**:
- Chrome/Edge (Chromium) 90+
- Firefox 88+
- Safari 14+

**Operating Systems**:
- Windows 10+
- macOS 11+
- Linux (Ubuntu 20.04+ with supported browsers)

**Not Supported**:
- Internet Explorer (EOL)
- Mobile browsers for editing (view-only acceptable)

## 3.9 UI Goals Summary

The user interface design aims to:
1. **Reduce cognitive load** through linear workflow and glanceable status displays
2. **Build trust** through transparency (quality scores, AI highlights, clear errors)
3. **Enable speed** through keyboard shortcuts, default paths, and parallel processing visibility
4. **Ensure accessibility** for all consultant personas regardless of technical skill
5. **Reflect brand** through consistent iNOV visual identity (yellow/navy, light bulb motif)
6. **Support quality** through inline editing, section regeneration, and real-time score updates

**Success Metrics** (measurable post-launch):
- Average time from upload to first download: <10 minutes
- Consultant satisfaction with UI clarity: ≥4.5/5 (survey)
- Accessibility audit score: ≥95% WCAG 2.1 AA compliance
- Error recovery success rate: ≥90% (users who encounter errors successfully resolve them)

---

**References**:
- Detailed UX specification: `docs/front-end-spec.md`
- Visual design system: `docs/figma-design-specifications.md`
- User research and personas: `docs/brief.md` (Section 3)

---
