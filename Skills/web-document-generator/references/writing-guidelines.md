# Writing Guidelines

Style guide for creating professional B2B technical documentation.

## Voice and Tone

### Professional but Approachable
- Write clearly and directly
- Avoid jargon unless necessary for the audience
- Be helpful, not condescending
- Use active voice

### Consistent Terminology
- Use the same term for the same concept throughout
- Match UI labels exactly (buttons, menus, screens)
- Define technical terms on first use
- Maintain a glossary for complex documents

---

## Structure Principles

### Progressive Disclosure
- Start with the overview, then details
- Most important information first
- Allow scanning with clear headers
- Use expandable sections for optional detail

### Logical Flow
- Number steps sequentially
- Use consistent heading hierarchy
- Group related content together
- Provide clear transitions between sections

---

## Writing Instructions

### Imperative Verbs
Start instructions with action verbs:

| Good | Avoid |
|------|-------|
| Tap **Settings** | You should tap Settings |
| Connect the cable | The cable should be connected |
| Verify the status | Make sure to verify the status |
| Select your region | You need to select your region |

### Be Specific
| Good | Avoid |
|------|-------|
| Tap **NEXT STEP** | Press the button |
| Wait for the 5-second countdown | Wait a moment |
| Enter your 6-digit PIN | Type your password |
| Select **English** from the dropdown | Choose your language |

### Conditional Instructions
Use clear if/then structures:

```
If the LED is green → Tap NEXT STEP
If the LED is red → Tap Troubleshooting Guide
```

Or decision tables for multiple conditions:

| Situation | Action |
|-----------|--------|
| LED is green | Tap **NEXT STEP** |
| LED is amber | Wait 30 seconds, then retry |
| LED is red | Tap **Troubleshooting Guide** |

---

## Formatting Conventions

### UI Elements
- **Bold** for buttons, menu items, screen names
- Use exact capitalization from the UI
- Include icons when helpful: Tap the 🔄 icon

### Code and Technical Values
- `monospace` for code, file paths, commands
- Include full paths: `/settings/network/apn.json`
- Quote exact error messages

### Emphasis
- *Italic* for new terms or light emphasis
- **Bold** for strong emphasis
- Avoid ALL CAPS except for UI text that uses it

### Lists
Use numbered lists for sequential steps:
1. First step
2. Second step
3. Third step

Use bullet lists for non-sequential items:
- Option A
- Option B
- Option C

---

## Callout Types

### Warning
For actions that could cause data loss or require caution:

> ⚠️ **Do not switch or close the app** during the asset refresh.

### Info
For helpful tips or additional context:

> ℹ️ Quick Installation toggle (OFF by default) — when enabled, skips intermediate steps.

### Conditional
For steps that only apply in certain situations:

> 🔀 This step only appears for devices that support external cameras.

### Success
For confirming successful completion:

> ✅ Installation complete. The device is now ready for use.

---

## Multi-language Content

### Parallel Structure
Maintain identical structure across all languages:

```html
<span data-lang="en">Tap **NEXT STEP** to continue.</span>
<span data-lang="pt">Toque em **PRÓXIMO PASSO** para continuar.</span>
```

### Translation Guidelines
- Translate meaning, not just words
- Adapt UI terminology to localized app versions
- Keep formatting consistent (bold, links)
- Verify technical terms with native speakers

### Common Translations (English → Portuguese)

| English | Portuguese |
|---------|------------|
| Step | Passo |
| Tap | Toque |
| Next Step | Próximo Passo |
| Previous | Anterior |
| Settings | Configurações |
| Connect | Conectar |
| Verify | Verificar |
| Complete | Concluir |
| Cancel | Cancelar |
| Save | Salvar |
| Edit | Editar |
| Delete | Excluir |
| Warning | Aviso |
| Error | Erro |
| Success | Sucesso |

---

## Screenshots

### When to Include
- New screens or major UI states
- Complex interactions
- Reference images for physical actions
- Before/after comparisons

### Captions
Write descriptive captions that add context:

| Good | Avoid |
|------|-------|
| "Installation overview showing all 7 steps" | "Screenshot 1" |
| "LED status indicators — green indicates online" | "LED screen" |
| "Mounting position on windshield" | "Figure 3" |

### Alt Text
Write alt text that conveys the image's purpose:

| Good | Avoid |
|------|-------|
| "Home screen with Installation button highlighted" | "Home screen screenshot" |
| "Green LED indicator showing device is online" | "LED indicator" |
| "Correctly mounted dash cam showing road-facing view" | "Dash cam photo" |

---

## Tables

### Decision Tables
Use for branching logic:

| Situation | Action |
|-----------|--------|
| Device is provisioned | Tap **NEXT STEP** |
| Device is semi-provisioned | Complete required fields |
| Device is unprovisioned | Tap **QUIT INSTALLATION** |

### Specification Tables
Use consistent columns:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `timeout` | 30 | Connection timeout in seconds |
| `retries` | 3 | Number of retry attempts |

### Comparison Tables
Use check marks for features:

| Feature | Basic | Pro |
|---------|-------|-----|
| Single device | ✓ | ✓ |
| Multi-device | — | ✓ |
| Analytics | — | ✓ |

---

## Common Patterns

### Step Completion
End each major step with a clear completion statement:

> Step 3 is complete when the dash cam is connected, volume is set, and server connectivity is confirmed.

### Prerequisites
List at the start of procedures:

**Before you begin:**
- Ensure the device is powered on
- Verify Wi-Fi is enabled
- Have your installation credentials ready

### Troubleshooting Links
Consistently format troubleshooting references:

> If the connection fails → Tap **Troubleshooting Guide ›** for assistance.

### Cross-references
Link to related sections:

> For APN configuration details, see [Step 3.3: Select or add an APN](#step-3-3).

---

## Quality Checklist

Before finalizing any document:

- [ ] All UI element names match the actual interface
- [ ] Steps are numbered correctly and sequentially
- [ ] Every image has descriptive alt text
- [ ] All links work correctly
- [ ] Language translations are complete and parallel
- [ ] Decision tables cover all scenarios
- [ ] Callouts are used appropriately
- [ ] No orphan headers (header without following content)
- [ ] Document flows logically from start to finish
