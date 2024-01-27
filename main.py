import speech_recognition as sr
import requests
from fabric import Connection

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

def find_command(response):
    inicio = response.find("sudo")
    for i in range(inicio, len(response)):
        if response[i] == "'": 
            fim = i
            break
    return response[inicio:fim]

my_url = "http://ece0-34-141-196-39.ngrok-free.app"
vm_ip = "192.168.100.12"
continuar = "yes"        

while continuar.lower() == "yes":        
    my_text = record_text()
    print("Text: ", my_text)

    my_response = requests.get(f"{my_url}?sentence={my_text}")
    my_response = my_response.text
    print("Response: ", my_response)

    my_command = find_command(my_response)
    print("Command: ", my_command)
    with Connection(vm_ip, port=22, user="mininet", connect_kwargs={"password": "mininet"}) as c:
        c.run(my_command, pty=True)
    continuar = input("Continue?(yes/no):")
