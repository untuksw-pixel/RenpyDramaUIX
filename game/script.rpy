## Script - Still The Same Sky

# Character declarations
define r = Character("Rara", color="#f7d8d1")
define d = Character("Dika", color="#b690a0")

# Scene background declarations
image bg main_menu = "images/main_menu_bg.png"
image bg rara = "images/scene_rara.png"
image bg dika = "images/scene_dika.png"
image bg desk = "images/scene_desk.png"

# Game start label
label start:
    scene bg rara with dissolve

    r "Are you sure... you're okay?"

    d "Yeah. I'm just... a bit tired."

    r "Don't lie. You're thinking about something else, aren't you?"

    d "No. Really. I'm just afraid... that you'll be disappointed."

    r "I won't be disappointed. As long as you're honest with me, that's enough."

    scene bg dika with dissolve

    menu:
        "I will wait for her.":
            jump choice_wait

        "I should head home.":
            jump choice_leave

label choice_wait:
    d "Then, I'll stay right here... waiting for you."

    r "Thank you, Dika. Don't let this twilight pass by alone."

    jump scene_reflection

label choice_leave:
    d "Maybe it's better if I head home now. Before the sky turns completely dark."

    r "Take care on your way. See you tomorrow."

    jump scene_reflection

label scene_reflection:
    scene bg desk with dissolve

    "Some encounters are destined never to truly end."

    "And under this same sky, our story continues."

    return
