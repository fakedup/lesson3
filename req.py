import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print ('Returned status code: {}'.format(result.status_code))

if __name__ == '__main__':
	data = get_weather ('http://api.openweathermap.org/data/2.5/weather?id=524901&appid=03e701b8d073c289b7940e664344d261&units=metric')
	print (data)