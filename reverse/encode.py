import requests

def run(text):
    response = requests.post('http://backendtask.robustastudio.com/decode', json={
        'string': text
    })
    return response.json().get('string', '')