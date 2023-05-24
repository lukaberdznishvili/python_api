import requests
import json
key = '981375208a2c94cd519b546a0c240380'
city = 'Gori'
cnt = 16
response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={cnt}&appid={key}')
payload = {'q': city, 'appid': key, 'units':'metric'}
response = requests.get('https://api.openweathermap.org/data/2.5/forcast', params=payload)
print(response)
print(response.status_code)
print(response.url)
print(response.headers)
print(response.text)
print(type(response.text))
result = response.json()
print(json.dumps(result, indent=10))



with open('weather.json', 'w') as file:
    json.dump(result, file, indent=4)

result = json.loads(response.text)
print(type(result))
with open('weather.json', 'r') as file:
    result = json.load(file)
    print(result)