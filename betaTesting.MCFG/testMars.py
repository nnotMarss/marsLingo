import time
import PySimpleGUI as sg
import os
def Clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

# Clear()
# try:
#     timeSleep = int(input(""))
# except:
#     exit("NotNum")

# while True:
#     print("L╭─╮\n    ading..\n")
#     time.sleep(timeSleep)
#     Clear()
    
#     print("L  ╮\n   ╯ading...\n")
#     time.sleep(timeSleep)
#     Clear()
    
#     print("L\n ╰─╯ading..\n")
#     time.sleep(timeSleep)
#     Clear()
    
#     print("L╭\n ╰  ading...\n")
#     time.sleep(timeSleep)
#     Clear()

################# config #################
class mars:
    class Lang:
        class EN:
            class Global:
                marsName = " RESTART: C:/Ur/Mom.py "
                marsLogo = "   __                             .____    .__                       \n _/  |_  _______________________  |    |   |__| ____    ____   ____\n \\   __\\/ __ \\_  __ \\_  __ \\__  \\ |    |   |  |/    \\  / ___\\ /  _ \\\n  |  | \\  ___/|  | \\/|  | \\// __ \\|    |___|  |   |  \\/ /_/  >  <_> )\n  |__|  \\___  >__|   |__|  (____  /_______ \\__|___|  /\\___  / \\____/\n            \\/                  \\/        \\/       \\//_____/         %s"
    class Setting:
        windowWid = 80
        windowChar = "="
    class Layouts:
        TestOne = [[sg.Text("Welcome to %s!\nPlease select one out of below mentioned mode to start! :3\n [1] Character Sound Learning, [3] Traslator.")],
                   [sg.Input(key="-INPUT-")],
                   [sg.Text(key="-TEXT-OPT-")],
                   [sg.Button("Confirm!"), sg.Button("Exit!")]]
##########################################

# tmp = int(mars.Setting.windowWid) * mars.Setting.windowChar
# print(tmp)


tmp = (int((mars.Setting.windowWid - len(mars.Lang.EN.Global.marsName)) / 2) * mars.Setting.windowChar) + mars.Lang.EN.Global.marsName + (int((mars.Setting.windowWid - len(mars.Lang.EN.Global.marsName)) / 2) * mars.Setting.windowChar)
print(tmp)

# tmp = int(mars.Setting.windowWid) * mars.Setting.windowChar
# print(tmp)
# # Define the window's contents
# layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
#             [sg.Input()],
#             [sg.Button('Ok')] ]

# # Create the window
# window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# # Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# # Do something with the information gathered
# print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# # Finish up by removing from the screen
# window.close()                                  # Part 5 - Close the Window


# startW = sg.Window("%s - Start Page" % mars.Lang.EN.Global.marsName, mars.Layouts.TestOne)

# choice, anwsers = startW.read()
# if choice == "Exit!" or choice == sg.WINDOW_CLOSED:
#     exit("ExitOnUserDemand")
# else:
#     pass

# startW["-TEXT-OPT-"].update('Hello ' + anwsers['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# import remi.gui as gui
# from remi import start, App

# class MyApp(App):
#     def __init__(self, *args):
#         super(MyApp, self).__init__(*args)

#     def main(self):
#         container = gui.VBox(width=120, height=100)
#         self.lbl = gui.Label('Hello world!')
#         self.bt = gui.Button('Press me!')

#         # setting the listener for the onclick event of the button
#         self.bt.onclick.do(self.on_button_pressed)

#         # appending a widget to another, the first argument is a string key
#         container.append(self.lbl)
#         container.append(self.bt)

#         # returning the root widget
#         return container

#     # listener function
#     def on_button_pressed(self, widget):
#         self.lbl.set_text('Button pressed!')
#         self.bt.set_text('Hi!')

# # starts the web server
# start(MyApp, port=8081)