import time
import os
def Clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

Clear()
try:
    timeSleep = int(input(""))
except:
    exit("NotNum")

while True:
    print("L╭─╮\n    ading..\n")
    time.sleep(timeSleep)
    Clear()
    
    print("L  ╮\n   ╯ading...\n")
    time.sleep(timeSleep)
    Clear()
    
    print("L\n ╰─╯ading..\n")
    time.sleep(timeSleep)
    Clear()
    
    print("L╭\n ╰  ading...\n")
    time.sleep(timeSleep)
    Clear()