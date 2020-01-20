import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
    if 'love' in text:
        print('I love you too')