# Common Template Specification

This document defines the common patterns and behaviors that apply to **all** document templates (installation guide, product spec, process workflow, technical manual).

---

## 1. Header

The header is fixed at the top and adapts based on viewport.

### 1.1 Desktop (≥1200px)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ [Logo]  |  Document Name                                    [English ▼] │
│              Platform/App Name                                          │
└──────────────────────────────────────────────────────────────────────────┘
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ← Progress bar (fixed, below header)
```

**Elements:**
- **Logo**: Lightmetrics logo, left-aligned
- **Divider**: Vertical 1px line separating logo from text
- **Document Name**: Semibold, primary text color (e.g., "Installer Guide")
- **Platform/App Name**: Small, muted text below document name (e.g., "RideView Companion App")
- **Language Dropdown**: Right-aligned (far right edge of header)
- **Progress Bar**: Separate fixed element positioned directly below the header (`top: var(--header-h)`), spans full width, shows page scroll progress

**Hamburger Menu**: Hidden on desktop (sidebar is always visible)

### 1.2 Tablet (640px – 1199px)

```
┌─────────────────────────────────────────────────────────────────┐
│ [Logo]  |  Document Name                     [English ▼]  [☰]  │
│              Platform/App Name                                  │
└─────────────────────────────────────────────────────────────────┘
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ← Progress bar (fixed, below header)
```

**Elements:**
- Same as desktop except:
- **Hamburger Menu**: Visible to the right of language dropdown
- **Progress Bar**: Separate fixed element below header

### 1.3 Mobile (<640px)

```
┌───────────────────────────────────────┐
│ [Logo]              [English ▼]  [☰] │
└───────────────────────────────────────┘
▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ← Progress bar (fixed, below header)
```

**Elements:**
- **Logo**: Left-aligned only (no document name text)
- **Language Dropdown**: Compact, right side
- **Hamburger Menu**: To the right of language dropdown
- **Progress Bar**: Separate fixed element below header

---

## 2. Side Panel (Navigation Index)

The side panel serves as a table of contents / index for the document.

### 2.1 Desktop (≥1200px)

**Position**: Fixed on the **left** side, below header
**State**: Always visible, cannot be closed
**Close Icon**: Hidden

```
┌───────────────────────────┐
│ INSTALLATION STEPS        │
├───────────────────────────┤
│ ① Unboxing               │
│   5 sub-steps             │
│                           │
│ ② Provisioning           │
│   1 sub-step              │
│                           │
│ ③ Check Network          │
│   3 sub-steps             │
│                           │
│ ④ Diagnostics            │
│   1 sub-step              │
│                           │
│ ⑤ General Settings       │
│   5 sub-steps             │
│                           │
│ ⑥ Mounting               │
│   8 sub-steps             │
│                           │
│ ⑦ External Camera        │
│   Conditional step        │
│                           │
│ ⑧ Complete Installation  │
│   Final step              │
├───────────────────────────┤
│ ↑ Back to top            │
│                           │
│ Last updated: Mar 2026    │
└───────────────────────────┘
```

**Structure per item:**
1. **Serial Number**: Circled number badge (1-N)
2. **Section Name**: Medium weight, primary color, clickable
3. **Description**: Small text, muted color (1-2 lines max)
   - Examples: "5 sub-steps", "Conditional step", "Final step"

**Footer:**
- "Back to top" link
- Document update/creation date

### 2.2 Tablet (640px – 1199px)

**Position**: Slides in from the **right**
**State**: Hidden by default
**Trigger**: Hamburger menu icon in header
**Animation**:
1. User taps hamburger → icon animates to "X" (close)
2. Side panel slides in from right
3. User taps X → icon animates back to hamburger
4. Side panel slides out to the right

```
Header: [...content...]  [English ▼]  [X]
                                        ┌───────────────────────────┐
                                        │ INSTALLATION STEPS     ✕  │
                                        ├───────────────────────────┤
                                        │ ① Unboxing               │
                                        │   5 sub-steps             │
                                        │ ...                       │
                                        └───────────────────────────┘
