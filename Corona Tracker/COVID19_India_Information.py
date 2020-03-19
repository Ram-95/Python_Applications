#COVID 19 India Cases
import requests
import bs4 as bs
import csv
import os
from datetime import date
from prettytable import PrettyTable


filename = 'COVID-19_India_Data.csv'
today = date.today().strftime("%B %d, %Y")


url = "http://www.mohfw.gov.in/"
response = requests.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'lxml')

x = soup.find('ol').findAll('p')


tbl = soup.find('table')
t_items = tbl.findAll('tr')
head = ['S.No', 'State/UT', 'Indian Cases', 'Foreign Cases', 'Discharged', 'Dead', 'Total Cases']


#Creating a Table
ind_table = PrettyTable(head)
summ_table = PrettyTable(['Total', 'Indian Cases', 'Foreign Cases', 'Discharged', 'Dead', 'Total Cases'])

for i in t_items[1:len(t_items)-1]:
    data = []
    for k in i.findAll('td'):
        data.append(k.text.strip())
    data.append(int(data[2]) + int(data[3]))
    ind_table.add_row(data)


print('\n' + '*'*20 + ' INDIA - STATE WISE INFORMATION ' + x[-1].text.strip() + ' ' + '*'*20 + '\n')
print(f'{ind_table}')

summ = []
for j in t_items[-1].findAll('td'):
    summ.append(j.text.strip())

total_cases = int(summ[1]) + int(summ[2])
summ.append(total_cases)

summ_table.add_row(summ)

print(f'\nSummary:\n{summ_table}')
print(f'\n[OFFICIAL DATA] - {x[1].text.strip()}\n')

'''Code for writing to the Files.'''
#Creating the CSV File if not already present
files = os.listdir()
deaths = int(summ[4])


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
