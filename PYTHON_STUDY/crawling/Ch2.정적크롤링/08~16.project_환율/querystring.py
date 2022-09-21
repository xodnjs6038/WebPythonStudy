# 쿼리스트링 (query string)
# 웹 요청시에 보내는 추가 인자 값

import requests as req

res = req.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%8A%A4%ED%8A%B8%EB%9E%A9')

print(res.text)