```

**Overlay**: Semi-transparent dark overlay covers content when panel is open

### 2.3 Mobile (<640px)

Same as tablet behavior.

---

## 3. Hero Section

The hero introduces the document with minimal content.

### Structure

```
┌─────────────────────────────────────────────────────────────┐
│ RIDEVIEW COMPANION APP          ← Platform/Eyebrow         │
│                                                             │
│ Guide to using the              ← Title (H1)               │
│ Installer Workflow                                          │
│                                                             │
│ A step-by-step guide for field  ← Description              │
│ installers on how to use the                                │
│ RideView companion app to                                   │
│ complete the installer workflow.                            │
│                                                             │
│─────────────────────────────────────────────────────────────│ ← Divider
└─────────────────────────────────────────────────────────────┘
```

**Elements (in order):**
1. **Platform/Eyebrow**: Uppercase, small, accent color (e.g., teal/eastern blue)
2. **Title**: Large, bold heading
3. **Description**: Paragraph, subtext color

**Removed elements:**
- Prerequisite chips (not shown in hero)
- Time estimate chips

---

## 4. Content Structure

### 4.1 Step Section

Each major section has the following structure:

```
┌─────────────────────────────────────────────────────────────┐
│ ┌─────────┐                                                 │
│ │ Step 1  │  ← Step Badge (pill)                           │
│ └─────────┘                                                 │
│                                                             │
│ Unboxing                        ← Step Title (H2)          │
│ STEP 01/07                      ← Step Indicator (optional)│
│                                                             │
│ Get the device unboxed, powered ← Purpose/Description      │
│ up, and ready for installation.                             │
└─────────────────────────────────────────────────────────────┘
```

**Step indicator**: Can be hidden, shown, or display contextual info (like "Conditional")

### 4.2 Subsection Content

Each subsection within a step:

```
┌─────────────────────────────────────────────────────────────┐
│ ┌─────┐                                                     │
│ │ 1.0 │  Pre-Installation Setup   ← Subsection badge + title│
│ └─────┘                                                     │
│                                                             │
│ 1. From the Home screen, tap Installation.                  │
│ 2. Select your dash cam vendor from the list.               │
│ 3. Tap the tile for the specific dash cam model.            │
│ 4. Review the overview screen for dash cam installation.    │
│                                                             │
│ ┌───────────────────────────────────────────────────────┐   │
│ │                                                       │   │
│ │              [Screenshot Image]                       │   │
│ │           (light background tint)                     │   │
│ │                                                       │   │
│ └───────────────────────────────────────────────────────┘   │
│                                                             │
│ Additional instructions can follow the image.               │
└─────────────────────────────────────────────────────────────┘
```

**Subsection elements:**
1. **Badge**: Circular/pill with subsection number (e.g., "1.0", "1.1")
2. **Title**: Subsection heading
3. **Instructions**: Numbered or bulleted list
4. **Image**: In container with light background tint

### 4.3 Image Containers

Images are displayed in containers with specific styling:

```css
/* Image container specifications */
.image-container {
  background: var(--theme-brand-light);  /* Light tint background */
  border-radius: var(--radius-xl);
  padding: var(--space-4);
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-container img {
  max-width: 100%;
  height: auto;
  /* NO cursor: zoom-in */
  /* NO click interaction */
}
```

**Image Rules:**
- **Background**: Light tint (brand-light color)
- **Positioning**: Centered within container
- **Size**: As large as possible while maintaining aspect ratio
- **Interaction**: NOT clickable, no zoom functionality
- **Order**: Instructions can come before OR after images

---

## 5. Responsive Breakpoints

| Breakpoint | Range | Layout |
|------------|-------|--------|
| Mobile | < 640px | Single column, hamburger nav, panel from right |
| Tablet | 640px – 1199px | Full header, hamburger nav, panel from right |
| Desktop | ≥ 1200px | Full header, sidebar always visible on left |

---

## 6. Progress Bar Implementation

The progress bar shows scroll position through the document. It is a **separate fixed element** positioned directly below the header (not inside it).

```html
<!-- Progress bar placed OUTSIDE and BEFORE the header in DOM -->
<div class="scroll-progress">
  <div class="scroll-bar" id="scrollBar"></div>
</div>

<header class="site-header">
  <!-- header content -->
</header>
```

```css
.scroll-progress {
  position: fixed;
  top: var(--header-h);  /* Positioned directly below header */
  left: 0;
  right: 0;
  height: 3px;
  background: var(--theme-border-light);
  z-index: 99;
}

.scroll-bar {
  height: 100%;
  background: var(--theme-brand);
  width: 0%;
  transition: width 0.1s;
}
```

```javascript
window.addEventListener('scroll', () => {
  const el = document.documentElement;
  const pct = (el.scrollTop / (el.scrollHeight - el.clientHeight)) * 100;
  document.getElementById('scrollBar').style.width = pct + '%';
});
```

---

## 7. Side Panel Animation (Tablet/Mobile)

```css
/* Panel slides from right */
.sidebar {
  position: fixed;
  top: var(--header-h);
  right: 0;  /* Changed from left: 0 */
  bottom: 0;
  transform: translateX(100%);  /* Hidden to right */
  transition: transform 0.25s ease;
}

.sidebar.open {
  transform: translateX(0);
}

/* Hamburger to X animation */
.hamburger span {
  transition: transform 0.2s, opacity 0.2s;
}

.hamburger.open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.hamburger.open span:nth-child(2) {
  opacity: 0;
}

.hamburger.open span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}
```

---

## 8. HTML Structure Reference

### Complete Header

```html
<!-- Scroll Progress (separate fixed element, placed before header in DOM) -->
<div class="scroll-progress">
  <div class="scroll-bar" id="scrollBar"></div>
