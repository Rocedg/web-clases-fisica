---
name: Academic Modernism
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434655'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#006329'
  on-tertiary: '#ffffff'
  tertiary-container: '#007f36'
  on-tertiary-container: '#c7ffca'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#7ffc97'
  tertiary-fixed-dim: '#62df7d'
  on-tertiary-fixed: '#002109'
  on-tertiary-fixed-variant: '#005320'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 44px
    fontWeight: '700'
    lineHeight: 52px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  formula-display:
    fontFamily: Plus Jakarta Sans
    fontSize: 19px
    fontWeight: '500'
    lineHeight: 32px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  space-2xs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4rem
  container-max: 72rem
  gutter-mobile: 1rem
  gutter-desktop: 1.5rem
---

## Brand & Style

This design system embodies a calm, precise, and encouraging educational environment tailored for high school physics students preparing for high-stakes university entrance exams (PAU/Selectividad). Inspired by atomic orbital trajectories and clear scientific notation, the aesthetic sits at the intersection of **Minimalism** and **Modern Corporate/Academic Design**.

The interface eliminates visual friction, digital clutter, and anxiety-inducing score dashboards. Instead, it prioritizes pure focus, legible mathematical formatting, and serene spatial balance. It conveys deep pedagogical competence, precision, and approachability. Every view gives the student a sense of orderly progression, luminous clarity, and intellectual calm.

## Colors

The color palette centers on high-clarity blues derived directly from the atomic orbital motif in the reference identity, set against expansive, soothing light canvases.

- **Primary (`#2563EB`)**: An energetic scientific blue used for key calls to action, active navigation states, problem selector markers, and focal interactive elements. Its pressed/hover variant deepens to `#1D4ED8`.
- **Secondary (`#0F172A`)**: Deep slate blue-black serving as the bedrock for typography, formula displays, and high-emphasis interface chrome. It provides superior contrast without the harshness of pure black.
- **Surface & Background (`#F8FAFC` & `#FFFFFF`)**: The global page canvas uses `#F8FAFC` (soft cool-slate tint), while instructional surfaces, problem statements, and cards use pure `#FFFFFF`.
- **Structural Neutral Borders (`#E2E8F0` and `#CBD5E1`)**: Subtle hairline separators establishing containment without visual noise.
- **Functional Semantics**:
  - **Success / Mastery (`#16A34A` with `#DCFCE7` tint)**: Reserved strictly for validated physics steps, correct solutions, and progress achievements.
  - **Error / Review Required (`#DC2626` with `#FEE2E2` tint)**: Gentle yet unequivocal red for calculation errors, formula misconceptions, and critical exam cautions.
  - **Guidance / Note (`#D97706` with `#FEF3C7` tint)**: Subdued amber for hints, theorem callouts, and exam tips.

## Typography

Plus Jakarta Sans provides geometric balance with warm, open letterforms that remain exceptionally legible through complex mathematical and physical statements.

- **Headlines**: Weighted at SemiBold (600) and Bold (700) with slight negative tracking (`-0.01em` to `-0.02em`) to deliver confident, academic authority without stiffness.
- **Body & Problem Statements**: Set with generous line-heights (`1.6` to `1.65`) to ensure students can digest complex word problems and derivation steps effortlessly.
- **Scientific Figures & Formulas**: When rendering inline math, units (e.g., $m/s^2$, $N\cdot m$), or KaTeX/LaTeX blocks, rely on proportional figure spacing (`font-variant-numeric: tabular-nums`) to align calculations vertically.

## Layout & Spacing

The layout is built on a 12-column responsive grid system optimized for concentrated reading and step-by-step problem resolution.

- **Rhythm & Structure**: Rooted in an 8pt base grid (`0.5rem`, `1rem`, `1.5rem`, `2rem`, `3rem`).
- **Content Max-Width**: Learning materials, exercise cards, and theory modules sit inside a constrained maximum width (`72rem` / 1152px) to prevent eye fatigue across expansive displays. Reading blocks are capped at `42rem` (~68 characters per line).
- **Responsive Adaptations**:
  - **Mobile (< 640px)**: Single column with `1rem` safe margins; exercise actions lock to sticky bottom sheets for one-handed operation.
  - **Tablet (640px - 1024px)**: 8-column layout with `1.25rem` gutters; navigation collapses to a clean top app bar.
  - **Desktop (1024px+)**: 12-column layout with dual-pane flexibility: syllabus/index on the left (3 cols), problem solving and formula workspace in the center/right (9 cols).

