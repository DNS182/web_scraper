import time
from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=django'
# data = requests.get(url).json()
# jobs = data.find('header' , class_='clearfix')
# print(jobs)

# data = requests.get(url).text
# vals = BeautifulSoup(data , 'lxml')
# jobs = vals.find_all('li' , class_='clearfix job-bx wht-shd-bx')
# print(jobs)
def scrape():
    rem =input("Skills to be removed:")
    data = requests.get(url).text
    vals = BeautifulSoup(data , 'lxml')
    jobs = vals.find_all('li' , class_='clearfix job-bx wht-shd-bx')
    for index , job in enumerate(jobs): 
        experience = job.find('li').text[11::].replace(' ' , '')
        if '0' in experience:
            name = job.find('h2').text
            posted_on = job.find('span' ,'sim-posted').text
            link = job.find('h2').a['href']
            skill = job.find('span' , class_='srp-skills').text.replace(' ' ,'')
            if rem not in skill:
                with open(f'{index}.txt' ,'w')as f:
                    f.write(f"NAME :{name.strip()}\n")
                    f.write( f"POSTED :{posted_on.strip()}\n")
                    f.write( f"EXPERiENCE :{experience.strip()}\n")
                    f.write(f"Skills: {skill.strip()}\n")
                    f.write(f"LINK : {link}\n")

if __name__ == '__main__':
    while True:
        scrape()
        time_to_wait = 10
        print(f"Wait Every {time_to_wait} sec to run again")
        time.sleep(time_to_wait * 1)
