import requests
import bs4 as bs
import time
from prettytable import PrettyTable

print(f"*********************** INDIA vs. AUSTRALIA Live Score ************************\n")

def score_details():
    url="https://www.cricbuzz.com/live-cricket-scores/22332/indw-vs-ausw-final-icc-womens-t20-world-cup-2020"

    response = requests.get(url)
    html = response.text
    soup = bs.BeautifulSoup(html, 'lxml')
    
    #Extracting the score and the Batsman details
    score = soup.find('div', class_= 'cb-min-bat-rw')
    info = soup.findAll('div', class_= 'cb-min-itm-rw')

    table = PrettyTable(['Batsman', 'Runs(Balls)', '4s', '6s', 'Strike Rate'])
    
    #Extracting the Batsmen Details
    for i in range(2):
        batsman = info[i].select_one("div:nth-of-type(1)").text.strip()
        runs = info[i].select_one("div:nth-of-type(2)").text.strip()
        balls = info[i].select_one("div:nth-of-type(3)").text.strip()
        fours = info[i].select_one("div:nth-of-type(4)").text.strip()
        sixes = info[i].select_one("div:nth-of-type(5)").text.strip()
        sr = info[i].select_one("div:nth-of-type(6)").text.strip()

        table.add_row([batsman, runs + '(' + balls + ')', fours, sixes, sr])


    print(f'Score: {score.text.strip()}\n')
    print(table)
    print(45*'+ ')


'''Driver Code - Calls the score function every 30 seconds.'''
x = 0
while x < 10:
    score_details()
    x += 1
    time.sleep(25)
