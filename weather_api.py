import requests
import json
import win32com.client as wincom
city=input('enter the name of city:')
url=f"https://api.weatherapi.com/v1/current.json?key=ed3481e001d045b697d143714230208&q={city}"
r=requests.get(url)
print(type(r))
print(r.text)
wdic=json.loads(r.text)
speak=wincom.Dispatch("SAPI.SpVoice")
#print(wdic["current"]["temp_c"])
#speak.Speak(wdic["current"]["temp_c"])

for e in wdic.keys():
    speak.Speak(e)
    print(e,':')
    for k,v in wdic[e].items():
        if k=="condition":
            for i,j in wdic["current"][k].items():
                speak.Speak(k)
                speak.Speak(i)
                speak.Speak(j)
                print(k,':',i,'=',j)
        else:
            speak.Speak(k)
            speak.Speak(v)
            print(k,'=',v)