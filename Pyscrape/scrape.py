import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# soup = BeautifulSoup(r.content, 'html.parser')


with open('index.html', 'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)