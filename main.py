import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('Hi there, what can I do for you?')

def take_commnand():
    try:
        with sr.Microphone() as source:
            #talk('Hi there, What can I do for you?')
            print('Alexa is Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_commnand()
    print('command')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        talk('Current time is '+ time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Pardon, could you please repeat?')

while True:
    run_alexa()