def on_received_number(receivedNumber):
    global hasDuck
    if receivedNumber == ID:
        hasDuck = True
        basic.show_icon(IconNames.DUCK)
    else:
        hasDuck = False
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global sendTo, hasDuck
    if hasDuck:
        sendTo = randint(1, players)
        if sendTo != ID:
            hasDuck = False
            basic.clear_screen()
            radio.send_number(sendTo)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

sendTo = 0
hasDuck = False
ID = 0
players = 0
radio.set_group(42)
players = 4
ID = 2
basic.show_number(ID)
if ID == 1:
    hasDuck = True
else:
    hasDuck = False