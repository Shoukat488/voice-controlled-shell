from gtts import gTTS
import speech_recognition as sr
import random
import os
import time
import commands


def recognize_speech():
    rcgn = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        rcgn.adjust_for_ambient_noise(source)
        audio = rcgn.listen(source)

    result = {
        "success": True,
        "error": None,
        "text": None
    }

    try:
        result["transcription"] = rcgn.recognize_google(audio)
    except sr.RequestError:
        result["success"] = False
        result["error"] = "API unavailable"
    except sr.UnknownValueError:
        result["error"] = "Unable to recognize speech"

    return result

def text_to_speak(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("text_to_voice.mp3")
    os.system("mpg321 -q text_to_voice.mp3")


def beep_high():
    os.system("mpg321 -q beep_hi.mp3")


def beep_low():
    os.system("mpg321 -q beep_lo.mp3")


if __name__ == "__main__":
    os.system('clear')
    print('Welcome to Voice commmand shell.\n How can I help you? ')
    text_to_speak('Welcome to Voice commmand shell, How can I help you? ')
    while (1):
        response = recognize_speech()

        if response["error"]:
            print("Sorry, we can't recognize you, Please try again")
            continue

        text = str(format(response["transcription"])).lower()
        print("You said:" + text)

        while (1):
            response = recognize_speech()
            if response["error"]:
                print("Sorry, we can't recognize you, Please try again")
                continue

            text = str(format(response["transcription"])).lower()
            print("You said:" + text)
            commands.runCommand(text)
