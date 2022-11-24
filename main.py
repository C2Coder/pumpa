val = 0
OLED.init(128, 64)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    global val
    val = pins.analog_read_pin(AnalogPin.P3)
    OLED.write_num_new_line(val)
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    OLED.new_line()
    if val > 400:
        pins.digital_write_pin(DigitalPin.P2, 1)
    elif val < 350:
        pins.digital_write_pin(DigitalPin.P2, 0)
    else:
        pass
loops.every_interval(200, on_every_interval)