## Elevation & Depth

This system avoids dark, heavy skeuomorphism and floating layered shadows. Depth is achieved primarily through pure white surfaces grounded on the pale `#F8FAFC` background, framed by micro-borders and delicate, tinted light dispersion.

- **Level 0 (Canvas)**: Background canvas `#F8FAFC`. Completely flat.
- **Level 1 (Default Cards & Blocks)**: Pure white background `#FFFFFF`, border `1px solid #E2E8F0`, with shadow `0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.03)`.
- **Level 2 (Hover State / Interactive Cards)**: Border shifts to `#CBD5E1`, shadow transitions to `0 4px 12px -2px rgba(37, 99, 235, 0.08), 0 2px 6px -2px rgba(15, 23, 42, 0.04)`.
- **Level 3 (Modals / Equation Drawers / Dropdowns)**: White surface, border `1px solid #E2E8F0`, shadow `0 12px 28px -4px rgba(15, 23, 42, 0.08), 0 4px 8px -2px rgba(15, 23, 42, 0.04)`.

## Shapes

The design uses balanced, modern rounded geometry (Level 2) reflecting the soft curves of atomic electron shells from the brand icon.

- **Standard Elements (Buttons, Inputs, Selectors)**: `rounded-md` (0.5rem / 8px) to establish clean, stable interfaces.
- **Containers (Exercise Cards, Callouts, Panels)**: `rounded-xl` (0.75rem / 12px to 1rem / 16px) for approachable containment that does not feel boxy.
- **Tags, Indicators & Filter Pills**: Fully rounded pill shapes (`9999px`) for exam year tags (e.g., "PAU 2024"), subject categories ("Cinemática", "Electromagnetismo"), and status markers.

## Components

### Buttons
- **Primary**: Solid `#2563EB` background, white label, `0.5rem` radius, subtle focus ring `0 0 0 3px rgba(37, 99, 235, 0.25)`. Hover background `#1D4ED8`.
- **Secondary**: Pure `#FFFFFF` background, `1px solid #E2E8F0`, text `#0F172A`. Hover background `#F8FAFC` and border `#CBD5E1`.
- **Ghost/Tertiary**: Transparent background, text `#2563EB`, hover background `#EFF6FF`.

### Cards & Problem Panels
- Pristine `#FFFFFF` surfaces with `1px solid #E2E8F0` border and Level 1 elevation.
- Problem header features metadata chips (topic, PAU call/year, difficulty) followed by an unencumbered, high-contrast exercise statement.

### Inputs & Math Formula Inputs
- Background `#FFFFFF`, border `1px solid #CBD5E1`, internal padding `0.625rem 0.875rem`, text `#0F172A`.
- Active focus state applies `#2563EB` border and an ambient `3px` outer ring in `#DBEAFE`.

### Chips & Badges
- **Topic Chips**: Background `#EFF6FF`, text `#1D4ED8`, border `1px solid #DBEAFE`, pill radius.
- **Success Chips**: Background `#DCFCE7`, text `#15803D`, border `1px solid #BBF7D0`.
- **Alert/Caution Chips**: Background `#FEE2E2`, text `#B91C1C`, border `1px solid #FECACA`.

### Checkboxes & Multiple Choice Option Cards
- Options are styled as full-width interactive cards with `1px solid #E2E8F0`.
- On selection, border transitions to `#2563EB`, background shifts to `#EFF6FF`, and radio/checkbox glyph fills with `#2563EB`.

### Specialized Academic Components
- **Step-by-Step Solution Accordion**: Segmented panels with subtle vertical timeline indicators linking the initial hypothesis, free-body diagram, mathematical deduction, and numerical result.
- **Formula Callout Box**: Border-left `3px solid #2563EB`, background `#F8FAFC`, providing clear visual isolation for fundamental laws (e.g., Newton's laws, Maxwell equations).