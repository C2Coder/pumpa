def draw():
    global display
    display = Math.map(val, limit_min, limit_max, 1, 5)
    basic.show_number(display)
    if display == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """)
    elif display == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
        """)
    elif display == 3:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif display == 4:
        basic.show_leds("""
            . . . . .
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif display == 5:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        pass
val = 0
display = 0
limit_max = 0
limit_min = 0
OLED.init(128, 64)
limit_min = 350
limit_max = 400

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    global val
    val = pins.analog_read_pin(AnalogPin.P2)
    draw()
    if val > limit_max:
        pins.digital_write_pin(DigitalPin.P12, 1)
    elif val < limit_min:
        pins.digital_write_pin(DigitalPin.P12, 0)
    else:
        pass
    OLED.write_num_new_line(val)
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
loops.every_interval(200, on_every_interval)
