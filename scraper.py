import requests
from bs4 import BeautifulSoup
print('Downloaded and imported the libraries')

youtube_link = 'https://www.youtube.com/feed/trending'
response = requests.get(youtube_link)
print('Downloading page into response object')
print(response.text[:1000])

