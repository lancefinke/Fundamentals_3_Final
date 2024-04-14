from Car import Car
import requests

c1 = Car("Ford","Mustang","2014","red",51423,20955.87,"manual",1)





api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format(c1.getMake().lower(),c1.getModel().lower(),c1.getYear())
response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
data = response.json()
print(data)

