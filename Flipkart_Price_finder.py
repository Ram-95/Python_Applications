# Flipkart Items Price finder - Prints the price of the item from the URL given as arguments.

#Necessary Modules
import bs4 as bs
import urllib.request
import os
import Slack_Push_Notification as Slack
global msg
def flipkart_price(url):
    ''' Prints the price of the Items' URLs provided as argument.'''
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    global msg
    #Getting the name of the item
    item_name = soup.find('p').text

    #Getting the price of item
    price = soup.find('div', class_ = '_1vC4OE _3qQ9m1').text

    msg = "Current price of \"{}\" is: Rs. {}/-".format(item_name, price)
    print(msg)

#List of URLs of items on Flipkart.
my_list = ['https://www.flipkart.com/redmi-8-onyx-black-64-gb/p/itmaf669d074ff27',           
        ]

for i in my_list:
    flipkart_price(i)


'''
    url = 'https://www.flipkart.com/adidas-adiray-m-running-shoes-men/p/itmf7g8fxnxydsuc?pid=SHOF7G8FYPMJTE45&lid=LSTSHOF7G8FYPMJTE458RA8CT&marketplace=FLIPKART&spotlightTagId=TrendingId_osp%2Fcil&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_ISKSFOA9MJUY_0&fm=neo%2Fmerchandising&iid=633f9421-e711-4aab-8d4b-900ac8af91f8.SHOF7G8FYPMJTE45.SEARCH&ppt=StoreBrowse&ppn=Store&ssid=kkwtb7mn5c0000001552810060372'

    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    getting the name of item
    item_name = soup.find('p').text

    getting the price
    price = soup.find('div', class_ = '_1vC4OE _3qQ9m1').text

    print("Current price of \"{}\" is: Rs. {}/-".format(item_name, price))

'''
# To get the current file name: os.path.basename(__file__)
# Entire Directory: __file__

Slack.slack_message(msg, __file__)
