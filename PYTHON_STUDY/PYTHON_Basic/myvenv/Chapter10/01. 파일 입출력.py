# 파일 입출력을 사용하는 이유
# : 파일로부터 데이터를 읽어와서 프로그램에 사용하기 위해 
# : 프로그램에서 만든 데이터를 파일형태로 저장하기 위해

# 파일 열기 모드
# w : 쓰기 모드(write) 
# a : 추가 모드(append)
# r : 읽기 모드(read)

# 1. 파일 쓰기
file = open("./myvenv/Chapter10/data.txt", "w", encoding="UTF-8")
file.write("1. 스파르타 코딩과 함께 파이썬 공부")
file.close()

# 2. 파일 추가
file = open("./myvenv/Chapter10/data.txt", "a", encoding="UTF-8")
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()

# 3. 파일 읽기
file = open("./myvenv/Chapter10/data.txt", "r", encoding="UTF-8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()