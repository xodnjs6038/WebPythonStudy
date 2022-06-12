import threading
import time
# 주식 자동 매매
# 매수, 매도

# 매수 스레드
def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중..")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 매수 타이밍 확인...")
        time.sleep(1)
        print("[매수] 매수 진행...")
        time.sleep(1)

# 매도 스레드
def saler():
    for i in range(5):
        print("[매도] 데이터 요청 중..")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 매도 타이밍 확인...")
        time.sleep(1)
        print("[매도] 매도 진행...")
        time.sleep(1)

# 메인 스레드
print("[메인] start")
buyer = threading.Thread(target=buyer)
saler = threading.Thread(target=saler)
buyer.start()
saler.start()

buyer.join() # 매수 스레드가 종료될때까지 메인 스레드가 기다림
saler.join() # 매도 스레드가 종료될떄까지 메인 스레드가 기다림
print("[메인] 장이 종료되었습니다.")