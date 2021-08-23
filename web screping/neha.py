import requests
from bs4 import BeautifulSoup
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
### step 1 : get the HTML
r = requests.get(url)
htmlcontent = r.content

#### step 2 : parser the HTML
soup = BeautifulSoup(htmlcontent,"html.parser")
