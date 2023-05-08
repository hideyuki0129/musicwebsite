import requests
import base64

client_id = '8bb72fc6e33e445aafe27cd10c296708'
client_secret = '21221a4b17734c8b8adb90d406ccb056'

credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'client_credentials'
}

response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
response_data = response.json()
access_token = response_data['access_token']
print("Access Token:", access_token)
