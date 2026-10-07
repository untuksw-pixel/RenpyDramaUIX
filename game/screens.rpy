## Screens - Still The Same Sky
## Custom UI implementation based on the Drama Visual Novel UI concept.

init -1:
    default preferences.fullscreen = False

################################################################################
## Main Menu
################################################################################

screen main_menu():
    tag menu

    # Background
    add "images/main_menu_bg.png"

    # Subtle bottom vignette
    add Transform("#000000", alpha=0.25)

    # Left Column: Elegant title and poetic subtitle
    vbox:
        xpos 160
        ypos 180
        spacing 24

        text _("Still\nThe Same\nSky"):
            font gui.title_font
            size 96
            color "#ffffff"
            line_spacing -15
            outlines [(3, "#101622aa", 0, 0)]

        null height 8

        text _("Some encounters are destined\nnever to truly end."):
            font gui.text_font
            size 19
            color "#cbd5e1"
            italic True
            line_spacing 4
            outlines [(1, "#101622cc", 0, 0)]

    # Bottom left subtle label
    text _("MAIN MENU"):
        xpos 80
        yalign 0.94
        size 13
        color "#64748b"
        kerning 4

    # Right Column: Minimalist navigation menu
    vbox:
        xalign 0.72
        ypos 230
        spacing 26

        textbutton _("START"):
            action Start()
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"

        textbutton _("CONTINUE"):
            action Continue()
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"

        textbutton _("LOAD"):
            action ShowMenu("load")
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"

        textbutton _("GALLERY"):
            action ShowMenu("gallery")
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"

        textbutton _("SETTINGS"):
            action ShowMenu("preferences")
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"

        textbutton _("QUIT"):
            action Quit(confirm=not main_menu)
            text_size 20
            text_kerning 3
            text_idle_color "#94a3b8"
            text_hover_color "#ffffff"


################################################################################
## Dialogue Screen (Say)
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        align (0.5, 0.94)
        xsize 1260
        ysize 220
        background "gui/textbox.png"
        padding (48, 28, 48, 24)

        if who is not None:
            text who:
                id "who"
                font gui.name_text_font
                size 28
                bold True
                color "#ffffff"
                ypos 4

        text what:
            id "what"
            font gui.text_font
            size 24
            color "#f1f5f9"
            ypos 46
            xsize 1164
            line_spacing 6

        # Quick Menu embedded at the bottom right of the textbox
        use quick_menu


################################################################################
## Quick Menu
################################################################################

screen quick_menu():
    zorder 100

    hbox:
        align (0.98, 0.88)
        spacing 18

        textbutton _("AUTO"):
            action Preference("auto-forward", "toggle")
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"
            text_selected_color "#ffffff"

        textbutton _("SKIP"):
            action Skip() alternate Skip(fast=True, confirm=True)
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"

        textbutton _("HISTORY"):
            action ShowMenu('history')
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"

        textbutton _("SAVE"):
            action ShowMenu('save')
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"

        textbutton _("LOAD"):
            action ShowMenu('load')
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"

        textbutton _("SETTINGS"):
            action ShowMenu('preferences')
            text_size 13
            text_kerning 1
            text_idle_color "#717e97"
            text_hover_color "#f7d8d1"


################################################################################
## Choice Screen
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        align (0.5, 0.65)
        spacing 16

        for i, item in enumerate(items):
            $ symbol = "◇" if i % 2 == 0 else "+"
            button:
                action item.action
                xsize 760
                ysize 68
                idle_background "images/choice_idle.png"
                hover_background "images/choice_hover.png"
                padding (28, 18)

                hbox:
                    spacing 16
                    align (0.0, 0.5)
                    text symbol:
                        size 18
                        color "#b690a0"
                        align (0.0, 0.5)
                    text item.caption:
                        size 22
                        color "#f1f5f9"
                        hover_color "#f7d8d1"
                        align (0.0, 0.5)


################################################################################
## Pause / Game Menu (Jeda)
################################################################################

