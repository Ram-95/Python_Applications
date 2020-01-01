#IMDB Scraping
'''Script that finds the Top 250 Movies on IMDB.'''
import requests
import bs4 as bs

#List that stores the details of the movies as a Dictionary.
movies = []
print('Scraping in Progress... ')

for idx in range(1,4):
    url = 'https://www.imdb.com/list/ls068082370/?sort=list_order,asc&st_dt=&mode=detail&page=' + str(idx)
    response = requests.get(url)
    html = response.text
    soup = bs.BeautifulSoup(html, 'lxml')

    temp = soup.findAll('div', class_= 'lister-item mode-detail')


    for i in temp:
        d = dict()
        
        d['Title'] = i.find('h3', class_= 'lister-item-header').find('a').text
        d['Rating'] = i.find('span', class_= 'ipl-rating-star__rating').text
        d['Director'] = i.select_one("p:nth-of-type(3)").find('a').text

        stars = [i.select_one("p:nth-of-type(3)").select_one("a:nth-of-type(2)").text,
                 i.select_one("p:nth-of-type(3)").select_one("a:nth-of-type(3)").text]
        d['Actors'] = stars


        movies.append(d)

print(len(movies))
