let val = 0
OLED.init(128, 64)
let limit_min = 350
let limit_max = 400
basic.forever(function () {
	
})
loops.everyInterval(200, function () {
    val = pins.analogReadPin(AnalogPin.P4)
    OLED.writeNumNewLine(val)
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    if (val > limit_max) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    } else if (val < limit_min) {
        pins.digitalWritePin(DigitalPin.P2, 0)
    } else {
    	
    }
})
