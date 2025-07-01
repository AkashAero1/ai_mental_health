import pyttsx3
import speech_recognition as sr

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # speaking speed
    engine.setProperty('voice', engine.getProperty('voices')[1].id)  # optional: choose voice
    engine.say(text)
    engine.runAndWait()

def record_voice_input(timeout=5):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return "Listening timed out."
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."
