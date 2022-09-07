# 예외처리가 필요한 이유
# : 프로그램 실행 중에 발생하는 에러를 미연에 방지
# try - except 구문 / else : 예외가 발생하지 않을 경우, finally : 항상 실행할 코드

# 원화를 입력, 환율 입력 -> 달러 값을 출력
won = input('원화 금액을 입력하세요>>>')
dollar = input("환율을 입력하세요>>>")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e: 
    print("나누기 0은 불가능합니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("예외가 발생하던지, 발생하지 않던지 항상 실행되는 코드")