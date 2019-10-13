# Flipkart Items Price finder - Prints the price of the item from the URL given as arguments.

#Necessary Modules
import bs4 as bs
import urllib.request


def flipkart_price(url):
    ''' Prints the price of the Items' URLs provided as argument.'''
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    #Getting the name of the item
    item_name = soup.find('p').text

    #Getting the price of item
    price = soup.find('div', class_ = '_1vC4OE _3qQ9m1').text

    print("Current price of \"{}\" is: Rs. {}/-".format(item_name, price))

#List of URLs of items on Flipkart.
my_list = ['https://www.flipkart.com/samsung-galaxy-s9-plus-coral-blue-64-gb/p/itmf33a6qhrkyth3?pid=MOBF2VWVHDAZRQGH&srno=b_1_1&otracker=hp_omu_Top%2BOffers%2BOn%2BMobiles_3_7.dealCard.OMU_YZLF8ZJ051G3_7&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers%2BOn%2BMobiles_NA_dealCard_cc_3_NA_view-all_7&lid=LSTMOBF2VWVHDAZRQGHCF6TXA&fm=neo%2Fmerchandising&iid=6ef955c2-b372-4b94-92ca-3b6131ecb748.MOBF2VWVHDAZRQGH.SEARCH&ppt=browse&ppn=browse&ssid=gtpkjmcy9c0000001570971060174',
           'https://www.flipkart.com/redmi-note-7s-astro-moonlight-white-32-gb/p/itm5e8bac3bcf4c4?pid=MOBFJFZDP9R3Z7YK&lid=LSTMOBFJFZDP9R3Z7YKQJSH2X&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Top%2BOffers_2_3.dealCard.OMU_88559FM66S42_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=2af1c4be-4b89-454e-95ed-09de21c5962f.MOBFJFZDP9R3Z7YK.SEARCH&ppt=browse&ppn=browse&ssid=s8tyw8t4fk0000001570970986200',
           'https://www.flipkart.com/sherlock-holmes-complete-novels-stories-volume/p/itmf3jbqsvdktrsn?pid=9780553212419&lid=LSTBOK9780553212419QAWDRK&marketplace=FLIPKART&srno=s_1_13&otracker=AS_QueryStore_OrganicAutoSuggest_0_15&fm=SEARCH&iid=7fc6db9f-ec7d-42c1-b9e8-ba0fde32b658.9780553212419.SEARCH&ppt=Homepage&ppn=Homepage&ssid=esl8lszfjk0000001552810927096&qH=e717ef139779e544',
           'https://www.flipkart.com/moto-z2-play-lunar-gray-64-gb/p/itmevt7xuk6xv3e7?pid=MOBEU9WRFZNAP2MJ&srno=s_1_4&otracker=search&lid=LSTMOBEU9WRFZNAP2MJVK3CZ5&fm=SEARCH&iid=a3be6899-5ef4-43a9-9dcd-ba4a059f63b1.MOBEU9WRFZNAP2MJ.SEARCH&ppt=SearchPage&ppn=Search&ssid=mmswc1u8cg0000001552811023594&qH=de88b155ee0c683f',
           'https://www.flipkart.com/highlander-men-s-checkered-casual-black-grey-shirt/p/itmfekrxkpxpdgg8?pid=SHTEZG79ZQGTFHZH&lid=LSTSHTEZG79ZQGTFHZHR9ENLK&marketplace=FLIPKART&srno=b_1_5&otracker=nmenu_sub_Men_0_Shirts&fm=neo%2Fmerchandising&iid=17c3cbcd-70f7-417c-b5a0-8453205cff2a.SHTEZG79ZQGTFHZH.SEARCH&ppt=StoreBrowse&ppn=Store&ssid=qi0y9l3wkw0000001552811061578',
           'https://www.flipkart.com/metronaut-men-solid-casual-blue-shirt/p/itmf5xtgj8h8syw7?pid=SHTF5XTGHYNPUED9&lid=LSTSHTF5XTGHYNPUED95AHKNN&marketplace=FLIPKART&srno=b_1_15&otracker=nmenu_sub_Men_0_Shirts&fm=neo%2Fmerchandising&iid=0ce9785f-4582-400d-a2a6-c62d2cb5296e.SHTF5XTGHYNPUED9.SEARCH&ppt=StoreBrowse&ppn=Store',
           'https://www.flipkart.com/jbl-t500-bluetooth-headset-mic/p/itmfa2ppt5rnagmz?pid=ACCFA2PPHMFS853G&lid=LSTACCFA2PPHMFS853GJ0MJDC&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3AACCEXBNK9ZZMUN4Y%3Bpt%3Ahp%3Buid%3Acc5c75ee-873e-7918-14ee-c15a54cd7e54%3B.ACCFA2PPHMFS853G.LSTACCFA2PPHMFS853GJ0MJDC&otracker=hp_reco_You%2BMay%2BLike_2_JBL%2BT500%2BBluetooth%2BHeadset%2Bwith%2BMic_ACCFA2PPHMFS853G.LSTACCFA2PPHMFS853GJ0MJDC_3&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_You%2BMay%2BLike_DESKTOP_HORIZONTAL_productCard_cc_2_NA_3&cid=ACCFA2PPHMFS853G.LSTACCFA2PPHMFS853GJ0MJDC',
           'https://www.flipkart.com/adidas-solonyx-2-0-m-running-shoes-men/p/itmf3xmjyg7mggry?pid=SHOEVMGGZJGEJZGA&lid=LSTSHOEVMGGZJGEJZGAOCO5LD&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3ASHOF7G8FYPMJTE45%3Bpt%3Ahp%3Buid%3Af50ba4c4-e9f0-25f4-a824-23a9151b1bf6%3B.SHOEVMGGZJGEJZGA.LSTSHOEVMGGZJGEJZGAOCO5LD&otracker=hp_reco_Suggested%2BItems_5_ADIDAS%2BSOLONYX%2B2.0%2BM%2BRunning%2BShoes%2BFor%2BMen_SHOEVMGGZJGEJZGA.LSTSHOEVMGGZJGEJZGAOCO5LD_4&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_Suggested%2BItems_DESKTOP_HORIZONTAL_productCard_cc_5_NA_4&cid=SHOEVMGGZJGEJZGA.LSTSHOEVMGGZJGEJZGAOCO5LD',
           'https://www.flipkart.com/sony-dsx-a110u-media-receiver-usb-car-stereo/p/itmf2gd8rfekwta8?pid=CDPF2G9VEGBRSPP8&lid=LSTCDPF2G9VEGBRSPP8UTOWZ4&marketplace=FLIPKART&srno=b_1_1&otracker=browse&fm=personalisedRecommendation%2Fp2p-same&iid=4a04836c-ad4f-4a98-adbd-6d7b1ef85a76.CDPF2G9VEGBRSPP8.SEARCH&ppt=Homepage&ppn=Homepage&ssid=2i37pt0l740000001552811138846',
           'https://www.flipkart.com/philips-9-w-round-b22-led-bulb/p/itme6zzs5rrzhbea?pid=BLBE6ZZS3GBMSRFG&lid=LSTBLBE6ZZS3GBMSRFGBL31A0&marketplace=FLIPKART&srno=b_1_7&otracker=nmenu_sub_Home%20%26%20Furniture_0_LED%20%26%20CFL&fm=personalisedRecommendation%2Fp2p-same&iid=e7c47080-4fda-4d11-a45d-df065a7a4dac.BLBE6ZZS3GBMSRFG.SEARCH&ppt=Homepage&ppn=Homepage&ssid=4m52zd9rs00000001552811159233',
           'https://www.flipkart.com/sandisk-ultra-dual-drive-m3-0-32-gb-otg/p/itmf3qyazyfgaf48?pid=ACCENUZA28X2PQ4G&lid=LSTACCENUZA28X2PQ4G2I1L5J&marketplace=FLIPKART&srno=s_1_2&otracker=search&fm=SEARCH&iid=9f70010f-2eb5-4633-abb2-9116bdb30ed8.ACCENUZA28X2PQ4G.SEARCH&ppt=SearchPage&ppn=Search&ssid=c8pc94pu9c0000001552811191243&qH=88442f18ff77821c']

for i in my_list:
    flipkart_price(i)
