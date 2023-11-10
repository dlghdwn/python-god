#입력암호화
""" import getpass

#pw = getpass.getpass("pass : ") #입력한 내용 안보임
pw = input("pass : ")
print(pw) """

#해시알고리즘 sha256
""" import hashlib

hl = hashlib.sha256()
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "1234567890"
target = "세븐틴 음악의 신"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
#print(hl.digest())
 """

#해시알고리즘 keccak256
""" import Crypto.Hash.keccak as kek

#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "1234567890"
target = "세븐틴 음악의 신"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

#print(kksh.digest())
print(kksh.hexdigest()) """

#활용-입력키 변환
""" import getpass
import hashlib

pw = getpass.getpass("pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """

#암호화 파일 저장
""" import hashlib
import os

#실제 호출지점
def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
        
    else:
        return True
    
if pwInsert(): #시작부분,  true면 if로 리턴 false는 else로 리턴
    pw = input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password") """
    
#시스템 정보
""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps) """

#웹정보 읽기1 urllib
""" import urllib.request as ur

url = 'https://www.google.com'
#url = "https://daum.net"
#url = "https://xkcd.com/"

res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
print(web) """

#웹정보 읽기2
""" import http.client as hc

#url = 'www.google.com'
url = 'www.daum.net'

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())
    
conn.close()
    
print(r) """

#웹정보 읽기3
""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)
    
print(web) """

#프로세스와 프로세서의 차이 알기
#싱글스레드
""" import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
    
end = time.time()

print("single end", end-start) """

#멀티스레드
""" import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end", end - start) """

#병렬처리, 일단 건너뛰기
""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))


start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc end", end - start) """

#main 실행
""" def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run() """

#비동기 처리
""" import asyncio
import random as rd
import time 

async def worker(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")

    print(f"end of {name}")
        
async def main():
    task1 = asyncio.create_task(worker("1test"))
    task2 = asyncio.create_task(worker("2test"))
    task3 = asyncio.create_task(worker("3test"))

    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end - start)

if __name__ == '__main__' :
    asyncio.run(main()) """

#비동기 처리 2
""" import asyncio
import time 

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)

async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(1)

async def main():
     
     task_1 = asyncio.create_task(worker1())
     task_2 = asyncio.create_task(worker2())

     print("start task")
     start = time.time()
     await task_1
     await task_2
     end = time.time()
     print("end task", end - start)

if __name__ == '__main__' :
    asyncio.run(main()) 
 """

#스케쥴
""" import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")

    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(3, 1, tester, ('1num',))
    s.enter(7, 1, tester, ('1num',))
    s.run()

if __name__ == "__main__":
    run()
    #main()
    print("end") """

#문자열 비교
""" import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff) #리스트로 출력됨
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """

#faker 임의 데이터
""" from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

with open("fktemp.csv", "w",newline='') as f :
    for i in range(30):
        f.write(temp.name() + "," + 
            temp.address() + "," + 
	        temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," +
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n") """

#시스템명령어
""" import subprocess as sp

#res = sp.run(["cmd", "/c", "dir"], capture_output=True)
#res = sp.run(["cmd", "/c", "dir"], capture_output=False)
#res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=False)
print(res)
 """

#에러 처리
""" import traceback as tb

def tester() :
	return 1/0

def caller():
	tester()
	
def main():
    try:
          caller()
		
    except ZeroDivisionError:
        print("xde error")
    
    except ValueError :
        print("ve error")

    except Exception as ex :
         print("ex error", ex)

    else :
         print("ok")

    finally :
	     print("end") """