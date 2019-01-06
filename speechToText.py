import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something! I will convert your voice to text!!!!')
    audio = r.listen(source)
    print ('Hoollllaaa wait you text is generated......')
    
text = r.recognize_google(audio)
print (text)