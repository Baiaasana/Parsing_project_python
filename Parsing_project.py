import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('Yell_ge.csv', 'w', encoding='UTF-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(["კლინიკის დასახელება", "ადგილმდებარეობა", "ცხელი ხაზი"])

for i in range(1, 8):
    url = 'https://www.yell.ge/companies.php?lan=geo&rub=174&SI_1=თბილისი&SR_pg=' + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    # print(soup)
    box = soup.find('div', class_="col-md-9 m-0 px-0")
    containers = box.find_all('div', class_="container px-0 pt-0 pb-3")
    for container in containers:
        title = container.find('div', align="left").a.text
        location = container.find('span', style="cursor:pointer;font-size:14px;color:#000000; ").text
        try:
            tel = container.find('div', class_="tel_font_companies").text
        except AttributeError:
            tel = container.find('span', class_="tel_font_companies").text

        file_obj.writerow([title, location, tel])
sleep(randint(12, 18))
file.close()