</div>

<!-- Header -->
<header class="site-header">
  <div class="site-header__brand">
    <img src="./assets/lightmetrics-logo.svg" alt="Lightmetrics" class="brand-logo-img" />
    <span class="brand-divider"></span>
    <span class="brand-text">
      <span class="brand-name">[Document Name]</span>
      <span class="brand-sub">[Platform/App Name]</span>
    </span>
  </div>

  <div class="header-right">
    <div class="lang-selector">
      <select class="lang-selector__dropdown" id="langSelect">
        <option value="en">English</option>
        <option value="pt">Português</option>
      </select>
    </div>

    <button class="hamburger" id="menuToggle" aria-label="Toggle menu">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </div>
</header>
```

### Complete Side Panel

```html
<div class="sidebar-overlay" id="sidebarOverlay"></div>

<aside class="sidebar" id="sidebar">
  <div class="sidebar__head">
    <span>[SECTION TITLE]</span>
    <button class="sidebar__close" id="sidebarClose" aria-label="Close menu">✕</button>
  </div>

  <ul class="sidebar__list">
    <li>
      <a href="#step-1" class="sidebar__link">
        <span class="sidebar__num">1</span>
        <span class="sidebar__text">
          <span class="sidebar__step-title">[Section Name]</span>
          <span class="sidebar__subtitle">[Description: e.g., "5 sub-steps"]</span>
        </span>
      </a>
    </li>
    <!-- Repeat for each section -->
  </ul>

  <div class="sidebar__foot">
    <a href="#top" class="sidebar__back-to-top">↑ Back to top</a>
    <p class="sidebar__date">Last updated: [Date]</p>
  </div>
</aside>
```

### Hero Section

```html
<div class="page-hero">
  <p class="page-hero__eyebrow">
    <span data-lang="en">[Platform Name]</span>
    <span data-lang="pt">[Nome da Plataforma]</span>
  </p>
  <h1 class="page-hero__title">
    <span data-lang="en">[Document Title]</span>
    <span data-lang="pt">[Título do Documento]</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Description]</span>
    <span data-lang="pt">[Descrição]</span>
  </p>
</div>
```

### Image Container

```html
<figure class="image-container">
  <img
    src="./assets/[image].png"
    alt="[Descriptive alt text]"
    loading="lazy"
  />
</figure>
```

---

## 9. Changes from Previous Template

| Aspect | Previous | Updated |
|--------|----------|---------|
| Side panel position (tablet/mobile) | Left | **Right** |
| Side panel trigger | Hamburger opens from left | **Hamburger opens from right** |
| Side panel on desktop | Closeable with X | **Always open, X hidden** |
| Sidebar items | Number + title only | **Number + title + description** |
| Sidebar footer | None | **Back to top + document date** |
| Hero section | Platform, title, desc, chips | **Platform, title, desc only** |
| Progress bar | Not present | **Fixed element below header (not inside header)** |
| Images | Clickable with zoom | **Not clickable, no zoom** |
| Image containers | White/transparent | **Light tinted background** |
