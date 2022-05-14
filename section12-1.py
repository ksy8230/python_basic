# 파이썬 데이터베이스 연동
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(sqlite3.version) # sqlite verstion
print(sqlite3.sqlite_version) # db engine verstion

# DB 생성 & auto commit
conn = sqlite3.connect("D:/python_basic/resource/database.db", isolation_level=None)

c = conn.cursor()
print(type(c))

# 테이블 생성 (TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, \
phone text, website text, regdate text)")


# 데이터 타입
c.execute("INSERT INTO users VALUES(1, 'kim', 'ksy@naver.com', '010-2222-2222', 'kim', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Park', 'Park@naver.com', '010-2221-1111', "pPar.bloc", nowDateTime))

# Many 타입
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2121-1111', "pLee.bloc", nowDateTime),
    (4, 'Han', 'Han@naver.com', '010-3421-1111', "Hee.bloc", nowDateTime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userList)

# conn.execute("DELETE FROM users").rowcount -> 몇개 지웠는지 숫자 반환

# 커밋, isolation_level=None 인 경우 자동반영 (자동 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
# conn.close()











































 