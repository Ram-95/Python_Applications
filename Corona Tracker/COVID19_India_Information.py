#COVID 19 India Cases
import requests
import bs4 as bs
from prettytable import PrettyTable


url = "http://www.mohfw.gov.in/"
response = requests.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'lxml')

x = soup.find('ol').select_one("li:nth-of-type(2)").text.split(')')[0]
l_items = x.split('(')

tbl = soup.find('table')
t_items = tbl.findAll('tr')
head = ['S.No', 'State/UT', 'Indian Cases', 'Foreign Cases', 'Discharged', 'Dead']


#Creating a Table
ind_table = PrettyTable(head)
summ_table = PrettyTable(['Total', 'Indian Cases', 'Foreign Cases', 'Discharged', 'Dead'])

for i in t_items[1:len(t_items)-1]:
    data = []
    for k in i.findAll('td'):
        data.append(k.text.strip())
    ind_table.add_row(data)

print('{}({})\n'.format(l_items[0].strip('\t'), l_items[1].strip()))
print(f'{ind_table}')

summ = []
for j in t_items[-1].findAll('td'):
    summ.append(j.text.strip())

summ_table.add_row(summ)

print(f'\nSummary:\n{summ_table}')
