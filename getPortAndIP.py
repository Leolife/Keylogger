def getIP():
    """
    Takes user inputted IP address and validates to ensure it is an IPv4 address.
    """
    valid_ip = False
    while not valid_ip:
        try:
            valid_ip = True  # assumes valid, but will change if invalid
            serverIP = input("IP address: ")
            check_ip = serverIP.split(".")  # separates the string by '.' and puts elements into a list
            check_ip = list(map(int, check_ip))  # converts the list elements into integers
            for num in check_ip:
                if not (0 <= num <= 255):  # ensures each octet is between 0 and 255
                    valid_ip = False
                    break
            if len(check_ip) != 4:  # ensures there are 4 octets
                valid_ip = False
            if not valid_ip:
                print("Invalid IP address")
        except ValueError:  # error catching for if there are not integers in ip address
            valid_ip = False
            print("Invalid IP address")
    return serverIP


def getPort():
    """
    Takes user inputted port and validates to ensure it is a correct port.
    """
    valid_port = False
    while not valid_port:
        try:
            valid_port = True  # assumes valid, but will change if invalid
            serverPort = int(input("Port number: "))  # converts the port into integer
            if not (1024 <= serverPort <= 65535):  # ensures port is between 1024 and 65,535 b/c 0-1023 are reserved
                valid_port = False
            if not valid_port:
                print("Invalid port")
        except ValueError:  # error catching for if there is not an integer in the port number
            valid_port = False
            print("Invalid port")
    return serverPort
