    # <cmdInit>
import os
import random
import time

class mars:
    import langMars as Lang
    import langMars2 as Lang2
    Stream = print
    Collect = input

    def Install(module):
        try:
            import module
        except ModuleNotFoundError:
            os.system("py -m pip install %s" % module)

    try:
        import pytermgui as Gui
    except ModuleNotFoundError:
        Install("pytermgui")

    def Clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    class Setting:
        EventNum = random.randint(100, 999)
        UserLang = open(".\\settingsMars.MCFG\\usrLangSel1.ENT", "r").read()
        FirstTime = open(".\\settingsMars.MCFG\\firstTmUp.ENT", "r").read()
        VerNum = open(".\\settingsMars.MCFG\\verNum.ENT", "r").read()
    
    class Lingo:
        class LetterA:
            Disp = "A"
            Sound = "Fa"
        class LetterB:
            Disp = "B"
            Sound = "Fe"
        class LetterC:
            Disp = "C"
            Sound = "Fu"
        class LetterD:
            Disp = "D"
            Sound = "Ja"
        class LetterE:
            Disp = "E"
            Sound = "Je"
        class LetterF:
            Disp = "F"
            Sound = "Ju"
        class LetterG:
            Disp = "G"
            Sound = "Ka"
        class LetterH:
            Disp = "H"
            Sound = "Ke"
        class LetterI:
            Disp = "I"
            Sound = "Ku"
        class LetterJ:
            Disp = "J"
            Sound = "Na"
        class LetterK:
            Disp = "K"
            Sound = "Ne"
        class LetterL:
            Disp = "L"
            Sound = "Nu"
        class LetterM:
            Disp = "M"
            Sound = "Ra"
        class LetterN:
            Disp = "N"
            Sound = "Re"
        class LetterO:
            Disp = "O"
            Sound = "Ru"
        class LetterP:
            Disp = "P"
            Sound = "Sa"
        class LetterQ:
            Disp = "Q"
            Sound = "Se"
        class LetterR:
            Disp = "R"
            Sound = "Su"
        class LetterS:
            Disp = "S"
            Sound = "Ta"
        class LetterT:
            Disp = "T"
            Sound = "Te"
        class LetterU:
            Disp = "U"
            Sound = "Tu"
        class LetterV:
            Disp = "V"
            Sound = "Za"
        class LetterW:
            Disp = "W"
            Sound = "Ze"
        class LetterX:
            Disp = "X"
            Sound = "Zu"
        class LetterY:
            Disp = "Y"
            Sound = "Ga"
        class LetterZ:
            Disp = "Z"
            Sound = "Ge"
        Map = {
        1: LetterA,
        2: LetterB,
        3: LetterC,
        4: LetterD,
        5: LetterE,
        6: LetterF,
        7: LetterG,
        8: LetterH,
        9: LetterI,
        10: LetterJ,
        11: LetterK,
        12: LetterL,
        13: LetterM,
        14: LetterN,
        15: LetterO,
        16: LetterP,
        17: LetterQ,
        18: LetterR,
        19: LetterS,
        20: LetterT,
        21: LetterU,
        22: LetterV,
        23: LetterW,
        24: LetterX,
        25: LetterY,
        26: LetterZ}

try:
    import colorama
except ModuleNotFoundError:
    mars.Install("colorama")
    # </cmdInit>

    #<firstTimeSetup>
if mars.Setting.FirstTime == "0" or mars.Setting.FirstTime == "":
    mars.Stream("\n%s\n Welcome! / Witaj! /  Привет!\n Select a language below: / Wybierz język poniżej: / Выберите язык ниже:\n \"EN\" - English, \"PL\" - Polski, \"RU\" - Русский\n" % mars.Lang.EN.StartSC.MarsLogo % ("V"+mars.Setting.VerNum))
    while True:
        ftsAwser = mars.Collect("=> ")
        if ftsAwser.upper() == "EN":
            with open(".\\settingsMars.MCFG\\firstTmUp.ENT", 'w') as Lang:
                Lang.write("1")
                Lang.close()
            with open(".\\settingsMars.MCFG\\usrLangSel1.ENT", 'w') as ftSetup:
                ftSetup.write("EN")
                ftSetup.close()
            break
        # elif ftsAwser.upper() == "PL":
        #     with open(".\\settingsMars.MCFG\\firstTmUp.ENT", 'w') as Lang:
        #         Lang.write("1")
        #         Lang.close()
        #     with open(".\\settingsMars.MCFG\\usrLangSel1.ENT", 'w') as ftSetup:
        #         ftSetup.write("PL")
        #         ftSetup.close()
        #     break
        # elif ftsAwser.upper() == "RU":
        #     with open(".\\settingsMars.MCFG\\firstTmUp.ENT", 'w') as Lang:
        #         Lang.write("1")
        #         Lang.close()
        #     with open(".\\settingsMars.MCFG\\usrLangSel1.ENT", 'w') as ftSetup:
        #         ftSetup.write("RU")
        #         ftSetup.close()
        #     break
        else:
            mars.Clear()
            mars.Stream("\n There's no \"%s\" option! / Nie ma opcji \"%s\"! / Нет \"%s\" варианта!\n \"EN\" - English, \"PL\" - Polski, \"RU\" - Русский" % (ftsAwser, ftsAwser, ftsAwser))
