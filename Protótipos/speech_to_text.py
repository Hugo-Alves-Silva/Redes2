import speech_recognition as sr
#import pyttsx3

r = sr.Recognizer()

def record_text():
    while(True):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2)
                return myText
        except sr.RequestError as e:
            print("Could not request results;{0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")

text = record_text()
#output_text(text)
print(text)
#print("Wrote text")
