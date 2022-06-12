# 모듈 추가
import sqlite3

# 데이터베이스 열기
conn = sqlite3.connect('/Users/susimdal/PYTHON_STUDY/PYTHON_Advanced/myvenv/Chapter5/sql_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
SELECT_SQL = """
    SELECT * FROM item
"""

# SQL 명령 실행
cur.execute(SELECT_SQL)

rows = cur.fetchall()
for row in rows:
    print(row)

# 데이터베이스 닫기
conn.close()