import pyttsx3

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
rate=engine.getProperty("rate")
engine.setProperty("rate",rate-80)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def readlinesfromfile(f):
    #f="file.txt"
    filehandle=open(f,'r')
    lines=filehandle.readlines()
    for line in lines:
        speak(line)

readlinesfromfile("file.txt")