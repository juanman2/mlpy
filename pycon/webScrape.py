from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.premierleague.com/tables"
uClient = uReq(my_url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

# tableBodyContainer isPL

teams = page_soup.findAll("tr", {"data-filtered-entry-size":"20"})
for t in teams:
    short = t.find("span", {"class":"short"})
    cols = t.findAll("td")
    print(short.text, cols[3].text, cols[4].text, cols[5].text, cols[6].text)
    
