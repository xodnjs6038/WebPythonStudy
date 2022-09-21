from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.naver.com/sise/sise_market_sum.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

# for title in soup.select("a.tltle"):
#     print(title.get_text(strip=True))

for tr in soup.select("table.type_2 tr"):
    if len(tr.select("a.tltle")) == 0:
        continue    
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(3)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(5)")[0].get_text(strip=True)
    print(title, price, change)