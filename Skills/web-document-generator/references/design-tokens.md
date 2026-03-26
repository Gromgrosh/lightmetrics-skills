# Design Tokens — LightSpectrum

All design tokens for web document templates are sourced from the **LightSpectrum Design System**.

## Authoritative Source

```
projects/Lightmetrics/paper-setup/lightspectrum.css
```

The `assets/base-styles.css` in this skill embeds all LightSpectrum tokens. Any token updates must be synced from the source file.

---

## Quick Reference

### Responsive Breakpoints

| Breakpoint | Width | Usage |
|------------|-------|-------|
| Mobile | < 640px | Single column, hamburger nav |
| Tablet | 640px - 1199px | Full header, hamburger nav, panel from right |
| Desktop | >= 1200px | Full header, sidebar always visible on left |

```css
/* Mobile first approach */
@media (min-width: 640px)  { /* Tablet+ */ }
@media (min-width: 1200px) { /* Desktop+ with sidebar */ }
```

---

## Theme Switching

Use `data-theme` attribute on `<body>` or `<html>`:

| Theme | Value | Brand Color |
|-------|-------|-------------|
| Light (default) | `light` | Plum (#8B2682) |
| Dark | `dark` | Plum light (#C356BC) |
| Secondary | `secondary` | Eastern Blue (#2898A2) |
| Secondary Dark | `secondary-dark` | Eastern Blue light (#45C9CB) |

```html
<body data-theme="light">       <!-- Primary/Plum theme (default) -->
<body data-theme="dark">        <!-- Primary dark mode -->
<body data-theme="secondary">   <!-- Eastern Blue theme -->
<body data-theme="secondary-dark"> <!-- Eastern Blue dark mode -->
```

---

## Color Palettes

### Primary Brand — Plum

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-plum-50` | #FDF5FE | Lightest tint |
| `--color-plum-100` | #FCEAFE | Light backgrounds |
| `--color-plum-200` | #F5D4FA | Hover states |
| `--color-plum-300` | #F4B5F2 | Borders |
| `--color-plum-400` | #ED85EA | Accents |
| `--color-plum-500` | #DF56DA | Mid-tone |
| `--color-plum-600` | #C356BC | Dark accents |
| `--color-plum-700` | #A12A97 | Strong accents |
| `--color-plum-800` | #8B2682 | **Main brand color** |
| `--color-plum-900` | #6C1964 | Dark variant |
| `--color-plum-950` | #470B40 | Darkest |

### Secondary — Eastern Blue

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-eastern-blue-50` | #EFFCFC | Lightest tint |
| `--color-eastern-blue-100` | #D7F6F6 | Light backgrounds |
| `--color-eastern-blue-200` | #B4EDED | Hover states |
| `--color-eastern-blue-300` | #80E0E0 | Mid-tone |
| `--color-eastern-blue-400` | #45C9CB | Accents |
| `--color-eastern-blue-500` | #29ACB1 | Strong accents |
| `--color-eastern-blue-600` | #2898A2 | **Secondary brand** |
| `--color-eastern-blue-700` | #24717A | Dark variant |
| `--color-eastern-blue-800` | #255D65 | Darker |
| `--color-eastern-blue-900` | #234E56 | Dark |
| `--color-eastern-blue-950` | #123339 | Darkest |

### Neutral — Shark

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-shark-50` | #F5F5F5 | Page background |
| `--color-shark-100` | #E9E8E8 | Card backgrounds |
| `--color-shark-200` | #D2D1D0 | Borders |
| `--color-shark-300` | #B2B0AE | Disabled text |
| `--color-shark-400` | #8A8785 | Placeholder text |
| `--color-shark-500` | #706D6B | Secondary text |
| `--color-shark-600` | #5E5B5A | Subtext |
| `--color-shark-700` | #514E4D | Strong secondary |
| `--color-shark-800` | #464443 | Dark UI |
| `--color-shark-900` | #3E3C3C | Darker UI |
| `--color-shark-950` | #212121 | **Primary text** |

### Status Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-success-50` | #DCF9F0 | Success background |
| `--color-success-500` | #0C9C71 | Success text/icons |
| `--color-warning-50` | #FBF6EF | Warning background |
| `--color-warning-500` | #D38B43 | Warning text/icons |
| `--color-error-50` | #FAE6E6 | Error background |
| `--color-error-500` | #D34343 | Error text/icons |

---

## Semantic Theme Variables

Use these instead of raw palette colors for automatic theme support:

```css
--theme-background    /* Page background */
--theme-surface       /* Card/panel background */
--theme-text          /* Primary text */
--theme-subtext       /* Secondary text */
--theme-muted         /* Tertiary/placeholder text */
--theme-border        /* Standard borders */
--theme-border-light  /* Subtle borders */
--theme-hover         /* Hover state backgrounds */
--theme-brand         /* Brand accent color */
--theme-brand-light   /* Brand tint for backgrounds */
--theme-brand-text    /* Text on brand backgrounds */
```

---

## Brand Swatch System

The brand swatch provides consistent brand color variations across themes:

```css
/* Primary (Plum) Light Mode */
--brand-swatch-primary-color: #8B2682
--brand-swatch-primary-variant-medium: #DF56DA
--brand-swatch-primary-variant-dark: #470B40
--brand-swatch-primary-variant-light: #FCEAFE
--brand-swatch-primary-text: #FFFFFF

/* Primary (Plum) Dark Mode — inverted */
--brand-swatch-primary-dark-color: #C356BC
--brand-swatch-primary-dark-variant-dark: #FCEAFE
--brand-swatch-primary-dark-variant-light: #470B40

/* Secondary (Eastern Blue) Light Mode */
--brand-swatch-secondary-color: #2898A2
--brand-swatch-secondary-variant-medium: #80E0E0
--brand-swatch-secondary-variant-dark: #123339
--brand-swatch-secondary-variant-light: #EFFCFC

/* Secondary (Eastern Blue) Dark Mode — inverted */
--brand-swatch-secondary-dark-color: #45C9CB
```

---

## Typography

### Font Family

```css
--font-family-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--font-weight-regular` | 400 | Body text |
| `--font-weight-medium` | 500 | Emphasis, labels |
| `--font-weight-semibold` | 600 | Sub-headings, badges |
| `--font-weight-bold` | 700 | Headings, strong emphasis |

### Fluid Font Sizes

**Always use fluid tokens for web** — they scale smoothly between 320px and 1440px viewports:

| Token | Mobile | Desktop |
|-------|--------|---------|
| `--font-size-display` | 32px | 50px |
| `--font-size-h1` | 28px | 42px |
| `--font-size-h2` | 25px | 35px |
| `--font-size-h3` | 22px | 29px |
| `--font-size-h4` | 20px | 24px |
| `--font-size-h5` | 18px | 20px |
| `--font-size-h6` | 16px | 17px |
| `--font-size-text-large` | 16px | 17px |
| `--font-size-text-main` | 14px | 14px (fixed) |
| `--font-size-text-small` | 12px | 12px |
| `--font-size-caption` | 10px | 11px |

Static `-min`/`-max` variants are available for print/email/JS interpolation only.

### Line Heights

| Token | Value |
|-------|-------|
| `--line-height-display` | 1.2 |
| `--line-height-h1` | 1.2 |
| `--line-height-h2` | 1.25 |
| `--line-height-h3` | 1.3 |
| `--line-height-h4` | 1.35 |
| `--line-height-h5` | 1.4 |
| `--line-height-h6` | 1.45 |
| `--line-height-text` | 1.6 |

### Letter Spacing

| Token | Value |
|-------|-------|
| `--letter-spacing-display` | -0.04em |
| `--letter-spacing-h1` | -0.025em |
| `--letter-spacing-h2` | -0.02em |
| `--letter-spacing-h3` | -0.01em |
| `--letter-spacing-h4` to `--letter-spacing-text` | 0 |

---

## Spacing

Based on 4px grid:

| Token | Value |
|-------|-------|
| `--space-0` | 0px |
| `--space-0-5` | 2px |
| `--space-1` | 4px |
| `--space-2` | 8px |
| `--space-3` | 12px |
| `--space-4` | 16px |
| `--space-5` | 20px |
| `--space-6` | 24px |
| `--space-8` | 32px |
| `--space-10` | 40px |
| `--space-12` | 48px |
| `--space-16` | 64px |
| `--space-20` | 80px |
| `--space-24` | 96px |
| `--space-32` | 128px |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | 0px | Sharp corners |
| `--radius-sm` | 2px | Subtle rounding |
| `--radius-default` | 4px | Default |
| `--radius-md` | 6px | Cards |
| `--radius-lg` | 8px | Larger cards |
| `--radius-xl` | 12px | Panels |
| `--radius-2xl` | 16px | Large panels |
| `--radius-3xl` | 24px | Hero elements |
| `--radius-full` | 9999px | Pills, avatars |

---

## Document Layout

```css
--sidebar-w: 260px
--header-h: 64px
--content-max: 900px
```

---

## Callout Colors

```css
/* Warning */
--warning-bg: #FFFBEB
--warning-border: #FCD34D
--warning-txt: #92400E

/* Info */
--info-bg: #EFF6FF
--info-border: #BFDBFE
--info-txt: #1E40AF

/* Conditional/Special */
--cond-bg: #FDF4FF
--cond-border: #D8B4FE
--cond-txt: #6B21A8

/* Success */
--success-bg: #F0FDF4
--success-border: #86EFAC
--success-txt: #166534
```

---

## Usage Example

```html
<style>
  /* All tokens are embedded in base-styles.css */

  .my-card {
    background: var(--theme-surface);
    border: 1px solid var(--theme-border);
    border-radius: var(--radius-lg);
    padding: var(--space-6);
  }

  .my-heading {
    font-size: var(--font-size-h2);
    font-weight: var(--font-weight-semibold);
    color: var(--theme-text);
  }

  .my-accent {
    color: var(--theme-brand);
  }
</style>
```

---

## Syncing Tokens

When LightSpectrum is updated, sync to this skill:

1. Read updated `projects/Lightmetrics/paper-setup/lightspectrum.css`
2. Update token definitions in `assets/base-styles.css`
3. Keep component styles (header, sidebar, etc.) unchanged
4. Test with all four themes: light, dark, secondary, secondary-dark
