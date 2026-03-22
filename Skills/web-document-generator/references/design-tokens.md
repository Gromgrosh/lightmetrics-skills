# Design Tokens — Light Spectrum

Design tokens for Lightmetrics web documents. Based on the Light Spectrum design system.

## Responsive Breakpoints

| Breakpoint | Width | Usage |
|------------|-------|-------|
| Mobile | < 640px | Phone portrait/landscape |
| Tablet | 640px - 1023px | Tablet, small laptop |
| Desktop | 1024px - 1199px | Standard desktop |
| Large Desktop | >= 1200px | Wide screens, sidebar visible |

```css
/* Mobile first approach */
@media (min-width: 640px)  { /* Tablet+ */ }
@media (min-width: 1024px) { /* Desktop+ */ }
@media (min-width: 1200px) { /* Large Desktop+ with sidebar */ }
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

Typography uses CSS `clamp()` for smooth scaling between 320px and 1440px viewports.

| Token | Mobile | Desktop | Formula |
|-------|--------|---------|---------|
| `--font-size-display` | 32px | 50px | `clamp(31.93px, calc(26.72px + 1.628vw), 50.16px)` |
| `--font-size-h1` | 28px | 42px | `clamp(28.38px, calc(24.55px + 1.198vw), 41.8px)` |
| `--font-size-h2` | 25px | 35px | `clamp(25.23px, calc(22.48px + 0.858vw), 34.84px)` |
| `--font-size-h3` | 22px | 29px | `clamp(22.43px, calc(20.54px + 0.589vw), 29.03px)` |
| `--font-size-h4` | 20px | 24px | `clamp(19.93px, calc(18.71px + 0.380vw), 24.19px)` |
| `--font-size-h5` | 18px | 20px | `clamp(17.72px, calc(17.02px + 0.218vw), 20.16px)` |
| `--font-size-h6` | 16px | 17px | `clamp(15.75px, calc(15.45px + 0.094vw), 16.8px)` |
| `--font-size-text-large` | 16px | 17px | `clamp(15.75px, calc(15.45px + 0.094vw), 16.8px)` |
| `--font-size-text-main` | 14px | 14px | Fixed (no scaling) |
| `--font-size-text-small` | 12px | 12px | `clamp(11.67px, calc(11.45px + 0.069vw), 12.44px)` |
| `--font-size-caption` | 10px | 11px | `clamp(9.72px, calc(9.34px + 0.120vw), 11.06px)` |

### Line Heights (Unitless)

Using unitless values for proper scaling with fluid fonts:

| Token | Value | Usage |
|-------|-------|-------|
| `--line-height-display` | 1.2 | Display headings |
| `--line-height-h1` | 1.2 | H1 headings |
| `--line-height-h2` | 1.25 | H2 headings |
| `--line-height-h3` | 1.3 | H3 headings |
| `--line-height-h4` | 1.35 | H4 headings |
| `--line-height-h5` | 1.4 | H5 headings |
| `--line-height-h6` | 1.45 | H6 headings |
| `--line-height-text` | 1.6 | Body text, paragraphs |

### Letter Spacing (em units)

Using `em` units for proportional scaling with font size:

| Token | Value | Usage |
|-------|-------|-------|
| `--letter-spacing-display` | -0.04em | Display text (tight) |
| `--letter-spacing-h1` | -0.025em | H1 headings |
| `--letter-spacing-h2` | -0.02em | H2 headings |
| `--letter-spacing-h3` | -0.01em | H3 headings |
| `--letter-spacing-text` | 0 | Body text |

---

## Colors

### Base Colors
```css
--color-white: #FFFFFF;
--color-black: #000000;
```

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

## Spacing

Based on 4px grid:

| Token | Value | Usage |
|-------|-------|-------|
| `--space-0` | 0px | None |
| `--space-0-5` | 2px | Hairline |
| `--space-1` | 4px | Tight |
| `--space-2` | 8px | Compact |
| `--space-3` | 12px | Snug |
| `--space-4` | 16px | Default |
| `--space-5` | 20px | Comfortable |
| `--space-6` | 24px | Relaxed |
| `--space-8` | 32px | Loose |
| `--space-10` | 40px | Section |
| `--space-12` | 48px | Large section |
| `--space-16` | 64px | Page section |
| `--space-20` | 80px | Major section |
| `--space-24` | 96px | Hero spacing |

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

## Theme Variables

### Light Mode (Default)
```css
--theme-background: var(--color-shark-50);    /* #F5F5F5 */
--theme-text: var(--color-shark-950);          /* #212121 */
--theme-subtext: var(--color-shark-600);       /* #5E5B5A */
--theme-border: var(--color-shark-200);        /* #D2D1D0 */
--theme-hover: var(--color-shark-50);          /* #F5F5F5 */
--theme-brand: var(--color-plum-800);          /* #8B2682 */
```

### Callout Colors
```css
/* Warning */
--callout-warning-bg: #FFFBEB;
--callout-warning-border: #FCD34D;
--callout-warning-text: #92400E;

/* Info */
--callout-info-bg: #EFF6FF;
--callout-info-border: #BFDBFE;
--callout-info-text: #1E40AF;

/* Conditional/Special */
--callout-conditional-bg: #FDF4FF;
--callout-conditional-border: #D8B4FE;
--callout-conditional-text: #6B21A8;

/* Success */
--callout-success-bg: #F0FDF4;
--callout-success-border: #86EFAC;
--callout-success-text: #166534;
```

---

## Document Layout

### Dimensions
```css
--sidebar-width: 260px;
--header-height: 64px;
--content-max-width: 900px;
```

### Responsive Breakpoints
```css
/* Mobile first */
@media (min-width: 640px)  { /* Tablet */ }
@media (min-width: 768px)  { /* Small desktop */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1200px) { /* Large desktop - sidebar visible */ }
```

---

## Usage Examples

### Apply to HTML Document
```html
<style>
:root {
  /* Import all tokens here */
  --color-plum-800: #8B2682;
  /* ... */
}

body {
  font-family: var(--font-family-primary);
  background: var(--theme-background);
  color: var(--theme-text);
  line-height: 1.6;
}

h1 {
  font-size: var(--font-size-h1);
  font-weight: var(--font-weight-medium);
  letter-spacing: var(--letter-spacing-h1);
  color: var(--theme-text);
}

.brand-accent {
  color: var(--theme-brand);
}

.card {
  background: var(--color-white);
  border: 1px solid var(--theme-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
}
</style>
```

### Complete CSS Import
See `assets/base-styles.css` for a complete stylesheet with all tokens applied.
