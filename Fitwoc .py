def on_button_pressed_a():
    basic.show_number(kroky)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(kroky * 0.05)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(kroky * 0.75)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global kroky, timer
    kroky += 1
    timer = 0
    basic.show_number(kroky)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

timer = 0
kroky = 0
radio.on()
radio.set_group(1)
basic.show_number(kroky)
timer = 0
kroky = 0

def on_forever():
    basic.pause(5000)
    radio.send_number(kroky)
basic.forever(on_forever)

def on_forever2():
    global timer
    basic.pause(1000)
    timer += 1
basic.forever(on_forever2)

def on_forever3():
    global timer
    if timer > 3600:
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        timer = 0
basic.forever(on_forever3)
