import speech_recognition as sr

record = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something! I will convert your voice to text!!!!')
    audio = record.listen(source)
    print ('Hoollllaaa wait you text is generated......')
    
text = record.recognize_google(audio)
print (text)