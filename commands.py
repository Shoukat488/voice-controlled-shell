from selenium import webdriver
import os
import subprocess
import index
import speech_recognition as sr
import webbrowser as wb
def runCommand(text):
    s = ""
    ss = ""

    if "shutdown" in text:
        os.system("shutdown -h now")
        index.text_to_speak("Shuting Down the PC.")
    elif 'exit' in text:
        index.text_to_speak("Good Bye")
        index.text_to_speak("Have a nice day")
        print("Good Bye")
        exit("Thank you")
    elif 'youtube' in text:
        index.text_to_speak('What you want to search on YouTube')
        response = index.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.youtube.com/results?search_query='+query
        wb.open_new_tab(url)
    elif 'google' in text:
        index.text_to_speak('What you want to search on Google')
        response = index.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.google.com/search?ei=aTLIXq3tGszCgweRtZ_IDw&q='+query
        wb.open_new_tab(url)
    elif 'close chrome' in text:
        browserExe = "chrome"
        index.text_to_speak('Closing Chrome')
        os.system("pkill "+browserExe)
    elif 'close firefox' in text:
        browserExe = "firefox"
        index.text_to_speak('Closing FireFox')
        os.system("pkill "+browserExe)
    elif "list files" in text:
        s = str(subprocess.os.system('ls'))
        print(s)
        index.text_to_speak("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal")

    elif "list formated files" in text or "list file permissions" in text:
        s = str(subprocess.os.system(['ls', '-l']))
        print(s)
        index.text_to_speak("All files present in the directory " + str(
            subprocess.os.system(['pwd'])) + " are displayed on terminal with permissions.")

    elif "list hidden files" in text:
        s = str(subprocess.check_output(['ls', '-a']))
        print(s)
        index.text_to_speak("All hidden files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal.")
    elif "current working directory" in text or "where i am standing" in text:
        s = str(subprocess.check_output(['pwd']))
        print(s)

    elif "what is the date today" in text:
        s = str(subprocess.check_output(['date', '+%c']))
        print(s)
        index.text_to_speak(s)

    elif "what is the day today" in text:
        s = str(subprocess.check_output(['date', '+%A']))
        print(s)
        index.text_to_speak(s)

    elif "what is the time" in text:
        s = str(subprocess.check_output(['date', '+%T']))
        print(s)
        index.text_to_speak(s)

    elif "calendar" in text:
        s = str(subprocess.check_output(['cal']))
        print(s)
        index.text_to_speak("The Calendar for the " + str(subprocess.check_output(['date', '+%B'])) + " month and " + str(
            subprocess.check_output(['date', '+%Y'])) + " year is printed on the screen.")

    elif "what is the username" in text:
        s = str(subprocess.check_output(['whoami']))
        print(s)
        index.text_to_speak("The user name is " + s)

    elif "what is the day" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%A")
        index.text_to_speak("Today is " + s)
        print("Today is " + s)

    elif "what is the date" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%d %m %Y")
        index.text_to_speak("Today is " + s)
        print("Today is " + s)

    elif "login as root user" in text:
        os.system("sudo -s")
        index.text_to_speak("Type your password first")

    elif "list users" in text or "list all users" in text or "list user" in text:
        s = str(os.subprocess.check_output["ls", "/home"])
        print(s)
        index.text_to_speak("List of users are " + s)

    elif "add user for login" in text:
        index.text_to_speak("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.text_to_speak(
                res["transcription"] + " user already exists.")
            print(res + " user already exists.")
        else:
            ss = str(subprocess.check_output(['adduser', name]))
            print(ss)
            index.text_to_speak("Sucessfully created the user.")

    elif "delete user" in text:
        index.text_to_speak("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + name
        if os.path.exists(r):
            index.text_to_speak(
                "Are you sure you want to delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1:
                ss = str(subprocess.check_output(['deluser', res]))
                print(ss)
                index.text_to_speak("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                index.text_to_speak("Unable to delete the file.")
        else:
            index.text_to_speak(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "permanent delete user" in text:
        index.text_to_speak("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.text_to_speak(
                "Are you sure you want to permanent delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(
                    ['deluser', '-remove-home', res]))
                print(ss)
                index.text_to_speak(
                    "Sucessfully permanent deleted the user.")
            else:
                print("You refused to permanent delete the file.")
                index.text_to_speak("Unable to delete the file.")
        else:
            index.text_to_speak(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "remove user from home" in text:
        index.text_to_speak("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.text_to_speak(
                "Are you sure you want to delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(['rm', r]))
                print(ss)
                index.text_to_speak("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                index.text_to_speak("Unable to delete the file.")

    elif "who created you" in text:
        s = "Following scientists created me:\n1. Saad Ismail\n2. Mehdi Raza Rajani\n3. Hassan Berry."
        index.text_to_speak(s)
        print(s)
    else:
        print("No such command exist.")
        index.text_to_speak("No such command exist.")
