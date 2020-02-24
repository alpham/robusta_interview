import requests

def run(text):
    response = requests.post('http://backendtask.robustastudio.com/encode', json={
        'string': text
    })
    return response.json().get('string', '')