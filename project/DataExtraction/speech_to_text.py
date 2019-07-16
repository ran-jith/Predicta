import speech_recognition as sr




def sound_input():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            #print("You said : {}".format(text))
            #print(str(text))
            return (str(text))
        except:
            print("Sorry could not recognize what you said")



