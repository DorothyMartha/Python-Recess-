from bs4 import BeautifulSoup
import requests

url = 'https://xeno-canto.org/'  # Corrected URL assignment
response = requests.get(url)

# Get title of the page
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')
print(title)
