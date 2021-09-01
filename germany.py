from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import random
import time
import sys
import os


URL = 'https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=pris&realmId=362'
PATH = '/Users/gentritmehmeti/chromedriver'
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36', 
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36', 
               'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36']
headers = {'User-Agent': random.choice(user_agents)}
driver = webdriver.Chrome(PATH)
list_of_links = []
generated_links = []
list_button_links = []
generated_button_links = []

def send_handle_request(url):
    global found
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    links_array = soup.find_all('a', class_='arrow')

    for i in links_array:
        list_of_links.append(i['href'])

    if len(list_of_links) > 4:
        for link in list_of_links:
            generated_links.append(f'https://service2.diplo.de/rktermin/{link}')
            control = "window.open('{0}')".format(f'https://service2.diplo.de/rktermin/{link}')
            driver.execute_script(control)
            driver.get(f"https://service2.diplo.de/rktermin/{link}")

        g_request = requests.get(generated_links[-1], headers=headers)
        if g_request.status_code == 200:
            body_req = BeautifulSoup(g_request.text, 'lxml')
            continue_buttons = body_req.find_all('a',{'class':'arrow', 'style':'float:right'})
            print(continue_buttons)
            if continue_buttons:
                for j in continue_buttons:
                    list_button_links.append(j['href'])
                for button in list_button_links:
                    generated_button_links.append(f'https://service2.diplo.de/rktermin/{button}')
                    script = "window.open('{0}')".format(f'https://service2.diplo.de/rktermin/{button}')
                    driver.execute_script(script)
        else:
            print('couldnt send request')
            
        found = True
        print(list_button_links)
    else:
        found = False
        print("doesn't exists yet")
        driver.quit()
    return found
 
if __name__=='__main__':
    send_handle_request(URL)
    if not found:
        os.execv(sys.executable, ['python'] + sys.argv)    


