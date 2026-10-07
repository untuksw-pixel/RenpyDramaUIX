## Game Configuration: Still The Same Sky

define config.name = _("Still The Same Sky")
define gui.show_name = False
define config.version = "1.0"
define gui.about = _p("""Still The Same Sky - Ren'Py Visual Novel UI Concept""")
define build.name = "still_the_same_sky"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 50
default preferences.afm_time = 15

define config.save_directory = "still_the_same_sky-save"
define config.window_icon = "gui/window_icon.png"
