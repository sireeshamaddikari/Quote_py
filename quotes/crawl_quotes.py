import requests
from bs4 import BeautifulSoup
from time import sleep

pages = [ 'http://quotes.toscrape.com/',
          'http://quotes.toscrape.com/page/1',
          'http://quotes.toscrape.com/page/2',
          'http://quotes.toscrape.com/page/3',
          'http://quotes.toscrape.com/page/4',
          'http://quotes.toscrape.com/page/5',
          'http://quotes.toscrape.com/page/6',
          'http://quotes.toscrape.com/page/7',
          'http://quotes.toscrape.com/page/8',
          'http://quotes.toscrape.com/page/9',
          'http://quotes.toscrape.com/page/10']

quotes_list = []   
def get_quotes(page): 
    html_page = requests.get(page)


    soup = BeautifulSoup(html_page.content,'html.parser')

    data = soup.select('.col-md-8 .quote')


    for quote in data :
        quote_dict = {'quote':'','author':'','tags':[]}
        quote_dict['quote'] = str(quote.select_one('.quote span').text.strip())
        quote_dict['author'] = str(quote.select_one('.quote small').text.strip())
        tags = []
        anchor_elements = quote.select('.quote .tags a')
        for anchor_element in anchor_elements :
            tags.append(anchor_element.get_text())
        quote_dict['tags'] = tags
        quotes_list.append(quote_dict)
    



for page in pages:
    get_quotes(page)
    sleep(10)

print(len(quotes_list),quotes_list[0])

import json
with open('quotes.json', 'w') as f:
    quotes_list = {"quotes":quotes_list}
    json.dump(quotes_list, f)