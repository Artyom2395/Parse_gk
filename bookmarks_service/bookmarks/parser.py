import requests
from bs4 import BeautifulSoup
import json


def parse_link(url):
    
    # Загружаем HTML-код страницы
    response = requests.get(url)
    html = response.text
    shema = url
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Изначально устанавливаем значения по умолчанию
    title = 'Пусто'
    description = 'Пусто'
    favicon = None

    # Поиск title и описания
    title_1 = soup.find('meta', attrs={'property': 'og:title'})
    title_2 = soup.find('title')
    description_1 = soup.find('meta', attrs={'property': 'og:description'})
    description_2 = soup.find('meta', attrs={'name': 'description'})
    schema_data = soup.find('script', attrs={'type': 'application/ld+json'})

    if title_1:
        title = title_1['content']
    elif title_2:
        title = title_2.text

    if description_1:
        description = description_1['content']
    elif description_2:
        description = description_2['content']
    elif schema_data:
       schema_data = schema_data.string
       parsed_data = parse_ldjson(schema_data)
       description = parsed_data['description']
       

    # Поиск иконки
    icon_2 = soup.find('meta', attrs={'property': 'og:image'})
    icon = soup.find('link', href=lambda value: value and 'favicon' in value and value.lower().endswith('.ico'))
    
    
    if icon_2:
        favicon = icon_2['content']
    elif icon:
        # Извлекаем значение атрибута href
        if shema[-1] == '/':
            shema = shema[:-1]
            favicon = shema + icon['href']
        else:
            favicon = shema + icon['href']
    elif schema_data:
        schema_data = schema_data.string
        parsed_data = parse_ldjson(schema_data)
        favicon = parsed_data['image'] if 'image' in parsed_data else parsed_data['image_0']
    
    return title, description, favicon  
    
#Функция для развертывания данных в application/ld+json
def parse_ldjson(data):
    parsed_data = {}

    def parse_nested(data, prefix=''):
        if isinstance(data, dict):
            for key, value in data.items():
                new_prefix = prefix + '_' + key if prefix else key
                parse_nested(value, new_prefix)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_prefix = prefix + '_' + str(i) if prefix else str(i)
                parse_nested(item, new_prefix)
        else:
            parsed_data[prefix] = data

    # Парсинг данных
    json_data = json.loads(data)
    parse_nested(json_data)

    return parsed_data