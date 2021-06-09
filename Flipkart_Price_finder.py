# Flipkart Items Price finder - Prints the price of the item from the URL given as arguments.

#Necessary Modules
import bs4 as bs
import urllib.request
import os

def flipkart_price(url):
    ''' Prints the price of the Items' URLs provided as argument.'''
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    global msg
    #Getting the name of the item
    item_name = soup.find('p').text

    #Getting the price of item
    price = soup.find('div', class_ = '_30jeq3 _16Jk6d').text

    msg = "Current price of \"{}\" is: Rs. {}/-".format(item_name, price)
    print(msg)

#List of URLs of items on Flipkart.
my_list = ['https://www.flipkart.com/redmi-8-onyx-black-64-gb/p/itmaf669d074ff27',           
        ]

for i in my_list:
    flipkart_price(i)
