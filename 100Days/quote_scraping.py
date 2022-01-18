# goal : scrape.

import requests
import bs4

# res = requests.get('https://quotes.toscrape.com/')
# soup = bs4.BeautifulSoup(res.text,'lxml')
#select author
# authors = set()
# for name in soup.select('.author'):
#    authors.add(name.text)
# print(authors)

# select quotes on the page
# quotes = []
# for x in soup.select('.text'):
#    quotes.append(x.text)
# print(quotes)

# pages scan
url = 'https://quotes.toscrape.com/page/'
page_still_valid = True
 
authors = set()
page = 1
while page_still_valid:
   page_url = url+str(page)
   res =  requests.get(page_url)

   if page_still_valid == False:
      break
   
   soup = bs4.BeautifulSoup(res.text,'lxml')

   for name in soup.select('.author'):
      authors.add(name.text)
   
   page = page + 1

print(authors)