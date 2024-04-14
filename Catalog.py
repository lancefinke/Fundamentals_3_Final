from Car import Car
import requests



car1 = Car("toyota","camry","2011","white",95426,5000.00,"automatic",1)
print(car1.getVerification())
car1.verify()
print(car1.getVerification())



'''api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format("ford","mustang","2014")
response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
data = response.json()
print(data)'''

