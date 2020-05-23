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
        "transcription": None
    }

    try:
        result["transcription"] = rcgn.recognize_google(audio)
    except sr.RequestError:
        result["success"] = False
        result["error"] = "API unavailable"
    except sr.UnknownValueError:
        result["error"] = "Unable to recognize speech"

    return result


def speak_to_speaker(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("tts.mp3")
    os.system("mpg321 -q tts.mp3")

def beep_high():
    os.system("mpg321 -q beep_hi.mp3")

def beep_low():
    os.system("mpg321 -q beep_lo.mp3")


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    os.system('clear')
    speak_to_speaker('Welcome to Voice commmand shell')
    speak_to_speaker('How can I help you?')
    print('How can I help you?')
    while (1):
        response = recognize_speech()

        if response["error"]:
            print("Sorry, we are unable to recognize you. Please say command again")
            continue

        text = str(format(response["transcription"])).lower()
        print("You said:" + text)

        # if ('hello' in text):
        #     beep_high()

        while (1):
            response = recognize_speech()
            if response["error"]:
                print("Sorry, we are unable to recognize you. Please say command again")
                continue

            text = str(format(response["transcription"])).lower()
            print("You said:" + text)
            commands.runCommand(text)
            # break
        # break
        # beep_low()
