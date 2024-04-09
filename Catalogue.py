from Car import Car as car
import requests

c1 = car("Ford","Mustang","2014","red",51423,"manual",1)

print(c1.getMiles())
c1.setMiles(4641)
print(c1.getMiles())


model = 'mustang'
year = '2014'
make='ford'
api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format(make,model,year)
response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
data = response.json()
print(data[0]['class'])

