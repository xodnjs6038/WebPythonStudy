# 실습문제 2.4.2
# 리스트 내포를 사용해서 다음과 같이 변경해보자.

# 변경 전
items = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 리스트 내포 사용 전
# result = []
# for item in items:
#     if item != None:
#         result.append(item)
#     else:
#         result.append('')
# print(result)

# 리스트 내포 사용 후
result =[i if i != None else '' for i in items]
print(result)