screen game_menu(title="", scroll=None, yinitial=0.0):
    tag menu
    modal True

    # Darkened blurred background
    add "images/game_menu_bg.png"

    # Close button 'X' at top right
    textbutton "✕":
        align (0.95, 0.05)
        action Return()
        text_size 28
        text_idle_color "#8e9aaf"
        text_hover_color "#f7d8d1"

    # If this is specifically the pause menu, show centered Pause card
    if title == "" or title == _("Pause") or title == "Pause" or title == "Jeda":
        frame:
            align (0.5, 0.5)
            xsize 480
            ysize 540
            background "images/jeda_card.png"
            padding (36, 36)

            vbox:
                align (0.5, 0.5)
                spacing 20

                text _("Pause"):
                    font gui.serif_font
                    size 48
                    color "#ffffff"
                    align (0.5, 0.0)

                vbox:
                    align (0.5, 0.5)
                    spacing 16

                    textbutton _("SAVE"):
                        action ShowMenu("save")
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

                    textbutton _("LOAD"):
                        action ShowMenu("load")
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

                    textbutton _("HISTORY"):
                        action ShowMenu("history")
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

                    textbutton _("SETTINGS"):
                        action ShowMenu("preferences")
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

                    textbutton _("GALLERY"):
                        action ShowMenu("gallery")
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

                    textbutton _("TITLE"):
                        action MainMenu()
                        xsize 260
                        ysize 46
                        hover_background "images/btn_pill.png"
                        text_align (0.5, 0.5)
                        text_size 20
                        text_kerning 2
                        text_idle_color "#8e9aaf"
                        text_hover_color "#ffffff"

    else:
        # Standard sub-screen container (for save, load, preferences, etc.)
        transclude


################################################################################
## Save / Load Screen
################################################################################

screen save():
    tag menu
    use file_slots(_("SAVE"))

screen load():
    tag menu
    use file_slots(_("LOAD"))

screen file_slots(title):
    use game_menu(title=title):
        # Header tabs: SAVE | LOAD
        vbox:
            align (0.5, 0.08)
            spacing 6

            hbox:
                spacing 48
                align (0.5, 0.5)

                textbutton _("SAVE"):
                    action ShowMenu("save")
                    text_size 22
                    text_kerning 2
                    text_bold True
                    text_idle_color ("#f7d8d1" if title == _("SAVE") else "#64748b")
                    text_hover_color "#ffffff"

                textbutton _("LOAD"):
                    action ShowMenu("load")
                    text_size 22
                    text_kerning 2
                    text_bold True
                    text_idle_color ("#f7d8d1" if title == _("LOAD") else "#64748b")
                    text_hover_color "#ffffff"

            # Underline bar on active tab
            hbox:
                align (0.5, 0.5)
                spacing 48
                if title == _("SAVE"):
                    frame:
                        xsize 72
                        ysize 2
                        background "#f7d8d1"
                    null width 72
                else:
                    null width 72
                    frame:
                        xsize 72
                        ysize 2
                        background "#f7d8d1"

        # 3x2 Grid of save slots
        grid 3 2:
            align (0.5, 0.54)
            xspacing 28
            yspacing 24

            for slot in range(1, 7):
                $ slot_num = f"{slot:02d}"
                button:
                    action FileAction(slot)
                    xsize 360
                    ysize 220
                    idle_background "images/slot_idle.png"
                    hover_background "images/slot_hover.png"
                    padding (12, 12)

                    vbox:
                        spacing 8
                        align (0.5, 0.5)

                        # Thumbnail screenshot
                        add FileScreenshot(slot):
                            xsize 336
                            ysize 138
                            align (0.5, 0.0)

                        # Slot metadata
                        hbox:
                            xsize 336
                            text "[slot_num]":
                                size 16
                                bold True
                                color "#f7d8d1"
                            null width 12
                            text FileTime(slot, format=_("%Y-%m-%d %H:%M"), empty=_("Empty Slot")):
                                size 14
                                color "#94a3b8"

                        text FileSaveName(slot):
                            size 13
                            color "#cbd5e1"
                            xsize 336

        # Pagination at bottom right
        hbox:
            align (0.85, 0.94)
            spacing 18

            textbutton "‹":
                action FilePagePrevious()
                text_size 18
                text_idle_color "#64748b"
                text_hover_color "#f7d8d1"

            for page in range(1, 6):
                textbutton str(page):
                    action FilePage(page)
                    text_size 16
                    text_idle_color "#94a3b8"
                    text_hover_color "#f7d8d1"
                    text_selected_color "#ffffff"

            textbutton "›":
                action FilePageNext()
                text_size 18
                text_idle_color "#64748b"
                text_hover_color "#f7d8d1"


################################################################################
## History Screen
################################################################################

