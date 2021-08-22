input.onButtonPressed(Button.A, function () {
    loopcount = 0
    for (let index = 0; index < 100; index++) {
        soundExpression.sad.play()
        loopcount += 1
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . # #
            # # # # .
            . # . # .
            `)
        basic.showLeds(`
            . . . . .
            . . . # #
            # . . . #
            . # # # #
            . . # . #
            `)
        basic.clearScreen()
        basic.showString("POOP")
    }
})
input.onButtonPressed(Button.B, function () {
    music.stopAllSounds()
})
let loopcount = 0
basic.showIcon(IconNames.Heart)
