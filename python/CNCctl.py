import serial


ser = None
flag = False


def displayhelp():
    print("List of commands:")
    print("help -- display help")
    print("exit -- quit controller")
    print("shell -- interactive G-code shell")
    print("start -- open serial port to communicate")
    print("file -- start send code from file")


def shell():
    print("Entering Interactive G-code Shell...")
    print("Type return to return to controller")
    while True:
        code = input("G>")
        if(code == "return"):
            print("returning to normal shell")
            return
        else:
            ser.write((code.strip() + "\n").encode("ASCII"))
            ser.read(1)


def send():
    fn = input("Please input G-Code file's filename:")
    f = open(fn)
    for l in f:
        print(l.strip())
        ser.write((l.strip() + "\n").encode("ASCII"))
        ser.read(1)

print("Welcome to CNC430 Contorl Program!")
print("type in commands to operate; help to list commands")

while True:
    comm = input(">")
    if(comm == "exit"):
        print()
        print("bye bye")
        exit()
    elif(comm == "help"):
        displayhelp()
    elif(comm == "shell"):
        if(flag):
            shell()
        else:
            print("Please open a serial port first")
    elif(comm == "start"):
        portnum = input("Input Serial port number:")
        ser = serial.Serial(portnum, 9600, timeout=None)
        flag = True
    elif(comm == "file"):
        if(flag):
            send()
        else:
            print("Please open a serial port first")
    else:
        print("I can't get you ;(")
