#WHO Data
import csv
import requests
import bs4 as bs
from datetime import date
from prettytable import PrettyTable
import os
import Slack_Push_Notification as Slack

filename = 'COVID-19_Global_Data.csv'

today = date.today().strftime("%d-%b-%y")


table = PrettyTable(['S.No', 'Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious/Critical'])

url= "https://www.worldometers.info/coronavirus/"

response = requests.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'lxml')

t_items = soup.find('table', id="main_table_countries_today").findAll('tr')
sno = 0
india = []

for i in t_items[1:len(t_items)-1]:
    sno += 1
    country = i.select_one("td:nth-of-type(1)").text.strip()
    total_cases =  i.select_one("td:nth-of-type(2)").text.strip()
    new_cases = 0 if i.select_one("td:nth-of-type(3)").text.strip() == '' else i.select_one("td:nth-of-type(3)").text.strip()
    deaths = 0 if i.select_one("td:nth-of-type(4)").text.strip() == '' else i.select_one("td:nth-of-type(4)").text.strip()
    new_deaths = 0 if i.select_one("td:nth-of-type(5)").text.strip() == '' else i.select_one("td:nth-of-type(5)").text.strip()
    total_recovered = 0 if i.select_one("td:nth-of-type(6)").text.strip() == '' else i.select_one("td:nth-of-type(6)").text.strip()
    active_cases = 0 if i.select_one("td:nth-of-type(7)").text.strip() == '' else i.select_one("td:nth-of-type(7)").text.strip()
    serious = 0 if i.select_one("td:nth-of-type(8)").text.strip() == '' else i.select_one("td:nth-of-type(8)").text.strip()

    table.add_row([sno, country, total_cases, new_cases, deaths, new_deaths, total_recovered, active_cases, serious])
    
    if country == 'India':
        india.append(country)
        india.append(total_cases)
        india.append(new_cases)
        india.append(deaths)
        

#Information about India
country = t_items[-1].select_one("td:nth-of-type(1)").text.strip()
total_cases =  t_items[-1].select_one("td:nth-of-type(2)").text.strip()
deaths = t_items[-1].select_one("td:nth-of-type(4)").text.strip()
new_cases = t_items[-1].select_one("td:nth-of-type(3)").text.strip()

print(table)
print(f'\n{country} {total_cases}\tDeaths: {deaths}')


#Creating the CSV File if not already present
files = os.listdir()

if filename not in files:
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['DATE', 'TOTAL_CASES', 'DEATHS'])
        print(f'\nCSV File Created Successfully.\n')



#Reading the CSV File
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',', lineterminator='\n')
    data = list(reader)
    #print(f'{data}')
    

if data[-1][0] == 'DATE':
    with open(filename, 'a') as f:
        writer = csv.writer(f, delimiter = ',', lineterminator = '\n')
        writer.writerow([today, int(total_cases.replace(',', '')), int(deaths.replace(',', ''))])
        
else:
    if data[-1][0] == today:
        data[-1][1] = str(max(int(data[-1][1].replace(',', '')), int(total_cases.replace(',', ''))))
        data[-1][2] = str(max(int(data[-1][2].replace(',', '')), int(deaths.replace(',', ''))))
        #print(f'{data}')
        with open(filename, 'w') as f:
            wr = csv.writer(f, delimiter= ',', lineterminator='\n')
            for item in data:
                wr.writerow(item)
    else:
        with open(filename, 'a') as f:
            writer = csv.writer(f, delimiter = ',', lineterminator = '\n')
            writer.writerow([today, int(total_cases.replace(',', '')), int(deaths.replace(',', ''))])
    

msg = f'{country} {total_cases}\tDeaths: {deaths}\n\n{india[0]}\tCases: {india[1]}({india[2]})\tDeaths: {india[3]}'
Slack.slack_message(msg, __file__)
print(f'{india[0]} --> Cases: {india[1]}({india[2]})\tDeaths: {india[3]}')


ch = input('\n\nDo you want to know India\'s COVID-19 State wise Information ?(y/n): \n')
if ch.lower() == 'y':
    import COVID19_India_Information as COVID_Ind

