# goal : to get every title of the book with a 2 star rating

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_title = []

for n in range(1,51):
   scrape_url = base_url.format(n)
   res = requests.get(scrape_url)
   soup = bs4.BeautifulSoup(res.text,'lxml')
   books = soup.select(".product-pod")

   for book in books:
      if len(book.select('.star-rating.Two')) != 0:
         book_title = book.select('a')[1]['title']
         two_star_title.append(book_title)

print(two_star_title)


# for x in range(1,51):
#    res = requests.get(base_url.format(x))
#    soup = bs4.BeautifulSoup(res.text,'lxml')

#    product = soup.select(".product_pod")
#    book_stars = soup.select(".star-rating.Two")

#    if book_stars is True:
#       title = soup.select('a')[1]['title']
#       print(title)