import os

# 파일 경로
file_path = "./myvenv/Chapter12/data.csv"

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    pass
else:
    # 파일 생성하기
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()
    