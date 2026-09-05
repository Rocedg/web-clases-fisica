---
name: Web Clases Física
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#002113'
  on-tertiary-container: '#009668'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-hero-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '800'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  formula-block:
    fontFamily: JetBrains Mono
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  code-badge:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-2xs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  gutter-mobile: 1rem
  gutter-desktop: 1.5rem
  max-container: 72rem
---

## Brand & Style

This design system embodies a modern, disciplined, academic aesthetic engineered specifically for Spanish Bachillerato and Selectividad/PAU university entrance preparation. The visual posture avoids gimmicky gamification in favor of cerebral clarity, rigorous pedagogical structure, and high cognitive ergonomics. 

The emotional tone balances high-stakes academic authority with approachable, low-anxiety study efficiency. Visuals are grounded in contemporary editorial-academic design: deep institutional slates, vibrant mathematical cobalt highlights, ample structural breathing room, and ultra-crisp formula integration. The interface feels akin to an executive digital notebook paired with an advanced technical laboratory—serious, empowering, and razor-sharp.

## Colors

The color palette is built around rigorous academic contrast and functional semantic feedback:

- **Primary Canvas & Ink**: Surface background sits at ultra-clean `#F8FAFC`, stepping into pure `#FFFFFF` for working cards and exam problem blocks. Primary typography and structural headers utilize deep collegiate slate (`#0F172A` and `#1E293B`), establishing authoritative visual weight and zero glare.
- **Academic Accent**: Vibrant Cobalt (`#2563EB`, hovering to `#1D4ED8`) drives core interactions, active state tabs, step-by-step resolution toggles, and key vector highlights.
- **Pedagogical Status Roles**:
  - **Success / Mastery**: Emerald (`#10B981`) indicates validated solutions, verified formula derivations, and achieved PAU benchmarks.
  - **Notice / Hint**: Amber (`#F59E0B`) highlights common conceptual traps, units mismatch warnings, and optional hints.
  - **Error / Correction**: Rose (`#EF4444`) signals computational slips, sign inversions, or invalid physical assumptions.
- **Separators & Dividers**: Crisp, low-noise lines at `#E2E8F0` retain layout discipline without visual distraction.

## Typography

The typography strategy separates navigational leadership, long-form reading, and scientific notation:

- **Headlines (Plus Jakarta Sans)**: Offers geometric cleanliness with slightly humanist apertures, making complex scientific chapter designations and exam year headers assertive yet readable.
- **Body & Explanations (Inter)**: Deployed across all problem statements, step-by-step logic, and educational copy. Calibrated line heights (1.6x) ensure sustained reading endurance during multi-part problem solving.
- **Math & Units (JetBrains Mono & KaTeX)**: Dedicated to formula cards, constant lists, SI unit declarations, and variable definitions. All inline equations should be matched in size to adjacent Inter text, while standalone derivations render centered inside structured formula surfaces.

## Layout & Spacing

The layout is built on a responsive 12-column grid system paired with strict 8pt vertical rhythm:

- **Desktop (>= 1024px)**: 12 columns with `1.5rem` (24px) gutters, capped at a focused reading width of `72rem` (1152px) to prevent excessive line lengths during formula-heavy reading. Two-column split-views (problem statement on left, interactive scratchpad/resolution steps on right) dominate drill screens.
- **Tablet (768px - 1023px)**: 8 columns with `1.25rem` gutters. Toolbars collapse into contextual action bars.
- **Mobile (< 768px)**: 4 columns with `1rem` edge margins. Complex derivations adopt vertical cascading disclosures (accordions) to safeguard horizontal mathematical formula space without horizontal overflow clipping.

## Elevation & Depth

This design system avoids heavy shadows, simulating crisp desk paper and technical documentation:

- **Level 0 (Base Surface)**: `#F8FAFC` flat canvas for background.
- **Level 1 (Cards & Modules)**: Pure `#FFFFFF` with a crisp outline `1px solid #E2E8F0` and an imperceptible ambient shadow: `0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.03)`.
- **Level 2 (Interactive Hover & Active Drills)**: Elevated problem containers during inspection use `0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05)` with `#CBD5E1` border highlighting.
- **Level 3 (Modals & Formula Tooltips)**: Focused reference popovers receive `0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04)` over a subtle `rgba(15, 23, 42, 0.4)` backdrop blur.

## Shapes

The design system maintains a refined, tight corner radius (Soft / 0.25rem to 0.5rem) to reinforce academic precision and institutional structure:

- Inputs, formula codeboxes, and standard buttons employ `0.375rem` (6px).
- Exercise cards, theory callouts, and layout modals scale up to `0.5rem` (8px).
- Pill formats are strictly reserved for categorical metadata tags (e.g., "PAU Madrid 2023", "Campo Gravitatorio", "Opción A") using `9999px` corner radius.

## Components

### Buttons
- **Primary Action**: Solid `#2563EB` fill, white text, 0.375rem radius, font weight 600. On hover: `#1D4ED8`. Active: subtle inset press (`transform: translateY(1px)`).
- **Secondary (Step Navigation / Reveal)**: `#FFFFFF` fill with `1px solid #E2E8F0`, `#1E293B` text. On hover: `#F1F5F9` surface with `#CBD5E1` border.
- **Ghost / Formula Tools**: Transparent background, `#64748B` text, hover background `#F1F5F9`.

### Chips & Badges
- **PAU Exam Tag**: Monospace badge (`JetBrains Mono`, 11px), solid `#0F172A` background with white text for official exam year references.
- **Topic Chips**: Tinted background (`#EFF6FF` for electromagnetism, `#ECFDF5` for thermodynamics) with bold color-matched text and `9999px` full-pill radius.

### Cards (Exercise & Theory)
- **Problem Statement Card**: Clean white container, `1px solid #E2E8F0`, `0.5rem` radius. Header carries exam origin chip and point score badge (e.g., "2.5 Pts"). 
- **Solution Step Card**: Indented container with left accent border (`3px solid #2563EB`), displaying the specific physics formula, substituted variables, and final boxed result.

### Inputs & Math Answer Drills
- **Numeric & Unit Fields**: Structured text input with fixed right-hand suffix container for scientific units (e.g., `m/s²`, `N·m`, `eV`). Border turns `#2563EB` with `0 0 0 3px rgba(37, 99, 235, 0.15)` on focus. Error state switches border to `#EF4444`.

### Checkboxes & Radios
- Square with 4px corner radius for multiple-choice options. Selected state displays crisp solid cobalt `#2563EB` with white internal glyph. Border sits at 1.5px thickness.

### Callout Containers (Pedagogical Guidance)
- **"Ojo con las unidades" (Warning)**: Light amber container (`#FFFBEB`), amber border (`#FDE68A`), left edge indicator (`#F59E0B`), containing common conversion pitfalls.
- **"Pista teórica" (Hint Accordion)**: Soft slate tint (`#F8FAFC`) with collapsible icon disclosure for guided self-correction.