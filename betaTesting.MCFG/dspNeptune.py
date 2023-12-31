import time
import shutil
wait = time.sleep
stream = print

def termSize():
    x, y = shutil.get_terminal_size()
    return x, y

def line(val1="", val2="=", val3=True, val4=0):
    if val3 == True:
        val4, y = termSize() 
        pass
    lTmp = (int((val4 - len(val1)) / 2) * val2)
    lTmp = lTmp + val1 + lTmp
    stream(lTmp)
    pass
