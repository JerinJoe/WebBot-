import requests
from bs4 import BeautifulSoup

# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# soup = BeautifulSoup(r.content, 'html.parser')


with open('index.html', 'r') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')
    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        course_title = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_title} + costs + {course_price}')