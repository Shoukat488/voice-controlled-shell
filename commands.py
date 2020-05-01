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

    elif "create a random file" in text:
        s = str(subprocess.check_output(['touch', '-t']))
        print(s)
        App.speak_to_speaker("A file has been created in " +
                             str(subprocess.check_output(['pwd'])))

    elif "go to home directory" in text:
        os.system("cd /home")
        #s = str(subprocess.check_output(['cd','/home']))
        # print(s)
        App.speak_to_speaker("Your have moved to home directory.")

    elif "go to root directory" in text:
        os.system("cd /")
        print("Your have moved to root directory.")
        App.speak_to_speaker("Your have moved to root directory.")

    elif "go to my directory" in text:
        os.system("cd ~")
        print("Your have moved to your directory.")
        App.speak_to_speaker("Your have moved to your directory.")

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

    elif "run ps" in text:
        s = str(subprocess.check_output(['ps', '-A']))
        print(s)
        App.speak_to_speaker("All processes are shown in the terminal")

    elif "show network status" in text:
        s = str(subprocess.check_output(['ifconfig']))
        print(s)
        App.speak_to_speaker("Network configuration is shown in the terminal")

    elif "create a link" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            App.speak_to_speaker("What do you want to name the link?")
            res1 = App.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            name1 = res1["transcription"]
            os.system("ls -s "+name+" "+name1)
            print("Sucessfully created the link.")
            App.speak_to_speaker("Sucessfully created the link.")
        else:
            App.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "delete a file" in text or "remove a file" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        print(res["transcription"])
        name = res["transcription"]
        if os.path.exists(name):
            App.speak_to_speaker(
                "Are you sure you want to delete " + name + " ?")
            res1 = App.recognize_speech_from_mic(
                sr.Recognizer(), sr.Microphone())
            name1 = res1["transcription"]
            if "yes" in name1:
                os.system("rm " + name1)
                print("Sucessfully deleted the file.")
                App.speak_to_speaker("Sucessfully deleted the file.")
            else:
                print("You refused to delete the file.")
                App.speak_to_speaker("Unable to delete the file.")
        else:
            App.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "create a file" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            App.speak_to_speaker(name + " already exsists.")
        else:
            os.system("touch " + name)
            App.speak_to_speaker(name + "file is created.")
            print(name + "file is created.")

    elif "just open nano editor" in text:
        os.system("nano")
        App.speak_to_speaker("Nano editor is opened")

    elif "just open gedit editor" in text:
        os.system("gedit")
        App.speak_to_speaker("Gedit editor is opened")

    elif "just open sublime editor" in text:
        os.system("subl")
        App.speak_to_speaker("Sublime editor is opened")

    elif "open nano editor" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['nano', res]))
        App.speak_to_speaker(res + "file is opened.")

    elif "open gedit editor" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['gedit', res["transcription"]]))
        App.speak_to_speaker(res["transcription"] + "file is opened.")

    elif "open sublime editor" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        res["transcription"] += ".*"
        ss = str(subprocess.check_output(['subl', res["transcription"]]))
        App.speak_to_speaker(res["transcription"] + "file is opened.")

    elif "tell me the file type" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = res["transcription"]
        if os.path.exists(name):
            ss = str(subprocess.check_output(['file', name]))
            App.speak_to_speaker(name + "file type is " + ss)
            print(ss)
        else:
            App.speak_to_speaker("Unable to find the file.")
            print("Unable to find the file.")

    elif "maunal" in text:
        App.speak_to_speaker("Tell the command name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        ss = str(subprocess.check_output(['man', res["transcription"]]))
        print(ss)

    elif "what is the status and configuration of network" in text:
        os.system('ifconfig')

    elif "make a new directory" in text:
        App.speak_to_speaker("Tell the file name")
        res = App.recognize_speech_from_mic(sr.Recognizer(), sr.Microphone())
        name = str(res["transcription"])
        if os.path.exists(name):
            App.speak_to_speaker(name + " already exsists.")
        else:
            ss = str(subprocess.check_output(['mkdir', name]))
            App.speak_to_speaker(name + "directory is created.")
            print(ss)

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
        # App.speak_to_speaker("Do you want to see any of the creator")
        # res = App.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        # name = res["transcription"]
        # print(name)
        # if 'yes' in name:
        # 	ss = "You want to see whom?"
        # 	print(ss)
        # 	App.speak_to_speaker(ss)
        # 	print("Call any name")
        # 	print("saad mehdi berry")
        # 	name = App.recognize_speech_from_mic(sr.Recognizer(),sr.Microphone())
        # 	name = name["transcription"]
        # 	if "saad" in name:
        # 		os.system("eog saad.jpg")
        # 	elif "mehdi" in name:
        # 		os.system("eog mehdi.jpg")
        # 	elif "berry" in name:
        # 		os.system("eog berry.jpg")
        # 	else:
        # 		print("You called invalid person")
        # 		App.speak_to_speaker("You called invalid person.")
        # else:
        # 	print("Exiting")
        # 	App.speak_to_speaker("Exiting.")

    else:
        print("No such command exist.")
        App.speak_to_speaker("No such command exist.")
