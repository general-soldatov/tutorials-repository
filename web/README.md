# Парсинг веб-страниц с помощью библиотеки beautifullsoup

Установим библиотеку:
```bash
pip install beautifulsoup4==4.12.3
```
Теперь импортируем библиотеку вначале файла
```python
from bs4 import BeautifulSoup
```
Если файл html содержится в каталоге, то можно воспользоваться контекстным менеджером:
```python
with open('file_path.html', 'r', encoding='utf-8') as page:
    soup = BeautifulSoup(page.read(), "html.parser")
```
Если же вы хотите подгрузить html-разметку с хостинга, то воспользуемся библиотекой `requests`:
```python
import requests
from bs4 import BeautifulSoup

url = 'http://example.com/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
```
Можно найти элемент с помощью метода `find`, он в качестве аргументов принимает тег, а в качестве необязательных - class_, id_:
```python
data = soup.find('table',class_='dsnode-table')
```
## Полезные ссылки
* Пример парсинга [таблицы с сайта](https://qna.habr.com/q/826703).  
* Примеры [скриптов для парсинга](https://python-scripts.com/beautifulsoup-parsing)
* 
