# Excel Templates Directory

This directory contains Excel templates used for data collection in the R&D Tax Relief Project Card Generator.

## Files

### 1. UBR_CC_Karta_Projektu_v2.xlsx (CURRENT - Use This!)
**Status**: ✅ Active - Ready for MVP Development
**Date**: October 22, 2025
**Version**: 2.0

**Purpose**: Data collection template for consultants to input R&D project information before AI generation.

**Structure**:
- **Sheet 1 "Dane projektów"**: Project data entry (20 rows)
  - 10 columns (A-J): Row number, Project name, Start date, End date, Description, Goal, Novelty, Challenges, Documentation, Responsible person
  - Row 5: Example data (realistic IoT/ML project)
  - Built-in Excel data validation (dates, text lengths)
  - iNOV branding (Yellow #F5C344, Navy #2C3E50)

- **Sheet 2 "Instrukcje"**: Comprehensive instructions
  - Field-by-field explanations
  - Examples of good responses
  - Data quality tips for AI generation
  - Step-by-step usage guide

**PRD Compliance**: 95% (Epic 1: FR1, FR2, FR4)

**Key Features**:
- ✅ All 7 required columns per PRD FR1 (including "Osoba odpowiedzialna")
- ✅ Data validation rules (dates, text lengths)
- ✅ Example data row demonstrating format
- ✅ Instructions sheet with detailed field explanations
- ✅ iNOV branding applied
- ✅ Polish language throughout

**Usage**:
1. Consultants download this template from system Dashboard or Upload screen
2. Fill in project data (1-20 projects) in rows 7-26
3. Delete example row (row 5) before upload
4. Upload to system for AI-powered project card generation

**For Developers**:
- Parse columns B-J (skip column A row numbers)
- Validate according to FR2 requirements
- Map to backend data model:
  - B → project_name
  - C → start_date (DD/MM/YYYY)
  - D → end_date (DD/MM/YYYY)
  - E → description (min 100 chars)
  - F → goal (min 50 chars)
  - G → novelty_element (optional)
  - H → technical_challenges (optional)
  - I → documentation (optional)
  - J → responsible_person

---

### 2. UBR_CC_Karta_Projektu_v1_original.xlsx (DEPRECATED)
**Status**: ⚠️ Archived - For Reference Only
**Date**: Original submission
**Version**: 1.0

**Purpose**: Original template provided by user, kept for reference.

**Issues** (why v2 was created):
- ❌ Missing required column "Osoba odpowiedzialna"
- ❌ No data validation rules
- ❌ No example data
- ❌ No instructions sheet
- ⚠️ Combined Opis/Cel in single column

**Do NOT use this version for development.**

---

## Related Documentation

- **Template Review**: `docs/reviews/TEMPLATE_REVIEW_AND_UPDATES.md`
  - Detailed comparison of v1 vs v2
  - Issue analysis and fixes
  - Testing recommendations
  - Migration plan

- **PRD Epic 1**: `docs/prd.md` (Section 5, Epic 1: Excel Template & Data Upload)
  - Functional requirements (FR1, FR2, FR4, FR5)
  - Success metrics
  - User value proposition

- **UX Specification**: `docs/front-end-spec.md` (Section 4.2: Upload Screen)
  - Upload workflow wireframe
  - Validation error handling
  - Template download integration

---

## For Future Template Updates

If you need to update the template:

1. **Update Version Number**: Increment to v3.0, v3.1, etc.
2. **Document Changes**: Update this README and create review document
3. **Test Thoroughly**: Ensure all validation rules work in Excel
4. **Update Backend**: Parser may need changes if structure changes
5. **Migrate Users**: Provide clear communication about what changed
6. **Keep Old Version**: Archive previous version for reference

---

## Quick Reference: Template Columns

| Col | Field | Required | Validation | Min Length |
|-----|-------|----------|------------|------------|
| A | Lp. (Row #) | No | - | - |
| B | Nazwa Projektu | Yes* | Text length | 5 |
| C | Data rozpoczęcia | Yes* | Date DD/MM/YYYY | - |
| D | Data zakończenia | Yes* | Date DD/MM/YYYY | - |
| E | Opis projektu | Yes* | Text length | 100 |
| F | Cel projektu | Yes* | Text length | 50 |
| G | Element nowości | No | - | - |
| H | Problemy techniczne | No | - | - |
| I | Dokumentacja | No | - | - |
| J | Osoba odpowiedzialna | Yes* | - | - |

*Required fields - system will reject upload if missing or invalid

---

**Maintained by**: Product Manager
**Last Updated**: October 22, 2025
