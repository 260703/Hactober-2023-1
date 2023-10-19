# this is a dummy project dont use it for production purpose 
# First, you'll need to install the speech_recognition library: "pip install SpeechRecognition"
#  (WARNING!!!)Make sure to have an active internet connection since this program relies on the Google Web Speech API for speech recognition.
#

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please start speaking...")
    audio = recognizer.listen(source, timeout=10)  # You can adjust the timeout as needed

# Use Google Web Speech API to recognize speech
try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said: " + recognized_text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
