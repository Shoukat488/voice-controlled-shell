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
        index.speak_to_speaker("Shuting Down the PC.")
    elif 'exit' in text:
        index.speak_to_speaker("Good Bye")
        index.speak_to_speaker("Have a nice day")
        print("Good Bye")
        exit("Thank you")
    elif 'youtube' in text:
        index.speak_to_speaker('What you want to search on YouTube')
        response = index.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.youtube.com/results?search_query='+query
        wb.open_new_tab(url)
    elif 'google' in text:
        index.speak_to_speaker('What you want to search on Google')
        response = index.recognize_speech()
        query = str(format(response["transcription"])).lower()
        url = 'https://www.google.com/search?ei=aTLIXq3tGszCgweRtZ_IDw&q='+query
        wb.open_new_tab(url)
    elif "list files" in text:
        s = str(subprocess.check_output(['ls']))
        print(s)
        index.speak_to_speaker("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal")

    elif "list formated files" in text or "list file permissions" in text:
        s = str(subprocess.check_output(['ls', '-l']))
        print(s)
        index.speak_to_speaker("All files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal with permissions.")

    elif "list hidden files" in text:
        s = str(subprocess.check_output(['ls', '-a']))
        print(s)
        index.speak_to_speaker("All hidden files present in the directory " + str(
            subprocess.check_output(['pwd'])) + " are displayed on terminal.")

    elif "current working directory" in text or "where i am standing" in text:
        s = str(subprocess.check_output(['pwd']))
        print(s)

    elif "what is the date today" in text:
        s = str(subprocess.check_output(['date', '+%c']))
        print(s)
        index.speak_to_speaker(s)

    elif "what is the day today" in text:
        s = str(subprocess.check_output(['date', '+%A']))
        print(s)
        index.speak_to_speaker(s)

    elif "what is the time" in text:
        s = str(subprocess.check_output(['date', '+%T']))
        print(s)
        index.speak_to_speaker(s)

    elif "calendar" in text:
        s = str(subprocess.check_output(['cal']))
        print(s)
        index.speak_to_speaker("The Calendar for the " + str(subprocess.check_output(['date', '+%B'])) + " month and " + str(
            subprocess.check_output(['date', '+%Y'])) + " year is printed on the screen.")

    elif "what is the username" in text:
        s = str(subprocess.check_output(['whoami']))
        print(s)
        index.speak_to_speaker("The user name is " + s)

    elif "create a random file" in text:
        s = str(subprocess.check_output(['touch', '-t']))
        print(s)
        index.speak_to_speaker("A file has been created in " +
                               str(subprocess.check_output(['pwd'])))

    elif "go to home directory" in text:
        os.system("cd /home")
        # s = str(subprocess.check_output(['cd','/home']))
        # print(s)
        index.speak_to_speaker("Your have moved to home directory.")

    elif "go to root directory" in text:
        os.system("cd /")
        print("Your have moved to root directory.")
        index.speak_to_speaker("Your have moved to root directory.")

    elif "go to my directory" in text:
        os.system("cd ~")
        print("Your have moved to your directory.")
        index.speak_to_speaker("Your have moved to your directory.")

    elif "what is the day" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%A")
        index.speak_to_speaker("Today is " + s)
        print("Today is " + s)

    elif "what is the date" in text:
        import datetime
        now = datetime.datetime.now()
        s = now.strftime("%d %m %Y")
        index.speak_to_speaker("Today is " + s)
        print("Today is " + s)

    elif "run ps" in text:
        s = str(subprocess.check_output(['ps', '-A']))
        print(s)
        index.speak_to_speaker("All processes are shown in the terminal")

    elif "show network status" in text:
        s = str(subprocess.check_output(['ifconfig']))
        print(s)
        index.speak_to_speaker(
            "Network configuration is shown in the terminal")

    elif "create a link" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            index.speak_to_speaker("What do you want to name the link?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            name1 = res1["transcription"]
            os.system("ls -s "+name+" "+name1)
            print("Sucessfully created the link.")
            index.speak_to_speaker("Sucessfully created the link.")
        else:
            index.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "delete a file" in text or "remove a file" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        print(res["transcription"])
        name = res["transcription"]
        if os.path.exists(name):
            index.speak_to_speaker(
                "Are you sure you want to delete " + name + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            name1 = res1["transcription"]
            if "yes" in name1:
                os.system("rm " + name1)
                print("Sucessfully deleted the file.")
                index.speak_to_speaker("Sucessfully deleted the file.")
            else:
                print("You refused to delete the file.")
                index.speak_to_speaker("Unable to delete the file.")
        else:
            index.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "create a file" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            index.speak_to_speaker(name + " already exsists.")
        else:
            os.system("touch " + name)
            index.speak_to_speaker(name + "file is created.")
            print(name + "file is created.")

    elif "just open nano editor" in text:
        os.system("nano")
        index.speak_to_speaker("Nano editor is opened")

    elif "just open gedit editor" in text:
        os.system("gedit")
        index.speak_to_speaker("Gedit editor is opened")

    elif "just open sublime editor" in text:
        os.system("subl")
        index.speak_to_speaker("Sublime editor is opened")

    elif "open nano editor" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['nano', res]))
        index.speak_to_speaker(res + "file is opened.")

    elif "open gedit editor" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['gedit', res["transcription"]]))
        index.speak_to_speaker(res["transcription"] + "file is opened.")

    elif "open sublime editor" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['subl', res["transcription"]]))
        index.speak_to_speaker(res["transcription"] + "file is opened.")

    elif "tell me the file type" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            ss = str(subprocess.check_output(['file', name]))
            index.speak_to_speaker(name + "file type is " + ss)
            print(ss)
        else:
            index.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "maunal" in text:
        index.speak_to_speaker("Tell the command name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        ss = str(subprocess.check_output(['man', res["transcription"]]))
        print(ss)

    elif "what is the status and configuration of network" in text:
        os.system('ifconfig')

    elif "make a new directory" in text:
        index.speak_to_speaker("Tell the file name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        if os.path.exists(name):
            index.speak_to_speaker(name + " already exsists.")
        else:
            ss = str(subprocess.check_output(['mkdir', name]))
            index.speak_to_speaker(name + "directory is created.")
            print(ss)

    elif "login as root user" in text:
        os.system("sudo -s")
        index.speak_to_speaker("Type your password first")

    elif "list users" in text or "list all users" in text or "list user" in text:
        s = str(os.subprocess.check_output["ls", "/home"])
        print(s)
        index.speak_to_speaker("List of users are " + s)

    elif "add user for login" in text:
        index.speak_to_speaker("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.speak_to_speaker(
                res["transcription"] + " user already exists.")
            print(res + " user already exists.")
        else:
            ss = str(subprocess.check_output(['adduser', name]))
            print(ss)
            index.speak_to_speaker("Sucessfully created the user.")

    elif "delete user" in text:
        index.speak_to_speaker("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        r = "/home" + name
        if os.path.exists(r):
            index.speak_to_speaker(
                "Are you sure you want to delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1:
                ss = str(subprocess.check_output(['deluser', res]))
                print(ss)
                index.speak_to_speaker("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                index.speak_to_speaker("Unable to delete the file.")
        else:
            index.speak_to_speaker(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "permanent delete user" in text:
        index.speak_to_speaker("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.speak_to_speaker(
                "Are you sure you want to permanent delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(
                    ['deluser', '-remove-home', res]))
                print(ss)
                index.speak_to_speaker(
                    "Sucessfully permanent deleted the user.")
            else:
                print("You refused to permanent delete the file.")
                index.speak_to_speaker("Unable to delete the file.")
        else:
            index.speak_to_speaker(res + " user does not exists.")
            print(res + " user does not exists.")

    elif "remove user from home" in text:
        index.speak_to_speaker("Tell the user name")
        res = index.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        r = "/home" + res["transcription"]
        if os.path.exists(r):
            index.speak_to_speaker(
                "Are you sure you want to delete " + res + " ?")
            res1 = index.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            if "yes" in res1["transcription"]:
                ss = str(subprocess.check_output(['rm', r]))
                print(ss)
                index.speak_to_speaker("Sucessfully deleted the user.")
            else:
                print("You refused to delete the file.")
                index.speak_to_speaker("Unable to delete the file.")

    elif "who created you" in text:
        s = "Following scientists created me:\n1. Saad Ismail\n2. Mehdi Raza Rajani\n3. Hassan Berry."
        index.speak_to_speaker(s)
        print(s)
        # index.speak_to_speaker("Do you want to see any of the creator")
        # res = index.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        # name = res["transcription"]
        # print(name)
        # if 'yes' in name:
        # 	ss = "You want to see whom?"
        # 	print(ss)
        # 	index.speak_to_speaker(ss)
        # 	print("Call any name")
        # 	print("saad mehdi berry")
        # 	name = index.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        # 	name = name["transcription"]
        # 	if "saad" in name:
        # 		os.system("eog saad.jpg")
        # 	elif "mehdi" in name:
        # 		os.system("eog mehdi.jpg")
        # 	elif "berry" in name:
        # 		os.system("eog berry.jpg")
        # 	else:
        # 		print("You called invalid person")
        # 		index.speak_to_speaker("You called invalid person.")
        # else:
        # 	print("Exiting")
        # 	index.speak_to_speaker("Exiting.")

    else:
        print("No such command exist.")
        index.speak_to_speaker("No such command exist.")
