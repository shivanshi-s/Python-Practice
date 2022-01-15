# rules
# try to get permission before scraping
#limitations
# every web scraping script is unique to update and change
#  with web scraping

import requests
import bs4
result = requests.get("https://example.com/")
print(type(result))
# print(result.text)

# beautiful soup converts it into soup and grab information easily from a giant string
soup = bs4.BeautifulSoup(result.text,"lxml")
# soup var  = pass ( text string, and what engine to parse through the text - lxml on the backend to go thru the text)
#    print(soup)
# grap something
# print(soup.select('title'))
# # returns a ^ list because there might be different things to the tag
# print(soup.select('title')[0].getText())


site_paragraphs = soup.select('p')
print(type(site_paragraphs[0])) # not a string , special soup object
print(site_paragraphs[0].getText())