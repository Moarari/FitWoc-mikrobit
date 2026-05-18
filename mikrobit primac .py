def on_received_number(receivedNumber):
    serial.write_line("kroky:" + ("" + str(receivedNumber)))
    serial.write_line("kalorie:" + ("" + str(receivedNumber * 0.05)))
    serial.write_line("metre:" + ("" + str(receivedNumber * 0.75)))
radio.on_received_number(on_received_number)

def on_forever():
    basic.show_icon(IconNames.YES)
radio.on()
radio.set_group(1)