from Car import Car
import requests







api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format("ford","mustang","2014")
response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
data = response.json()
print(data)

