#COVID 19 India Cases
import requests
import bs4 as bs
from prettytable import PrettyTable
import Slack_Push_Notification as Slack


url = "http://www.mohfw.gov.in/"
response = requests.get(url)
html = response.text
soup = bs.BeautifulSoup(html, 'lxml')

l_items = soup.find('ol').select_one("li:nth-of-type(2)").findAll('p')


tbl = soup.find('table')
t_items = tbl.findAll('tr')
head = ['S.No', 'State/UT', 'Indian Cases', 'Foreign Cases', 'Discharged', 'Dead']


#Creating a Table
ind_table = PrettyTable(head)

for i in t_items[1:len(t_items)-1]:
    data = []
    for k in i.findAll('td'):
        data.append(k.text.strip())
    ind_table.add_row(data)

print(f"{l_items[1].text.strip()} ({l_items[0].text.split(',')[1].strip()}")
print(f'{ind_table}')
