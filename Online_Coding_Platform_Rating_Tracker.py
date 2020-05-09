    #Online Coding Platform Rating Tracker
'''
Scrapes the Online Coding Platforms like Codechef, Codeforces, HackerEarth and SPOJ with the help of given URLs and 
extracts the rating for a given user and prints the rating.
'''
try:
    import bs4 as bs
    import requests
    # To print the results in a Tabular Format
    from prettytable import PrettyTable
    import Slack_Push_Notification as Slack

    table = PrettyTable(['Coding Platform', 'Rating / Rank / Score'])


    #URLs of Coding Platforms
    cc_url = 'https://www.codechef.com/users/ramm_y2k'
    cf_url = 'http://codeforces.com/profile/iamram'
    he_url = 'https://www.hackerearth.com/users/pagelets/ram13/coding-data/'
    spoj_url = 'https://www.spoj.com/users/iam_ram/'
    ib_url = 'https://www.interviewbit.com/profile/i.am_ram/'
    lc_url = 'https://leetcode.com/ram_babu/'

    #Codeforces Scrapping
    cf_response = requests.get(cf_url)
    cf_html = cf_response.text

    cf_soup = bs.BeautifulSoup(cf_html, "lxml")

    #Extracting the rating and the position
    cf_rating = cf_soup.find('div', class_= 'info').find('ul').find('li').find('span').text
    cf_position = cf_soup.find('div', class_ = 'user-rank').find('span').text.strip()

    table.add_row(['Codeforces', cf_rating + ' (' + cf_position + ')'])
    


    #Codechef Scrapping
    cc_response = requests.get(cc_url)
    cc_html = cc_response.text

    cc_soup = bs.BeautifulSoup(cc_html, "lxml")

    #Extracting the rating and stars
    cc_rating = cc_soup.find('div', class_= 'rating-number').text
    cc_stars = cc_soup.find('div', class_ = 'rating-star').text

    table.add_row(['CodeChef', cc_rating + ' (' + cc_stars.strip() + ')'])
    


    #HackerEarth Scrapping
    he_response = requests.get(he_url)
    he_html = he_response.text

    he_soup = bs.BeautifulSoup(he_html, "lxml")

    #Extracting the Rating
    he_rating = he_soup.find('a', class_= 'dark weight-700').text
    table.add_row(['HackerEarth', he_rating])
    

    #LeetCode Scrapping
    lc_response = requests.get(lc_url)
    lc_html = lc_response.text
    lc_soup = bs.BeautifulSoup(lc_html, 'lxml')

    lc_rating = lc_soup.findAll('span', class_= "badge")[1].text.strip()
    table.add_row(['LeetCode', lc_rating])

    #SPOJ Scrapping
    spoj_response = requests.get(spoj_url)
    spoj_html = spoj_response.text
    spoj_soup = bs.BeautifulSoup(spoj_html, "lxml")

    temp = spoj_soup.find('div', class_= 'col-md-3')

    '''Either of the below will work - The Rank is present in the third <p> tag'''
    #spoj_rank = temp.find('p').find_next('p').find_next('p').text.strip()
    spoj_rank = temp.select_one("p:nth-of-type(3)").text.strip()
    table.add_row(['SPOJ', spoj_rank.split(':')[1]])
    

    #Interview Bit Scraping
    ib_response = requests.get(ib_url)
    ib_response = ib_response.text
    ib_response = bs.BeautifulSoup(ib_response, 'lxml')
    ib_response = ib_response.find('div', class_= 'user-stats').find('div', class_= 'stat pull-left')
    ib_score = ib_response.find('div', class_ = 'txt').text
    table.add_row(['Interview Bit Score', ib_score])

except Exception as e:
    print(f'Exception Occurred! \n{e}')
else:
    print(table)


    ''' Code to send a Slack Push Notification '''
    msg = 'Codeforces Rating: {}\nCodechef Rating: {}\nHackerEarth: {}\nLeetCode - {}\nSPOJ - {}\nInterviewBit Score: {}'.format(cf_rating + ' ' + '(' + cf_position + ')',
                                                                                         cc_rating + ' ' + '(' + cc_stars + ')' ,
                                                                                         he_rating,
                                                                                         lc_rating,
                                                                                         spoj_rank,
                                                                                         ib_score)

    Slack.slack_message(msg, __file__)
    
#print('\n**** Message Preview: **** \n{}'.format(msg))
