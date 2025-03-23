from bs4 import BeautifulSoup
import requests

url = "http://www.ibm.com"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

for link in soup.find_all('a',href=True):
    print(link.get('href'))