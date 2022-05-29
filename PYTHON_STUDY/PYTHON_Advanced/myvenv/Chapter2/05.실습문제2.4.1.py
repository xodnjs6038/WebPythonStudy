# 실습문제 2.4.1
# 리스트 내포를 사용해서 world_list에 들어있는 문자열 중 첫글자가 a인 것만 뽑아서 리스트로 만드세요.

# 변경 전
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 변경 후
# ['apple', 'apolo', 'abocado']

# 리스트 내포 사용하기 전
# result = []
# for word in word_list:
#     if word[0] == 'a':
#         result.append(word)
# print(result)

# 리스트 내포 사용한 후
result = [i for i in word_list if i[0] == 'a']
print(result)

