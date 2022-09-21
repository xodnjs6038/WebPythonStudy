# 프로젝트 진행하며 배울 내용
# - requests 활용한 기초적인 파싱
# - find(), split() 등을 활용한 기초적인 문자열 파싱
# - 정규식(regex)을 활용한 패턴 검색
# - 쿼리스트링에 대한 이해
# - beautifulsoup 을 활용한 편리한 html 파싱
# - css selector 를 활용한 손쉬운 파싱

import requests as req

res = req.get('https://finance.naver.com/marketindex')

html = res.text

p = html.split('<span class="value">')[1].split('</span>')[0]

print(p)