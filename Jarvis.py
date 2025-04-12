import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import random
from sgs import songs

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(a):
    engine.say(a)
    engine.runAndWait()

def open(a):
    if(a.lower()=="open google"):
        webbrowser.open("http://google.com")
    elif(a.lower()=="open youtube"):
        webbrowser.open("http://youtube.com")
    else:
        speak("i cant understand")

def play(a):
    song=a.lower().split(" ")[1]
    link=songs[song]
    webbrowser.open(link)

def news(a):
    webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")

def cal(n):
    a=int(n.split(" ")[0])
    b=int(n.split(" ")[2])
    
    if("+"in n):
        print(a+b)
        speak(str(a+b))
    elif("-" in n):
        print(a-b)
        speak(str(a-b))
    elif("*" in n):
        print(a*b)
        speak(str(a*b))
    elif("/" in n):
        print(a/b)
        speak(str(a/b))
    else:
        pass
    
def table(a):
    n=a.lower().split(" ")[2]
    n=int(n)
    for i in range(1,11):
        speak(f"{n} x {i} = {n*i}") 

def ran_num(n):
    a=int(n.split(" ")[3])
    b=int(n.split(" ")[5])
    d=random.randint(a,b)
    print(d)
    speak(str(d))

          
if __name__=="__main__":
    speak("Hye..this is friday how can i help you..")
    while True:
        with sr.Microphone() as source:
            print("hearing.......")
            # speak("hearing.")
            audio=r.listen(source)
            
        try:
            cmd=r.recognize_google(audio)
            print(cmd)
            
            if("friday" in cmd.lower()):
                a="Yeh, i am here to assist you.."
                b="hello i m listening.."
                c="i am friday as for assistance in your work.."
                d=random.choice([a,b,c])
                speak(d)

            elif(cmd.lower().startswith("open")):
                open(cmd)
            
            elif(cmd.lower().startswith("play")):
                play(cmd)
                
            elif("news" in cmd.lower()):
                news(cmd)
            
            elif("jokes" in cmd.lower()):
                jok=(pyjokes.get_joke())
                print(jok)
                speak(jok)
            
            elif("table" in cmd.lower()):
                table(cmd)

            elif("+" in cmd.lower() or "-" in cmd.lower() or "*" in cmd.lower()):
                cal(cmd)
            
            elif("random number" in cmd.lower()):
                ran_num(cmd)

            elif("thank" in cmd.lower()):
                print("Its my plearure")
                speak("its my pleasure")

            else:
                print("I am not understanding")
                speak("I am not understanding")
                
        except Exception as e:
            print("say it again")
            # speak("say it again")