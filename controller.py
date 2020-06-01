from gtts import gTTS
import speech_recognition as sr
import os

def recognize_speech():
    rcgn = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        rcgn.adjust_for_ambient_noise(source)
        audio = rcgn.listen(source)

    response = {
        "success": True,
        "error": None,
        "text": None
    }

    try:
        response["transcription"] = rcgn.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


def text_to_speak(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("text_to_voice.mp3")
    os.system("mpg321 -q text_to_voice.mp3")