screen history():
    tag menu

    # Dark background
    add "images/game_menu_bg.png"

    # Close button 'X'
    textbutton "✕":
        align (0.95, 0.05)
        action Return()
        text_size 28
        text_idle_color "#8e9aaf"
        text_hover_color "#f7d8d1"

    # Header label
    text "HISTORY":
        xpos 160
        ypos 60
        size 16
        color "#64748b"
        kerning 4

    # Backlog scrollable area
    frame:
        align (0.5, 0.55)
        xsize 1320
        ysize 720
        background None

        viewport:
            yinitial 1.0
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 28
                xsize 1260

                for h in _history_list:
                    hbox:
                        spacing 24
                        xsize 1240

                        # Vertical accent indicator line
                        frame:
                            xsize 2
                            ysize 36
                            background "#b690a0"
                            align (0.0, 0.1)

                        # Speaker name
                        if h.who:
                            text h.who:
                                size 22
                                bold True
                                color "#f7d8d1"
                                min_width 140
                                xalign 0.0
                        else:
                            null width 140

                        # Dialogue excerpt
                        text h.what:
                            size 22
                            color "#e2e8f0"
                            line_spacing 4
                            xsize 1000

    # Minimalist flat return button
    button:
        align (0.92, 0.94)
        action Return()
        hover_background "#ffffff12"
        padding (14, 10)
        hbox:
            spacing 10
            align (0.5, 0.5)
            add "images/icon_back.png":
                align (0.0, 0.5)
            text _("Back"):
                size 18
                color "#94a3b8"
                hover_color "#f7d8d1"
                align (0.0, 0.5)


################################################################################
## Preferences / Settings Screen
################################################################################

default persistent.ui_category = "Display"
default persistent.resolution_choice = "1920 x 1080"
default persistent.transition_choice = "Fade"
default persistent.font_choice = "Inter"
default persistent.selected_language = "en"
default persistent.textbox_opacity = "75%"
default persistent.mousewheel_history = True
default persistent.confirm_quit = True

init python:
    _resolution_list = ["1920 x 1080", "1600 x 900", "1280 x 720"]

    def cycle_resolution(direction=1):
        curr = persistent.resolution_choice
        try:
            idx = _resolution_list.index(curr)
        except ValueError:
            idx = 0
        new_idx = (idx + direction) % len(_resolution_list)
        persistent.resolution_choice = _resolution_list[new_idx]
        res_map = {
            "1920 x 1080": (1920, 1080),
            "1600 x 900": (1600, 900),
            "1280 x 720": (1280, 720)
        }
        renpy.set_physical_size(res_map[persistent.resolution_choice])
        renpy.restart_interaction()

    _transition_list = ["Fade", "Dissolve", "None"]

    def cycle_transition(direction=1):
        curr = persistent.transition_choice
        try:
            idx = _transition_list.index(curr)
        except ValueError:
            idx = 0
        new_idx = (idx + direction) % len(_transition_list)
        persistent.transition_choice = _transition_list[new_idx]
        if persistent.transition_choice == "None":
            _preferences.transitions = 0
        else:
            _preferences.transitions = 2
        renpy.restart_interaction()

    _font_list = ["Inter", "Lora Serif"]
    _font_map = {
        "Inter": "fonts/Inter-Regular.ttf",
        "Lora Serif": "fonts/Lora-Regular.ttf"
    }

    def cycle_font(direction=1):
        curr = persistent.font_choice
        try:
            idx = _font_list.index(curr)
        except ValueError:
            idx = 0
        new_idx = (idx + direction) % len(_font_list)
        persistent.font_choice = _font_list[new_idx]
        gui.text_font = _font_map[persistent.font_choice]
        renpy.restart_interaction()

    _opacity_list = ["75%", "90%", "100%"]

    def cycle_opacity(direction=1):
        curr = persistent.textbox_opacity
        try:
            idx = _opacity_list.index(curr)
        except ValueError:
            idx = 0
        new_idx = (idx + direction) % len(_opacity_list)
        persistent.textbox_opacity = _opacity_list[new_idx]
        renpy.restart_interaction()

    def set_game_language(lang):
        persistent.selected_language = lang
        renpy.change_language(None if lang == "en" else "indonesian")
        renpy.restart_interaction()

style pref_slider is slider:
    xsize 280
    ysize 20
    left_bar Frame("images/slider_left.png", 5, 5)
    right_bar Frame("images/slider_right.png", 5, 5)
    thumb "images/slider_thumb.png"
    thumb_offset 10

