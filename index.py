import speech_recognition as sr
import os
import controller
import commands

os.system('clear')
print('Welcome to Voice commmand shell.\n How can I help you? ')
controller.text_to_speak('Welcome to Voice commmand shell, How can I help you? ')
while (True):
    response = controller.recognize_speech()

    if response["error"]:
        print("Sorry, we can't recognize you, Please try again")
        continue

    text = str(format(response["transcription"])).lower()
    print("You: " + text)
    commands.commandExecute(text)