elif mars.Setting.FirstTime == "1":
    pass
else:
    mars.Clear()
    mars.Stream("\n\n   GENERAL ERROR!! CFGRESTREQ#001")
    exit()
    #</firstTimeSetup>
    #<preStartPhase>

mars.Stream("[DEBUG INFO]:\n- firstTmUp.ENT: %s\n- usrLangSel1.ENT: %s" % (mars.Setting.FirstTime, mars.Setting.UserLang)) #nice
mars.Clear()
    #<classEN>
if mars.Setting.UserLang == "EN":
    mars.Stream("%s\n %s\n %s\n\n %s" % (mars.Lang.EN.StartSC.MarsLogo % ("V"+mars.Setting.VerNum),mars.Lang.EN.StartSC.WelcMSG,mars.Lang.EN.StartSC.SubWelcMSG,mars.Lang.EN.StartSC.DscWelcMSG))

    #</preStartPhase>
selectorAwsNum = -1
while True:
    while True:
        try:
            selectorAws = int(mars.Collect("\n=> "))
            # if selectorAws <= 4:
            #     selectorAwsNum = selectorAws
            #     break
            if selectorAws == 1 or selectorAws == 3:
                selectorAwsNum = selectorAws
                break
            elif selectorAws >= 2 and selectorAws <= 4:
                mars.Clear()
                mars.Stream(">> %s <<\n> %s" % (mars.Lang.EN.AlphaSC.AlphaMSG,mars.Lang.EN.SelectorSC.WrongAwsSub))
            elif selectorAws > 4:
                mars.Clear()
                mars.Stream("> %s\n> %s" % (mars.Lang.EN.SelectorSC.WrongAws,mars.Lang.EN.SelectorSC.WrongAwsSub))
            else:
                mars.Clear()
                mars.Stream("> %s\n> %s" % (mars.Lang.EN.SelectorSC.WrongAws,mars.Lang.EN.SelectorSC.WrongAwsSub))
        except ValueError:
            mars.Clear()
            mars.Stream("> %s\n> %s" % (mars.Lang.EN.SelectorSC.WrongAwsValue,mars.Lang.EN.SelectorSC.WrongAwsSub))
        except KeyboardInterrupt:
            mars.Stream("<Exitting AWS>")
            break
    mars.Clear()
    if selectorAwsNum == 1:
        while True:
            try:
                mars.Clear()
                randIndex = random.randint(1,26)
                selClass = mars.Lingo.Map[randIndex]
                mars.Stream("\n%s" % (mars.Lang.EN.QuizSC.CowSaysStart % selClass.Disp))
                charQuizAws = mars.Collect(" > ")
                if charQuizAws.upper() == selClass.Sound.upper():
                    mars.Clear()
                    mars.Stream("\n%s" % (mars.Lang.EN.QuizSC.CowSaysOK % (selClass.Disp,selClass.Sound)))
                    time.sleep(3.2)
                elif charQuizAws.upper() != selClass.Sound.upper():
                    mars.Clear()
                    mars.Stream("\n%s" % (mars.Lang.EN.QuizSC.CowSaysNo % (selClass.Disp,selClass.Sound)))
                    time.sleep(3.2)
                else:
                    mars.Stream("\n\n   GENERAL ERROR!! CFGRESTREQ#002")
                    break
            except KeyboardInterrupt:
                mars.Stream("\n\n<Exiting Quiz>")
                break
    elif selectorAwsNum == 3:
        mars.Clear()
        mars.Stream("\n %s\n Press [CTRL]+[C] to exit!" % mars.Lang.EN.TransSC.StartMSG)
        while True:
            try:
                
                transAws = mars.Collect("\n > ")
                try:
                    transAws = transAws.lower().replace("f", "ju")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("a", "fa")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("r", "su")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("m", "ra")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("n", "re")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("j", "na")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("e", "je")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("k", "ne")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("b", "fe")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("h", "ke")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("t", "te")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("d", "ja")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("g", "ka")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("s", "ta")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("q", "se")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("p", "sa")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("u", "tu")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("z", "ge")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("v", "za")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("w", "ze")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("x", "zu")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("y", "ga")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("c", "fu")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("i", "ku")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("o", "ru")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("l", "nu")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("natu", "ju")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("tatu", "su")
                except:
                    pass
                try:
                    transAws = transAws.lower().replace("rje", "re")
                except:
                    pass
                
                mars.Stream(transAws)
            except KeyboardInterrupt:
                mars.Stream("\n\n<Exitting Trans>")
                break
        pass
    break



    #</classEN>
    #
    #<classPL>
if mars.Setting.UserLang == "PL":
    mars.Stream(" %s" % (mars.Lang.PL.AlphaSC.AlphaMSG))
    #</preStartPhase>
    #</classPL>
    #
    #<classRU>
if mars.Setting.UserLang == "RU":
    mars.Stream(" %s" % (mars.Lang.RU.AlphaSC.AlphaMSG))
    #</preStartPhase>
    #</classRU>

mars.Collect("<Exitted>")