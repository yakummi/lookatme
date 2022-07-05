import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.lookatme.ru/')
soup = BeautifulSoup(response.text, "html.parser")
work = soup.find_all('div', 'g-item g-item-post g-item-v featured height-300')
# print(work)
for directory in work:
    title = directory.find('div', 'title').text
    print(title)
    thema = directory.find('div', 'flow').text
    print(thema)
    views = directory.find('li', 'item-meta meta-views-counter').text
    print('Просмотров:',views)
    comments = directory.find('li', 'item-meta meta-comments-counter').text
    print('Комментарии:',comments)
    test = directory.find()
    print('-'*20)