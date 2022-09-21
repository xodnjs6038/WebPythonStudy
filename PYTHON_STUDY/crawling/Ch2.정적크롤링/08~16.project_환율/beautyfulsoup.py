# beautyfulsoup
# requests: http 통신을 편하게
# beautyfulsoup: html 통신을 편하게

# 주요 기능
# - html 문자열 파싱
# - html 노드 인식 및 편리한 기능들
# - parent, children, contents, descendants, silbling
# - string, strings, stripped_strings, get_text()
# - prettify
# - html attribute 

from bs4 import BeautifulSoup as BS
import requests as req

url = "https://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser")
print(soup.title)