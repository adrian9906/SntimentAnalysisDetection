import speech_recognition as sr

def voiceToText(lang):
    
    r = sr.Recognizer()
    
    with sr.Microphone() as origin:
        r.pause_threshold = 0.8
        print("You can speak now")
        audio = r.listen(origin)
        
        try:
            googleSearch = r.recognize_google(audio,language=lang)
            return googleSearch
        
        except sr.UnknownValueError:
            if lang.__contains__('en'):
                print("ups, Sorry try again")
            elif lang.__contains__('es'):
                print("lo siento intenta otra vez")
            return 'still waiting'
        
        except sr.RequestError:
            if lang.__contains__('en'):
                print("ups Sorry bad request")
            elif lang.__contains__('es'):
                print("lo siento realiza la peticion nuevamente")
            return 'still waiting'
            
        except:
            if lang.__contains__('en'):
                print("sorry something went wrong")
            elif lang.__contains__('es'):
                print("lo siento algo fue mal")
            return 'still waiting'