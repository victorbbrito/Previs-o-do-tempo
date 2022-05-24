# Usando API do OpenWeather
import requests

API_KEY = 'd1dcb81a2157ca0c43b97d1b3e4a3944'
cidade = input("Informe o nome de uma Cidade: ")
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()

descricao = requisicao_dic['weather'][0]['description']
descricao = descricao.capitalize()
temperatura_kelvin = requisicao_dic['main']['temp']
temperatura_c = temperatura_kelvin - 273.15
temperatura_f = (temperatura_c * 9/5) + 32

print('Em {} temos {}'.format(cidade.capitalize(), descricao))
print('{:.2f} °C'.format(temperatura_c))
print('{:.2f} °F'.format(temperatura_f))
print('{:.2f} K'.format(temperatura_kelvin))
