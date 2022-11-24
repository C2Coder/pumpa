function draw () {
	
}
let display = 0
let val = 0
OLED.init(128, 64)
let limit_min = 350
let limit_max = 400
loops.everyInterval(200, function () {
    val = pins.analogReadPin(AnalogPin.P2)
    display = Math.round(Math.map(val, limit_min, limit_max, 1, 5))
    OLED.writeNumNewLine(val)
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    OLED.newLine()
    if (display == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
    } else if (display == 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
    } else if (display == 3) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (display == 4) {
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (display == 5) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
    	
    }
    if (val >= limit_max) {
        pins.digitalWritePin(DigitalPin.P12, 1)
    } else if (val <= limit_min) {
        pins.digitalWritePin(DigitalPin.P12, 0)
    } else {
    	
    }
})
