import re

# 전화번호 정규표현식 사이트
# https://regexr.com/63bls
# 1. Group 
# 1) 매칭되는 문자열 한개
str1 = '010-2343-3333'
result = re.match('\d{2,3}-\d{3,4}-(\d{4})$', str1)
print(result.group(1))

# 2) 매칭되는 문자열 여러개
str2 = '010-2344-7777,010-2344-8888,010-2344-9999,010-2344-2222'
results = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=,|$)', str2)
for idx, result in enumerate(results, 1):
    print(f'{idx}. {result.group(1)}')

# 2. Substitution (교체)
str3 = '010-2343-3333'
result = re.sub('(?<=\d{3}-\d{4}-)\d{4}', '****', str3)
print(result)