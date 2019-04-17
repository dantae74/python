from bs4 import BeautifulSoup4 as bs
import requests

base = "https://www.youtube.com/result?search_query="
qstring = "boddingtons+advert"

r = requests.get(base+qstring)

page = r.text
soup = bs(page, 'html.parser')
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
