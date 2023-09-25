# datetime 모듈의 datetime 함수를 dt라는 별명으로 사용
#from datetime import datetime as dt

# 현재 시간 출력 
#print (dt.now()) 
 
""" # 특정 시간대의 현재 시간 출력
from pytz import timezone
#tx = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezone :", dt.now(tz))
 """

# 문자열을 날짜로 변환 (지정해서 출력)
""" date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object) """

# 날짜를 문자열로 변환 (현재 시각을 출력)
""" date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """

# 모듈화
""" import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time() 
print(res)  """

# os모듈 확인
""" import os

# 현재 디렉토리 출력 
print(os.getcwd())

# 상위 디렉토리로 변경, 상대경로, 절대경로 
os.chdir("../")

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일목록 출력 
print(os.listdir())

# 폴더 생성 
os.mkdir("new_directory")
print(os.listdir())

# 폴더 삭제 
os.rmdir("new_directory") 
print(os.listdir())
 """
 
 #os 모듈화
""" import mod.utils as mu
import os

print(mu.get_curdir()) 

pname = "python"
mu.os_mkdir(pname)
print (os.listdir())

os.rmdir(pname) 
print (os.listdir()) """

#sys
""" import sys

print(sys.version)
print(sys.argv) """

# 스택
""" list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(list)

top = list.pop()
print(top)
print(list)
print(len(list)) """

# 큐
queue = []
queue.append(1)
queue.append(2)
queue.append(2)
queue.append(4)
queue.append(5)
print(queue)

front = queue.pop(0)
print(front)
print(queue)
print(len(queue))
