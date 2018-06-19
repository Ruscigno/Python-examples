import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA")
soup = BeautifulSoup(r.content, "html")
links = soup.find_all("a")
for link in links:
    print("<a href='%s'>'%s'</a>" %(link.get("href"), link.text))

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    try:
        print(item.contents[0].find_all("a", {"class": "bussiness-name"})[0].text)
        print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
        print(item.contents[1].find_all("span", {"itemprop": "wtreetAddress"})[0].text)
        print(item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text)
        print(item.contents[1].find_all("li", {"class": "primary"})[0].text)
    except:
        pass