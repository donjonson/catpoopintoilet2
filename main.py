def on_button_pressed_a():
    global loopcount
    loopcount = 0
    for index in range(100):
        soundExpression.hello.play()
        loopcount += 1
        basic.show_leds("""
            . . . . .
            . . . # .
            . . . # #
            # # # # .
            . # . # .
            """)
        basic.show_leds("""
            . . . . .
            . . . # #
            # . . . #
            . # # # #
            . . # . #
            """)
        basic.clear_screen()
        basic.show_string("POOP")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.stop_all_sounds()
input.on_button_pressed(Button.B, on_button_pressed_b)

loopcount = 0
basic.show_icon(IconNames.HEART)