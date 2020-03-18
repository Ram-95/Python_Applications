#COVID 19 India Cases
import requests
import bs4 as bs
from prettytable import PrettyTable


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


print('\n' + '*'*20 + ' INDIA - STATE WISE INFORMATION ' + x[-1].text.strip()  + '*'*20 + '\n')
print(f'{ind_table}')

summ = []
for j in t_items[-1].findAll('td'):
    summ.append(j.text.strip())
summ.append(int(summ[1]) + int(summ[2]))

summ_table.add_row(summ)

print(f'\nSummary:\n{summ_table}')
print(f'\n[OFFICIAL DATA] - {x[1].text.strip()}\n')
