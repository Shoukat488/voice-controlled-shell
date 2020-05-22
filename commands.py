import os
import subprocess
import App
import speech_recognition as sr


def runCommand(text):
    s = ""
    ss = ""

    if "shutdown" in text:
        os.system("shutdown -h now")
        App.speak_to_speaker("Shuting Down the PC.")
    elif 'exit' in text:
        App.speak_to_speaker("Good Bye")
        App.speak_to_speaker("Have a nice day")
        print("Good Bye")
        exit("Thank you")
    elif "list files" in text:
        s = str(subprocess.check_output(['ls']))
        print(s)
        App.speak_to_speaker("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal")

    elif "list formated files" in text or "list file permissions" in text:
        s = str(subprocess.check_output(['ls', '-l']))
        print(s)
        App.speak_to_speaker("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal with permissions.")

    elif "list hidden files" in text:
        s = str(subprocess.check_output(['ls', '-a']))
        print(s)
        App.speak_to_speaker("All hidden files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal.")

    elif "current working directory" in text or "where i am standing" in text:
        s = str(subprocess.check_output(['pwd']))
        print(s)

    elif "what is the date today" in text:
        s = str(subprocess.check_output(['date', '+%c']))
        print(s)
        App.speak_to_speaker(s)

    elif "what is the day today" in text:
        s = str(subprocess.check_output(['date', '+%A']))
        print(s)
        App.speak_to_speaker(s)

    elif "what is the time" in text:
        s = str(subprocess.check_output(['date', '+%T']))
        print(s)
        App.speak_to_speaker(s)

    elif "calendar" in text:
        s = str(subprocess.check_output(['cal']))
        print(s)
        App.speak_to_speaker("The Calendar for the " + str(subprocess.check_output(['date', '+%B'])) + " month and " + str(
            subprocess.check_output(['date', '+%Y'])) + " year is printed on the screen.")

    elif "what is the username" in text:
        s = str(subprocess.check_output(['whoami']))
        print(s)
        App.speak_to_speaker("The user name is " + s)


    elif "what is the day" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%A")
        App.speak_to_speaker("Today is " + s)
        print("Today is " + s)

    elif "what is the date" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%d %m %Y")
        App.speak_to_speaker("Today is " + s)
        print("Today is " + s)

    

    elif "login as root user" in text:
        os.system("sudo -s")
        App.speak_to_speaker("Type your password first")

    elif "list users" in text or "list all users" in text or "list user" in text:
        s = str(os.subprocess.check_output["ls", "/home"])
        print(s)
        App.speak_to_speaker("List of users are " + s)

    elif "add user for login" in text:
        App.speak_to_speaker("Tell the user name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            App.speak_to_speaker(
                res["transcription"] + " user already exists.")
            print(res + " user already exists.")
        else:
            ss = str(subprocess.check_output(['adduser', name]))
            print(ss)
            App.speak_to_speaker("Sucessfully created the user.")

    elif "delete user" in text:
        App.speak_to_speaker("Tell the user name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + name
        if os.path.exists(r):
            App.speak_to_speaker(
                "Are you sure you want to delete " + res + " ?")
            res1 = App.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1:
                ss = str(subprocess.check_output(['deluser', res]))
                print(ss)
                App.speak_to_speaker("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                App.speak_to_speaker("Unable to delete the file.")
        else:
            App.speak_to_speaker(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "permanent delete user" in text:
        App.speak_to_speaker("Tell the user name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            App.speak_to_speaker(
                "Are you sure you want to permanent delete " + res + " ?")
            res1 = App.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(
                    ['deluser', '-remove-home', res]))
                print(ss)
                App.speak_to_speaker(
                    "Sucessfully permanent deleted the user.")
            else:
                print("You refused to permanent delete the file.")
                App.speak_to_speaker("Unable to delete the file.")
        else:
            App.speak_to_speaker(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "remove user from home" in text:
        App.speak_to_speaker("Tell the user name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            App.speak_to_speaker(
                "Are you sure you want to delete " + res + " ?")
            res1 = App.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(['rm', r]))
                print(ss)
                App.speak_to_speaker("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                App.speak_to_speaker("Unable to delete the file.")

    elif "who created you" in text:
        s = "Following scientists created me:\n1. Saad Ismail\n2. Mehdi Raza Rajani\n3. Hassan Berry."
        App.speak_to_speaker(s)
        print(s)
        
    else:
        print("No such command exist.")
        App.speak_to_speaker("No such command exist.")
