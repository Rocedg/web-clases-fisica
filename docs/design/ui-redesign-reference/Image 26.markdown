---
name: Web Clases Rocedg
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
  on-surface-variant: '#434655'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
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
  tertiary: '#006242'
  on-tertiary: '#ffffff'
  tertiary-container: '#007d55'
  on-tertiary-container: '#bdffdb'
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
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-lg-mobile:
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
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.04em
  formula-code:
    fontFamily: JetBrains Mono
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 24px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  space-xxs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4rem
  gutter-mobile: 1rem
  gutter-desktop: 1.5rem
  container-max: 1280px
---

## Brand & Style

This design system delivers an academic, calm, and intellectually empowering digital environment tailored to Bachillerato and PAU / Selectividad students preparing for high-stakes Physics examinations in Spain. Balancing rigor with accessibility, the UI lowers cognitive anxiety while maintaining academic credibility.

The aesthetic philosophy centers on **Refined Academic Minimalism**:
- **Clarity over ornament:** Formulae, diagrams, and problem statements demand zero visual competition. Uncluttered surfaces allow complex scientific thought to breathe.
- **Supportive & modern:** Drawing from the atomic orbit emblem, the interface uses fluid transitions, soft architectural radii, and confident typographic rhythm.
- **Approachable authority:** The presence of deep navy grounding coupled with electric royal blue conveys institutional expertise without feeling clinical or cold.

## Colors

The palette is engineered for prolonged focus during revision sessions, utilizing distinct functional roles across all surfaces:

- **Primary (`#2563EB` / Active Blue):** Direct interaction focal point. Used for primary CTAs, active tab indicators, focus rings, and highlighted formula variables.
- **Secondary (`#0F172A` / Deep Space Navy):** Anchor color for high-contrast typographic hierarchy, high-level structural sidebars, and key metric counters.
- **Tertiary (`#10B981` / Emerald Mastery):** Strictly reserved for success indicators, correct solutions, mastery badges, and positive progression markers.
- **Destructive / Alert (`#EF4444` / Coral Red):** Strictly reserved for incorrect quiz choices, conceptual pitfalls, and critical deadline alerts.
- **Neutral (`#64748B` / Cool Slate):** Body copy secondary roles, problem descriptions, metadata labels, and subtle borders.
- **Canvas Base (`#F8FAFC` to `#F1F5F9`):** Light, restful backdrop that reduces ocular strain compared to pure white.
- **Interactive Light Tint (`#EFF6FF`):** Soft sky background for selected state pills, note callouts, and hover surfaces.

## Typography

Typography is set exclusively in **Plus Jakarta Sans**, chosen for its geometric foundation, tall x-height, and contemporary warmth. Numerals and superscripts remain legible even in complex mathematical expressions.

- **Headlines & Problem Titles:** Rendered in weights `700` and `800` with subtle negative tracking (`-0.02em`) to build an editorial, structured feel.
- **Body & Explanations:** Set with a generous line height (`1.625` multiplier) to facilitate sustained scanning across technical definitions and step-by-step problem derivations.
- **Mathematical Formulations & Units:** Paired with `JetBrains Mono` for code blocks, raw calculation steps, and physics parameter breakdowns (e.g., $m/s^2$, $N\cdot m$, $e^{-}$).

## Layout & Spacing

A 12-column responsive fluid grid governs desktop layouts, defaulting to single-column stacking on mobile:

- **Desktop (≥ 1024px):** 12 columns, 24px gutters, max-width container of 1280px centered on screen. Split layouts (e.g., exercise prompt on the left, interactive calculation workspace on the right) follow a 5:7 or 6:6 column balance.
- **Tablet (768px - 1023px):** 8 columns, 20px gutters, 24px outer margins.
- **Mobile (< 768px):** 4 columns, 16px gutters, 16px outer margins. Collapsible bottom sheets host formula cheatsheets and calculator popovers.

Vertical cadence relies on an 8px base grid, ensuring consistent card heights and predictable rhythm between theory paragraphs, diagram figures, and multiple-choice answer groups.

## Elevation & Depth

Visual hierarchy leverages soft, low-contrast physical tiers rather than deep drop shadows, avoiding visual heaviness:

- **Layer 0 (Canvas):** Tone `#F8FAFC`. Base canvas layer for the main viewport.
- **Layer 1 (Card & Module Surfaces):** Solid `#FFFFFF` bordered with `1px solid #E2E8F0`. Shadow is an airy, ambient drop: `0px 1px 3px rgba(15, 23, 42, 0.04), 0px 4px 12px rgba(15, 23, 42, 0.03)`.
- **Layer 2 (Active Exercise / Hover State):** Border transitions to `#CBD5E1` or `#BFDBFE`. Shadow elevates slightly: `0px 4px 16px rgba(37, 99, 235, 0.08), 0px 2px 6px rgba(15, 23, 42, 0.04)`.
- **Layer 3 (Modals, Dropdowns & Floating Formula Tools):** Solid `#FFFFFF` with `0px 12px 32px rgba(15, 23, 42, 0.1), 0px 4px 12px rgba(15, 23, 42, 0.05)` and a subtle `1px solid #CBD5E1` edge.

## Shapes

The design system employs **Level 2 Roundedness** (`0.5rem` base, `1rem` on container cards). This provides a friendly, approachable touch without sacrificing structured discipline:

- **Buttons & Form Inputs:** `0.5rem` (8px) for balanced, crisp interaction targets.
- **Cards, Panels & Exercise Boxes:** `1rem` (16px) for distinct framing of educational modules.
- **Status Pills, Topic Tags & PAU Year Badges:** Full pill radius (`9999px`) for quick visual scanning.

## Components

### Buttons
- **Primary:** Solid `#2563EB` fill, white text, 8px radius, medium weight. Subtle micro-lift on hover with `#1D4ED8`.
- **Secondary:** Surface `#FFFFFF`, border `1px solid #CBD5E1`, text `#0F172A`. On hover, background shifts to `#F8FAFC`.
- **Ghost:** Transparent background, `#2563EB` or `#64748B` text; used for non-essential navigation like "Ver pista" (Show hint).

### Cards (Exercise & Topic Cards)
- Grounded on `#FFFFFF`, framed with a `1px solid #E2E8F0` hairline border and soft Level 1 shadow.
- Header contains category metadata in `label-sm` uppercase (e.g., `CAMPO GRAVITATORIO · PAU 2024`), accompanied by difficulty and mastery status pills.

### Chips & Badges
- **Topic Badges:** Background `#EFF6FF`, text `#2563EB`, rounded full, 12px font size with `font-weight: 600`.
- **Mastery Badges:** Background `#ECFDF5`, text `#065F46`, paired with an emerald checkmark icon.

### Form Inputs & Selectors
- Background `#FFFFFF`, border `1.5px solid #E2E8F0`, interior text `#0F172A`.
- Active focus ring: `0 0 0 3px rgba(37, 99, 235, 0.15)` with border turning `#2563EB`.

### Exercise Options (Radio & Multiple Choice Cards)
- Full-width selectable cards. Neutral state: `#FFFFFF` surface with `#E2E8F0` border.
- **Selected:** Border `#2563EB`, background `#EFF6FF`.
- **Correct Submission:** Border `#10B981`, background `#ECFDF5`, text `#065F46`.
- **Incorrect Submission:** Border `#EF4444`, background `#FEF2F2`, text `#991B1B`.

### Formula Box (Physics Callout)
- Light slate tinted background (`#F8FAFC`), left accent border `3px solid #2563EB`, displaying LaTeX/Math formulas rendered via high-legibility mathematical typesetting.