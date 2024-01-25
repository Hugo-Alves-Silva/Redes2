import requests
text = 'build a network with a single topology with 2 nodes'
r = requests.get(f'http://cb93-34-91-134-74.ngrok-free.app?sentence={text}')
print(r.text)
print(type(r.text))
