from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

youtube_link = 'https://www.youtube.com/feed/trending'

'''print('Downloaded and imported the libraries')
response = requests.get(youtube_link)
print('Downloading page into response object')
print(response.text[:1000])

doc = BeautifulSoup(response.text)
print('Converted to a BeautifulSoup object !')'''

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)
  return driver

print('Setted a browser.')
#if __name__ == '___main_':
driver = get_driver()
driver.get("https://www.python.org")

print('Page title:', driver.title)