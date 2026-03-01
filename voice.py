import speech_recognition as sr
import pyttsx3
import re  

tts_model = pyttsx3.init()
sr_model = sr.Recognizer()

def speak(text):
    tts_model.say(text)
    tts_model.runAndWait()

def input_voice():
    with sr.Microphone() as source:
        print("Listening for voice input...")
        sr_model.adjust_for_ambient_noise(source)
        audio = sr_model.listen(source)

        try:
            text = sr_model.recognize_google(audio)
            print("Recognized Voice Input:", text)
            number = re.findall(r'\d+', text)
            if number:
                print(f"Detected Number: {number[0]}")
                return text
            else:
                return None
        except sr.UnknownValueError:
            speak("Could not understand the audio.")
            return None
        except sr.RequestError:
            speak("Network error.")
            return None


