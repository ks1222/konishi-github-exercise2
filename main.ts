radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == ID) {
        hasDuck = true
        basic.showIcon(IconNames.Duck)
    } else {
        hasDuck = false
    }
})
input.onGesture(Gesture.Shake, function () {
    if (hasDuck) {
        sendTo = randint(1, players)
        if (sendTo != ID) {
            hasDuck = false
            basic.clearScreen()
            radio.sendNumber(sendTo)
        }
    }
})
let sendTo = 0
let hasDuck = false
let ID = 0
let players = 0
radio.setGroup(42)
players = 4
ID = 2
basic.showNumber(ID)
if (ID == 1) {
    hasDuck = true
} else {
    hasDuck = false
}
