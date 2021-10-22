# Flipkart Items Price finder - Prints the price of the item from the URL given as arguments.

#Necessary Modules
import bs4 as bs
import urllib.request
import os

def flipkart_price(url):
    ''' Prints the price of the Items' URLs provided as argument.'''
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    #Getting the name of the item
    item_name = soup.find('p').text

    #Getting the price of item
    price = soup.find('div', class_ = '_30jeq3 _16Jk6d').text

    msg = "Current price of \"{}\" is: Rs. {}/-".format(item_name, price)
    print(msg)

#List of URLs of items on Flipkart.
my_list = ['https://www.flipkart.com/redmi-8-onyx-black-64-gb/p/itmaf669d074ff27',           
'https://www.flipkart.com/puma-flip-flops/p/itme8e4bba87778c?pid=SFFFHUNYAEH5K7KC&lid=LSTSFFFHUNYAEH5K7KCMJNJGK&marketplace=FLIPKART&store=osp%2Fcil&srno=b_1_2&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_4.dealCard.OMU_P44HQ9IPWEIN_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_3&fm=neo%2Fmerchandising&iid=e55f055b-fb3c-4f3a-9810-f9a098386d8d.SFFFHUNYAEH5K7KC.SEARCH&ppt=browse&ppn=browse&ssid=vuxg3ldyio0000001623222842094',
           
        ]

for i in my_list:
    flipkart_price(i)


