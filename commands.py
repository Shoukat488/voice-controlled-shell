import os
import subprocess
import speech_recognition as sr
import webbrowser as wb
import controller

def commandExecute(text):
    s = ""
    ss = ""

    if "shutdown" in text:
        os.system("shutdown -h now")
        controller.text_to_speak("Shuting Down the PC.")
    elif 'exit' in text:
        controller.text_to_speak("Good Bye, Have a nice day")
        print("Good Bye")
        exit("Thank you")
    elif 'youtube' in text:
        controller.text_to_speak('What you want to search on YouTube')
        response = controller.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.youtube.com/results?search_query='+query
        wb.open_new_tab(url)
    elif 'google' in text:
        controller.text_to_speak('What you want to search on Google')
        response = controller.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.google.com/search?ei=aTLIXq3tGszCgweRtZ_IDw&q='+query
        wb.open_new_tab(url)
    elif 'close chrome' in text:
        browserExe = "chrome"
        controller.text_to_speak('Closing Chrome')
        os.system("pkill "+browserExe)
    elif 'close firefox' in text:
        browserExe = "firefox"
        controller.text_to_speak('Closing FireFox')
        os.system("pkill "+browserExe)
    elif "list files" in text:
        s = str(subprocess.os.system('ls'))
        print(s)
        controller.text_to_speak("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal")

    elif "list formated files" in text or "list file permissions" in text:
        s = str(subprocess.os.system(['ls', '-l']))
        print(s)
        controller.text_to_speak("All files present in the directory " + str(
            subprocess.os.system(['pwd'])) + " are displayed on terminal with permissions.")

    elif "list hidden files" in text:
        s = str(subprocess.check_output(['ls', '-a']))
        print(s)
        controller.text_to_speak("All hidden files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal.")
    elif "current working directory" in text or "where i am standing" in text:
        s = str(subprocess.check_output(['pwd']))
        print(s)

    elif "what is the date today" in text:
        s = str(subprocess.check_output(['date', '+%c']))
        print(s)
        controller.text_to_speak(s)

    elif "what is the day today" in text:
        s = str(subprocess.check_output(['date', '+%A']))
        print(s)
        controller.text_to_speak(s)

    elif "what is the time" in text:
        s = str(subprocess.check_output(['date', '+%T']))
        print(s)
        controller.text_to_speak(s)

    elif "calendar" in text:
        s = str(subprocess.check_output(['cal']))
        print(s)
        controller.text_to_speak("The Calendar for the " + str(subprocess.check_output(['date', '+%B'])) + " month and " + str(
            subprocess.check_output(['date', '+%Y'])) + " year is printed on the screen.")

    elif "what is the username" in text:
        s = str(subprocess.check_output(['whoami']))
        print(s)
        controller.text_to_speak("The user name is " + s)

    elif "what is the day" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%A")
        controller.text_to_speak("Today is " + s)
        print("Today is " + s)

    elif "what is the date" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%d %m %Y")
        controller.text_to_speak("Today is " + s)
        print("Today is " + s)

    elif "login as root user" in text:
        os.system("sudo -s")
        controller.text_to_speak("Type your password first")

    elif "list users" in text or "list all users" in text or "list user" in text:
        s = str(os.subprocess.check_output["ls", "/home"])
        print(s)
        controller.text_to_speak("List of users are " + s)

    elif "add user for login" in text:
        controller.text_to_speak("Tell the user name")
        res = controller.recognize_speech()
        name = str(res["transcription"])
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            controller.text_to_speak(
                res["transcription"] + " user already exists.")
            print(res + " user already exists.")
        else:
            ss = str(subprocess.check_output(['adduser', name]))
            print(ss)
            controller.text_to_speak("Sucessfully created the user.")

    elif "delete user" in text:
        controller.text_to_speak("Tell the user name")
        res = controller.recognize_speech()
        name = str(res["transcription"])
        r = "/home" + name
        if os.path.exists(r):
            controller.text_to_speak(
                "Are you sure you want to delete " + res + " ?")
            res1 = controller.recognize_speech()
            if "yes" in res1:
                ss = str(subprocess.check_output(['deluser', res]))
                print(ss)
                controller.text_to_speak("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                controller.text_to_speak("Unable to delete the file.")
        else:
            controller.text_to_speak(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "permanent delete user" in text:
        controller.text_to_speak("Tell the user name")
        res = controller.recognize_speech()
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            controller.text_to_speak(
                "Are you sure you want to permanent delete " + res + " ?")
            res1 = controller.recognize_speech()
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(
                    ['deluser', '-remove-home', res]))
                print(ss)
                controller.text_to_speak(
                    "Sucessfully permanent deleted the user.")
            else:
                print("You refused to permanent delete the file.")
                controller.text_to_speak("Unable to delete the file.")
        else:
            controller.text_to_speak(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "remove user from home" in text:
        controller.text_to_speak("Tell the user name")
        res = controller.recognize_speech()
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            controller.text_to_speak(
                "Are you sure you want to delete " + res + " ?")
            res1 = controller.recognize_speech()
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(['rm', r]))
                print(ss)
                controller.text_to_speak("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                controller.text_to_speak("Unable to delete the file.")

    elif "who created you" in text:
        s = "Following scientists created me:\n1. Saad Ismail\n2. Mehdi Raza Rajani\n3. Hassan Berry."
        controller.text_to_speak(s)
        print(s)
    else:
        print("No such command exist.")
        controller.text_to_speak("No such command exist.")
