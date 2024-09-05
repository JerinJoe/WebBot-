from bs4 import BeautifulSoup
import requests
import time
# bring html text of that specific page

print("put skill not familiar with")
unfamiliar_skill = input('>')
print(f'Fitering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):

        published_date = job.find('span',class_= 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_= 'srp-skills').text.replace(' ','')
            # debug print(published_date)
            more_info = job.header.h2.a['href']
            if unfamiliar_skill.lower() not in skills.lower():
                with open(f'posts/{index}.txt','w') as f:
                    # print(f"Company name: {company_name.strip()}")
                    # print(f"Required Skills: {skills.strip()}")
                    # print(f"more Info : {more_info}")
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"more Info : {more_info}\n")
                print(f"Saved post {index}")
                    

    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f"Waiting {time_wait} minutes")
        time.sleep(time_wait * 60)