screen preferences():
    tag menu

    # Dark background
    add "images/game_menu_bg.png"

    # Close button 'X'
    textbutton "✕":
        align (0.95, 0.05)
        action Return()
        text_size 28
        text_idle_color "#8e9aaf"
        text_hover_color "#f7d8d1"

    # Header
    text _("SETTINGS"):
        xpos 160
        ypos 60
        size 16
        color "#64748b"
        kerning 4

    hbox:
        align (0.5, 0.55)
        spacing 60

        # Left Sidebar (Categories)
        vbox:
            spacing 14
            xsize 240

            $ categories = [
                ("Display", _("Display")),
                ("Text", _("Text")),
                ("Audio", _("Audio")),
                ("Language", _("Language")),
                ("Gameplay", _("Gameplay"))
            ]
            for cat_id, cat_name in categories:
                button:
                    action SetVariable("persistent.ui_category", cat_id)
                    xsize 220
                    ysize 48
                    idle_background (None if persistent.ui_category != cat_id else "images/nav_active.png")
                    hover_background "images/nav_active.png"
                    padding (16, 12)

                    text cat_name:
                        size 18
                        color ("#ffffff" if persistent.ui_category == cat_id else "#8e9aaf")
                        align (0.0, 0.5)

            null height 40

            # Minimalist flat return button
            button:
                action Return()
                xsize 220
                ysize 44
                hover_background "#ffffff12"
                padding (14, 10)
                hbox:
                    spacing 10
                    align (0.0, 0.5)
                    add "images/icon_back.png":
                        align (0.0, 0.5)
                    text _("Back"):
                        size 18
                        color "#8e9aaf"
                        hover_color "#f7d8d1"
                        align (0.0, 0.5)

        # Right Panel (Options)
        frame:
            xsize 760
            ysize 540
            background "#12172488"
            padding (36, 32)

            vbox:
                spacing 18

                # 1. DISPLAY SETTINGS
                if persistent.ui_category == "Display":
                    fixed:
                        xsize 680
                        ysize 44
                        text _("Fullscreen"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action Preference("display", "toggle")

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Resolution"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        hbox:
                            align (1.0, 0.5)
                            spacing 14
                            textbutton "‹":
                                action Function(cycle_resolution, -1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5
                            text persistent.resolution_choice:
                                size 17
                                color "#cbd5e1"
                                min_width 130
                                text_align 0.5
                                yalign 0.5
                            textbutton "›":
                                action Function(cycle_resolution, 1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Skip After Choices"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action Preference("after choices", "toggle")

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Transition Effect"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        hbox:
                            align (1.0, 0.5)
                            spacing 14
                            textbutton "‹":
                                action Function(cycle_transition, -1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5
                            text persistent.transition_choice:
                                size 17
                                color "#cbd5e1"
                                min_width 100
                                text_align 0.5
                                yalign 0.5
                            textbutton "›":
                                action Function(cycle_transition, 1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Font Type"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        hbox:
                            align (1.0, 0.5)
                            spacing 14
                            textbutton "‹":
                                action Function(cycle_font, -1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5
                            text persistent.font_choice:
                                size 17
                                color "#cbd5e1"
                                min_width 110
                                text_align 0.5
                                yalign 0.5
                            textbutton "›":
                                action Function(cycle_font, 1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5

                # 2. TEXT SETTINGS
                elif persistent.ui_category == "Text":
                    fixed:
                        xsize 680
                        ysize 44
                        text _("Text Speed"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        bar value Preference("text speed"):
                            style "pref_slider"
                            align (1.0, 0.5)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Auto-Forward Delay"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        bar value Preference("auto-forward time"):
                            style "pref_slider"
                            align (1.0, 0.5)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Wait for Voice on Auto"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action Preference("wait for voice", "toggle")

                    null height 8

                    # Live preview card
                    frame:
                        xsize 680
                        ysize 100
                        padding (24, 18)
                        background "#161d2b"
                        vbox:
                            spacing 6
                            align (0.0, 0.5)
                            text _("Speed Preview:"):
                                size 13
                                color "#8e9aaf"
                            text _("Still the same sky, and so are the memories lingering here."):
                                size 17
                                color "#f7d8d1"

                # 3. AUDIO SETTINGS
                elif persistent.ui_category == "Audio":
                    fixed:
                        xsize 680
                        ysize 44
                        text _("Music Volume (BGM)"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        bar value Preference("music volume"):
                            style "pref_slider"
                            align (1.0, 0.5)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Sound Effects (SFX)"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        bar value Preference("sound volume"):
                            style "pref_slider"
                            align (1.0, 0.5)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Voice Volume"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        bar value Preference("voice volume"):
                            style "pref_slider"
                            align (1.0, 0.5)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Mute All Audio"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action Preference("all mute", "toggle")

                # 4. LANGUAGE SETTINGS
                elif persistent.ui_category == "Language":
                    fixed:
                        xsize 680
                        ysize 36
                        text _("Language Selection"):
                            size 20
                            bold True
                            color "#f1f5f9"
                            align (0.0, 0.5)

                    hbox:
                        spacing 20
                        button:
                            action Function(set_game_language, "en")
                            xsize 320
                            ysize 54
                            idle_background ("images/lang_card_selected.png" if persistent.selected_language == "en" else "images/lang_card_idle.png")
                            hover_background "images/lang_card_selected.png"
                            padding (20, 14)
                            hbox:
                                align (0.5, 0.5)
                                spacing 10
                                if persistent.selected_language == "en":
                                    text "✓" size 16 color "#f7d8d1"
                                text _("English (Default)"):
                                    size 16
                                    bold (persistent.selected_language == "en")
                                    color ("#f7d8d1" if persistent.selected_language == "en" else "#94a3b8")

                        button:
                            action Function(set_game_language, "id")
                            xsize 320
                            ysize 54
                            idle_background ("images/lang_card_selected.png" if persistent.selected_language == "id" else "images/lang_card_idle.png")
                            hover_background "images/lang_card_selected.png"
                            padding (20, 14)
                            hbox:
                                align (0.5, 0.5)
                                spacing 10
                                if persistent.selected_language == "id":
                                    text "✓" size 16 color "#f7d8d1"
                                text _("Bahasa Indonesia"):
                                    size 16
                                    bold (persistent.selected_language == "id")
                                    color ("#f7d8d1" if persistent.selected_language == "id" else "#94a3b8")

                    null height 10

                    frame:
                        xsize 680
                        padding (20, 16)
                        background "#161d2b"
                        text _("Interface and dialogue language will be updated immediately upon selection."):
                            size 14
                            color "#94a3b8"
                            line_spacing 4

                # 5. GAMEPLAY SETTINGS
                elif persistent.ui_category == "Gameplay":
                    fixed:
                        xsize 680
                        ysize 44
                        text _("Skip Unseen Text"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action Preference("skip", "toggle")

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Dialogue Box Opacity"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        hbox:
                            align (1.0, 0.5)
                            spacing 14
                            textbutton "‹":
                                action Function(cycle_opacity, -1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5
                            text persistent.textbox_opacity:
                                size 17
                                color "#cbd5e1"
                                min_width 80
                                text_align 0.5
                                yalign 0.5
                            textbutton "›":
                                action Function(cycle_opacity, 1)
                                text_size 22
                                text_idle_color "#8e9aaf"
                                text_hover_color "#f7d8d1"
                                yalign 0.5

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Mousewheel Rollback/History"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action ToggleField(persistent, "mousewheel_history", True, False)

                    fixed:
                        xsize 680
                        ysize 44
                        text _("Confirm Before Quit"):
                            size 19
                            color "#f1f5f9"
                            align (0.0, 0.5)
                        imagebutton:
                            align (1.0, 0.5)
                            idle "images/switch_off.png"
                            selected_idle "images/switch_on.png"
                            action ToggleField(persistent, "confirm_quit", True, False)


################################################################################
## Gallery Screen
################################################################################

screen gallery():
    tag menu

    # Blurred background
    add "images/game_menu_bg.png"

    # Close button 'X'
    textbutton "✕":
        align (0.95, 0.05)
        action Return()
        text_size 28
        text_idle_color "#8e9aaf"
        text_hover_color "#f7d8d1"

    # Header
    vbox:
        xpos 160
        ypos 56
        spacing 6

        text _("GALLERY"):
            size 16
            color "#64748b"
            kerning 4

        text _("Memories & Illustrations"):
            font gui.serif_font
            size 26
            color "#f1f5f9"

    # CG Grid (2 rows x 2 columns)
    $ gallery_items = [
        (_("01 • Sunset on the Balcony"), "images/thumb_main_menu.png", "images/main_menu_bg.png"),
        (_("02 • Rara's Gaze"), "images/thumb_scene_rara.png", "images/scene_rara.png"),
        (_("03 • Dika's Path"), "images/thumb_scene_dika.png", "images/scene_dika.png"),
        (_("04 • Story at the Reading Desk"), "images/thumb_scene_desk.png", "images/scene_desk.png")
    ]

    grid 2 2:
        align (0.5, 0.55)
        xspacing 48
        yspacing 32

        for title, thumb_path, full_path in gallery_items:
            button:
                action Show("cg_viewer", transition=dissolve, cg_image=full_path)
                xsize 416
                ysize 280
                idle_background Frame("images/slot_idle.png", 16, 16)
                hover_background Frame("images/slot_hover.png", 16, 16)
                padding (18, 16)

                vbox:
                    spacing 12
                    align (0.5, 0.5)

                    add thumb_path:
                        align (0.5, 0.0)

                    text title:
                        size 15
                        bold True
                        color "#cbd5e1"
                        hover_color "#f7d8d1"
                        align (0.5, 0.5)

    # Minimalist flat return button
    button:
        align (0.92, 0.94)
        action Return()
        hover_background "#ffffff12"
        padding (14, 10)
        hbox:
            spacing 10
            align (0.5, 0.5)
            add "images/icon_back.png":
                align (0.0, 0.5)
            text _("Back"):
                size 18
                color "#94a3b8"
                hover_color "#f7d8d1"
                align (0.0, 0.5)


################################################################################
## Fullscreen CG Viewer
################################################################################

screen cg_viewer(cg_image):
    modal True
    zorder 300

    button:
        action Hide("cg_viewer", transition=dissolve)
        xfill True
        yfill True
        background "#000000f0"

        add cg_image:
            align (0.5, 0.5)

        text _("Click anywhere to close"):
            align (0.5, 0.95)
            size 16
            color "#94a3b8"
            outlines [(1, "#000000cc", 0, 0)]


################################################################################
## About Screen
################################################################################

screen about():
    tag menu

    add "images/game_menu_bg.png"

    textbutton "✕":
        align (0.95, 0.05)
        action Return()
        text_size 28
        text_idle_color "#8e9aaf"
        text_hover_color "#f7d8d1"

    frame:
        align (0.5, 0.5)
        xsize 720
        ysize 480
        background "images/jeda_card.png"
        padding (48, 48)

        vbox:
            spacing 18
            align (0.5, 0.5)

            text _("Still The Same Sky"):
                font gui.title_font
                size 54
                color "#ffffff"
                align (0.5, 0.5)

            text _("UI Style: Minimalist, elegant, story-focused.\nSpecially crafted for an immersive and emotional\nvisual novel experience."):
                size 18
                color "#cbd5e1"
                align (0.5, 0.5)
                line_spacing 6
                text_align 0.5

            null height 12

            textbutton _("Back"):
                align (0.5, 0.5)
                action Return()
                text_size 20
                text_idle_color "#f7d8d1"
                text_hover_color "#ffffff"


################################################################################
## Confirmation Modal Screen
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "#00000088"

    frame:
        align (0.5, 0.5)
        xsize 520
        ysize 260
        background "images/jeda_card.png"
        padding (36, 36)

        vbox:
            align (0.5, 0.5)
            spacing 28

            text _(message):
                size 22
                color "#f1f5f9"
                text_align 0.5
                align (0.5, 0.5)

            hbox:
                align (0.5, 0.5)
                spacing 42

                textbutton _("Yes"):
                    action yes_action
                    text_size 20
                    text_bold True
                    text_idle_color "#f7d8d1"
                    text_hover_color "#ffffff"

                textbutton _("No"):
                    action no_action
                    text_size 20
                    text_bold True
                    text_idle_color "#8e9aaf"
                    text_hover_color "#ffffff"


################################################################################
## Notification Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        align (0.5, 0.08)
        padding (24, 12)
        background "#161b28dd"

        text "[message!tq]":
            size 18
            color "#f7d8d1"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0.0 yoffset -20
        easein_quint .25 alpha 1.0 yoffset 0
    on hide:
        easeout_quint .25 alpha 0.0 yoffset -20


################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        align (0.5, 0.5)
        xsize 600
        ysize 180
        background "images/jeda_card.png"
        padding (36, 32)

        vbox:
            spacing 18
            align (0.5, 0.5)

            text prompt:
                size 20
                color "#f1f5f9"
                align (0.5, 0.5)

            input id "input":
                size 22
                color "#f7d8d1"
                align (0.5, 0.5)
