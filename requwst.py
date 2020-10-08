import requests
import pandas
import matplotlib
import scipy
response = requests.get('https://www.kinopoisk.ru/recommend/?tab=all')
response.encoding('utf-8')
response.text
print(response)