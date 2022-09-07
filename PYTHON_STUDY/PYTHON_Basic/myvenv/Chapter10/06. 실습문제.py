import csv
# data = [
#     ["종목", "매입가", "수량", "목표가"],
#     ["삼성전자", 85000, 10, 90000],
#     ["NAVER", 3380000, 5, 400000],
# ]

# file = open("./myvenv/Chapter10/mystock.csv", "w")

# writer = csv.writer(file)


# for d in data:
#     writer.writerow(d)

# file.close()

### 오류 해결 과정 중심

def show_profit(data):
    name = data[0] # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount # 수익금
    profit_ratio = (target_price/purchase_price -1 ) * 100

    print(f"{name} {profit:.2f} {profit_ratio:.2f}")

### 파일 열기 
file = open("./myvenv/Chapter10/mystock.csv", "r")

# 파일 데이터 읽기
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)

file.close()