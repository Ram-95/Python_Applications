# Dharani Scraping
import bs4 as bs
import requests
import csv
import os

Chelpur_ID = '2302006'  # Chelpur village
Mandal_ID = '429'   # Chelpur mandal
District_ID = '23'  # Jangaon
Pattadar_passbook_number = 'T23020060641'
khata_number = '60641'

new_url = 'https://dharani.telangana.gov.in/getPublicDataInfo?villageId=2302006&flagToSearch=surveynumber&searchData=17/A&flagval=district&district=23&mandal=429&divi=&khataNoIdselect=60641&ReqType=Citizen'

##filename = 'Yellamla_land_details.csv'
##head = ['District', 'Mandal', 'Village', 'Survey No.', 'Pattadar Name', 'Father/Husband Name', 'Total Extent(Ac. Gts)', 'Land Status', 'Market Value']
### Writing the header to the file
##with open(filename, 'w') as f:
##    writer = csv.writer(f, delimiter= ',', lineterminator= '\n')
##    writer.writerow([x for x in head])
##
##headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
##survey_url = 'https://dharani.telangana.gov.in/getSurveyCitizen?villId=2302006&flag=survey'
##response = requests.get(survey_url, headers)
##html = response.text
##soup = bs.BeautifulSoup(html, 'lxml')
##
##x = soup.findAll('option')
##survey_ids = []
##
##for i in x:
##    survey_ids.append(i.text)
##
##survey_ids = survey_ids[1:]
##
###print(f'{survey_ids[1:10]}')
##
##
##''' Getting the Land Details '''
##
##for i in range(len(survey_ids)):
##    survey_no = survey_ids[i]
##    land_url = 'https://dharani.telangana.gov.in/getPublicDataInfo?villageId=2302006&flagToSearch=surveynumber&searchData=2302006&flagval=district&district=23&mandal=429&divi='
##    #print(land_url)
##
##    # Getting data from the URL
##    response = requests.get(land_url, headers)
##    html = response.text
##    soup = bs.BeautifulSoup(html, 'lxml')
##
##    d = soup.findAll('div', class_='col-12')
##    details = []
##    for i in d:
##        temp = i.text
##        try:
##            value = ' '.join(temp.split('\r')[1].split())
##            details.append(value)
##        except IndexError:
##            continue
##    
##    # Writing the details to the CSV file
##    with open(filename, 'a', encoding="utf-8") as f:
##        writer = csv.writer(f, delimiter= ',', lineterminator='\n')
##        writer.writerow(details)
##    
##
##print(f'\nFile writing complete\n')
