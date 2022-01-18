# beautiful soup
# create a new request to "get" https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)
# make soup out of it - pass the resulting text and the lxml library
# select soup
# try and select the class of .thumbImage

import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")

#print(soup.select('.thumbimage'))
# the first thumb image

computer = soup.select('.thumbimage')[0]
# want to grab a particular class so we can call it as a DICTIONARY 
print(computer['src'])
# img src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png"

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')

# raw content of the img = binary file
#print(image_link._content)
# save in computer in the form of an img

f = open('my_computer_img.png','wb')
f.write(image_link.content)
f.close()