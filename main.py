random = 0

def on_button_pressed_a():
    roll_dice()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    roll_dice()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    roll_dice()
input.on_button_pressed(Button.B, on_button_pressed_b)

def roll_dice():
    global random
    random = randint(1, 6)
    music.play(music.tone_playable(415, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    if random == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif random == 2:
        basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . # . .
            . . . . .
            """)
    elif random == 3:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """)
    elif random == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    elif random == 5:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . # . # .
            . # . # .
            . # . # .
            . . . . .
            """)