#COVID 19 India Cases
import requests
import bs4 as bs
import csv
import os
from datetime import date
from prettytable import PrettyTable


filename = 'COVID-19_India_Data.csv'
state_filename = 'COVID-19_State_wise_Information.csv'

today = date.today().strftime("%d-%b-%y")


url = "http://www.mohfw.gov.in/"
response = requests.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'lxml')

x = soup.find('div', class_= 'content newtab').find('p').text.strip()


t_items = soup.find('div', class_= 'content newtab').find('table').find('tbody').findAll('tr')
head = ['S.No', 'State/UT', 'Total Active Cases', 'Discharged', 'Dead', 'Total Cases']


#Creating a Table
ind_table = PrettyTable(head)
summ_table = PrettyTable(['Total', 'Total Active Cases', 'Discharged', 'Dead', 'Total Cases'])


b = soup.findAll('div', class_='iblock_text')
india_total = b[1].find('div').text.strip() + '(considering only Indian Citizens) = ' + b[1].find('span').text

#Writing the state wise information to a file
with open(state_filename, 'w') as f:
    writer = csv.writer(f, delimiter= ',', lineterminator= '\n')
    writer.writerow([x.upper() for x in head])


for i in t_items[:len(t_items)-1]:
    state_data = []
    for k in i.findAll('td'):
        state_data.append(k.text.strip())
    state_data.append(int(state_data[2]) + int(state_data[3]) + int(state_data[4]))
    ind_table.add_row(state_data)

    with open(state_filename, 'a') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(state_data)


print('\n' + '*'*20 + ' INDIA - STATE WISE INFORMATION ' + x + ' ' + '*'*20 + '\n')
print(f'{ind_table}')

summ = []
for j in t_items[-1].findAll('td'):
    summ.append(j.text.strip())

total_cases = int(summ[1].replace('#', '')) + int(summ[2].replace('#', '')) + int(summ[3].replace('#', ''))
summ.append(total_cases)

summ_table.add_row(summ)

print(f'\nSummary:\n{summ_table}')
print(f'\n[OFFICIAL DATA] - {india_total}\n')



'''Code for writing to the Files.'''
#Creating the CSV File if not already present
files = os.listdir()
deaths = int(summ[3])


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
        writer.writerow([today, total_cases, deaths])
        
else:
    if data[-1][0] == today:
        data[-1][1] = str(max(int(data[-1][1].replace(',', '')), total_cases))
        data[-1][2] = str(max(int(data[-1][2].replace(',', '')), deaths))

        with open(filename, 'w') as f:
            wr = csv.writer(f, delimiter= ',', lineterminator='\n')
            for item in data:
                wr.writerow(item)
    else:
        with open(filename, 'a') as f:
            writer = csv.writer(f, delimiter = ',', lineterminator = '\n')
            writer.writerow([today, total_cases, deaths])


