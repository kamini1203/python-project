import win32com.client as wincom
print("welcome to robospeaker 1.1. crated by Nisha")
while(True):
    x=input("enter what you want me to pronounce:")
    speak=wincom.Dispatch("SAPI.SpVoice")
    if x=='p':
        print(speak.Speak('bye bye friend'))
        break
    speak.Speak(x)