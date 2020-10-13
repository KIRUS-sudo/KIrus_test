import requests
from bs4 import BeautifulSoup

bank_id = 10990073

url = f'https://www/banki.ru/services/questions-answer/?id= (bank_id)'
r = requests.get(url)
with open('test.html', 'w') as output_file:
    output_file.write(r.text)