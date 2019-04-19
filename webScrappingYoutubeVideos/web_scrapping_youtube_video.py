from bs4 import BeautifulSoup4 as bs
import requests

base = "https://www.youtube.com/result?search_query="
qstring = "boddingtons+advert"

r = requests.get(base+qstring)

page = r.text
soup = bs(page, 'html.parser')
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

videoList = []
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videoList.append(tmp)

count=0
for item in videolist:
 
    # increment counter:
    count+=1
 
    # initiate the class:
    yt = YouTube(item)
 
    # have a look at the different formats available:
    #formats = yt.get_videos()
 
    # grab the video:
    video = yt.get('mp4', '360p')
 
    # set the output file name:
    yt.set_filename('Video_'+str(count))
 
    # download the video:
    video.download('./')
