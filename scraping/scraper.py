from bs4 import BeautifulSoup
import requests

scrape_url = 'https://staging.hard.lk'

r = requests.get(scrape_url)

print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title)