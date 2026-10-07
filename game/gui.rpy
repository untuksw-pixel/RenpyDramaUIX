## Initialization
init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

## Color Palette - Langit Masih Sama
## Extracted from the UI design sheet:
## Soft Peach / Rose: #f7d8d1
## Muted Mauve: #b690a0
## Slate Cool: #5b6175
## Slate Deep: #41516b
## Dark Background: #121622

define gui.accent_color = '#f7d8d1'
define gui.idle_color = '#8e9aaf'
define gui.idle_small_color = '#717e97'
define gui.hover_color = '#f7d8d1'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#454f63'

define gui.muted_color = '#252d3d'
define gui.hover_muted_color = '#384359'

define gui.text_color = '#f8fafc'
define gui.interface_text_color = '#e2e8f0'

## Typography
define gui.text_font = "fonts/Inter-Regular.ttf"
define gui.name_text_font = "fonts/Inter-Regular.ttf"
define gui.interface_text_font = "fonts/Inter-Regular.ttf"

define gui.title_font = "fonts/Caveat-Bold.ttf"
define gui.serif_font = "fonts/Lora-Regular.ttf"

define gui.text_size = 26
define gui.name_text_size = 30
define gui.interface_text_size = 22
define gui.label_text_size = 28
define gui.notify_text_size = 20
define gui.title_text_size = 64

## Dialogue Box
define gui.textbox_height = 230
define gui.textbox_yalign = 0.94

define gui.name_xpos = 42
define gui.name_ypos = 28
define gui.name_xalign = 0.0

define gui.dialogue_xpos = 42
define gui.dialogue_ypos = 78
define gui.dialogue_width = 1176
define gui.dialogue_text_xalign = 0.0

## Choice Buttons
define gui.choice_button_width = 760
define gui.choice_button_height = 68
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(24, 12, 24, 12)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = "#e2e8f0"
define gui.choice_button_text_hover_color = "#f7d8d1"

## Quick Buttons
define gui.quick_button_text_size = 15
define gui.quick_button_text_idle_color = "#8e9aaf"
define gui.quick_button_text_hover_color = "#f7d8d1"
define gui.quick_button_text_selected_color = "#ffffff"

## Navigation
define gui.navigation_spacing = 20

## File Slots
define gui.slot_button_width = 360
define gui.slot_button_height = 220
define gui.slot_button_borders = Borders(12, 12, 12, 12)
define gui.slot_button_text_size = 18
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = "#8e9aaf"
define gui.slot_button_text_selected_idle_color = "#ffffff"
define gui.slot_button_text_selected_hover_color = "#f7d8d1"

define config.thumbnail_width = 336
define config.thumbnail_height = 138

## History
define gui.history_height = 140
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 0.0
define gui.history_name_text_color = "#b690a0"

define gui.history_text_xpos = 320
define gui.history_text_ypos = 0
define gui.history_text_width = 1100
define gui.history_text_xalign = 0.0
