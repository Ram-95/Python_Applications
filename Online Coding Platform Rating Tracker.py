#Online Coding Platform Rating Tracker
'''
Scrapes the Online Coding Platforms like Codechef, Codeforces, HackerEarth and SPOJ with the help of given URLs and 
extracts the rating for a given user and prints the rating.
'''
import bs4 as bs
import requests

cc_url = 'https://www.codechef.com/users/ramm_y2k'
cf_url = 'http://codeforces.com/profile/iamram'
he_url = 'https://www.hackerearth.com/users/pagelets/ram13/coding-data/'
spoj_url = 'https://www.spoj.com/users/iam_ram/'

#Codeforces Scrapping
cf_response = requests.get(cf_url)
cf_html = cf_response.text

cf_soup = bs.BeautifulSoup(cf_html, "html.parser")
cf_temp = cf_soup.find('div', class_ = 'info')

cf_position = cf_temp.find_next('span', class_= 'user-gray').text.strip()
cf_rating = cf_temp.find_next('span', class_= 'user-gray').find_next('span', class_= 'user-gray').text

print('Codeforces Rating: {} ({})'.format(cf_rating, cf_position))


#Codechef Scrapping
cc_response = requests.get(cc_url)
cc_html = cc_response.text

cc_soup = bs.BeautifulSoup(cc_html, "lxml")
cc_rating = cc_soup.find('div', class_= 'rating-number').text

cc_stars = cc_soup.find('div', class_ = 'rating-star').text

print('CodeChef Rating: {} ({})'.format(cc_rating, cc_stars))


#HackerEarth Scrapping
he_response = requests.get(he_url)
he_html = he_response.text

he_soup = bs.BeautifulSoup(he_html, "lxml")
he_rating = he_soup.find('a', class_= 'dark weight-700').text

print('Hacker Earth Rating: {}'.format(he_rating))


#SPOJ Scrapping
spoj_response = requests.get(spoj_url)
spoj_html = spoj_response.text

spoj_soup = bs.BeautifulSoup(spoj_html, "lxml")
temp = spoj_soup.find('div', class_= 'col-md-3')

#Either of the below will work - The Rank is present in the third <p> tag.
#spoj_rank = temp.find('p').find_next('p').find_next('p').text.strip()
spoj_rank = temp.select_one("p:nth-of-type(3)").text.strip()

print('SPOJ {}'.format(spoj_rank))
