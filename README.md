# RenpyDramaUIX — Langit Masih Sama

A warm, cinematic romance and slice-of-life drama visual novel user interface theme built for **Ren'Py 8.2+**.

---

## Overview

**RenpyDramaUIX** (*Langit Masih Sama*) is designed for emotional, atmospheric narrative games, slice-of-life storytelling, and romance visual novels. Featuring a soft pastel and warm slate palette, card-based dialogue layouts, and custom interactive widgets, it provides an elegant and polished reading experience.

---

## Key Features

- **Cinematic & Warm Aesthetic:**
  - Soft peach and rose accents (`#f7d8d1`, `#b690a0`) paired with deep midnight slate backgrounds (`#121622`).
  - Balanced serif and modern sans-serif typography pairing (Caveat, Lora, Inter).
- **Custom UI Components:**
  - Modern dialogue box with name badges and subtle drop shadows.
  - Floating pill-style choice buttons with smooth hover feedback.
  - File slots system showcasing screenshot thumbnails, chapter titles, and timestamps.
  - Pause / Quick Menu overlay with instant navigation shortcuts.
- **Comprehensive Settings Menu:**
  - Display preferences (Fullscreen and resolution switching).
  - Audio mixer (BGM, SFX, Voice sliders with custom thumbs).
  - Text speed controls and auto-forward timer adjustments.
  - Runtime language switcher with visual country card selector.
- **Bilingual Support:** Full English base scripts with Indonesian localization (`game/tl/indonesian/`).

---

## Directory Structure

```text
RenpyDramaUIX/
├── game/
│   ├── fonts/               # Caveat, Lora, and Inter font files
│   ├── gui/                 # Textbox frames and window icon
│   ├── images/              # Custom UI panels, buttons, toggles, cards, backgrounds
│   ├── tl/indonesian/       # Complete Indonesian localization strings
│   ├── gui.rpy              # Theme color palette, sizing, and styling rules
│   ├── options.rpy          # Window and build configuration
│   ├── screens.rpy          # Screen definitions (Menu, Save, Load, Settings, History)
│   └── script.rpy           # Demo script and scene flow
├── .gitignore
└── README.md
```

---

## Installation & Usage

1. Clone or download this repository:
   ```bash
   git clone https://github.com/untuksw-pixel/RenpyDramaUIX.git
   ```
2. Open the **Ren'Py Launcher** (version 8.2 or newer).
3. Add or select **RenpyDramaUIX** from the project list and click **Launch Project**.

---

## Compatibility

- **Engine:** Ren'Py 8.2+ (Python 3)
- **Native Resolution:** 1920 × 1080 (Full HD, 16:9)
- **Platforms:** Windows, macOS, Linux
