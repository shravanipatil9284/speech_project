import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Adjusting for background noise... please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎧 Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)   # or recognize_sphinx for offline
        print("📝 You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("😅 Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("⚠️ Recognition service unavailable.")
        return ""

# --- Main loop ---
while True:
    command = listen()
    if not command:
        continue

    if "hello" in command:
        speak("Hello! How are you?")
    elif "your name" in command:
        speak("I am your speech assistant.")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break
    else:
        speak("You said " + command)
