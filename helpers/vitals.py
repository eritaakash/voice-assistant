import speech_recognition as spr
import pyttsx3 as tts

def init():
    print('\n\n')
    speak('Hello, How can I help you?')

def listen():
    r = spr.Recognizer()
    mic = spr.Microphone()

    try:

        with mic as source:
            print('[!]: Say something...')

            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            r.recognize_google(audio)

            text = r.recognize_google(audio)
            print('[?]: You said: ', text)

            return text
    
    except spr.UnknownValueError:
        print('[!]: Sorry, I did not get that...')
        return 'Sorry, I did not get that...'
    

    
def speak(text):
    print('[!]: Assistant: ', text, '\n\n')
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()