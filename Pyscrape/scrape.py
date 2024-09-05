import requests
from bs4 import BeautifulSoup

# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
# print(soup.prettify())

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup = BeautifulSoup(r.content, 'html.parser')


s = soup.find('div',class_ = 'entry-content')
# content = s.find_all('p')
# print(s)
if s:
    content = s.find_all('p')
    for paragraph in content:
        print(paragraph.text)
else:
    print("Could not find the div with class 'entry-content'")

