# 삼각형 출력 1번, 나
""" range = (1,2,3,4,5)
for i in reversed (range):
    print("*" * i) """

# 삼각형 출력 1번, 교수님
""" for i in range(5, 0, -1): #5~0 -1씩 빼기
    print("*" * i) """
    
# 삼각형 출력 2번 나, 교수님
""" for i in range(1,6): 
    print("*" * i) """
    
# 삼각형 출력 3번, 나
""" for i in range(1,6):
    result = 1 + 2*(i-1)
    print("*"* result) """
    
# 3번 교수님
""" for i in range(1, 6):
    spaces = " " * (6-i)
    stars = "*" * (2 * i - 1)
    print (spaces + stars)  """
    
# 삼각형 출력 4번 교수님
""" for i in range(1, 6):
    spaces = " " * (6-i)
    stars = "*" * (2 * i - 1)
    print (spaces + stars)
    
for i in range(6, 0 ,-1):
    spaces = " " * (6-i)
    stars = "*" * (2 * i - 1)
    print (spaces + stars) """

#=================================
# 5*5 출력
# 정상출력
""" num = 0
line = []
for i in range (5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
    
# 세로출력
""" line = []
for i in range (1,6):
    for j in range(1,6):
        num = ((j - 1)*5) + i
        line.append(num)
    print(line)
    line = [] """
    
# 역순출
""" num = 26
line = []
for i in range (5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []  """
    
#======================
# 가위, 바위, 보
""" import random as rd

def pc_choice():
    list =  ['1', '2', '3']
    return rd.choice(list)

def determine_winner(user_choice):
    pcnum = pc_choice()
    print(user_choice,pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif(
     (user_choice == '1' and pcnum == '3') or
     (user_choice == '2' and pcnum == '1') or
     (user_choice == '3' and pcnum == '2') 
     ):
        print("승")
        return
    else:
        print("패")
        return

print("1: 가위")
print("2: 바위")
print("3: 보")
print("1~3 숫자를 입력하세요")
chnum = input()
determine_winner(chnum)
 """
#=============================
# 파일쓰기
""" file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close()
 """
 
""" file = open("c:/Users/Catholic/temp.text","w")
for i in range(100):
    file.write(f"{i}\n")
    
file.close()
 """

# 추가로 쓸 때
""" file = open("c:/Users/Catholic/temp.text","a")

file.write("hello\n")
file.write("world")

file.close() """

#파일 읽기
""" f = open("temp.txt", "r")
res = f.read()
print(res)

f.close() """

# 다른경로 파일 읽기
""" f = open("c:/Users/Catholic/temp.text","r")
res = f.read()
print(res)

f.close()  """

# 한 라인씩 읽기
""" f = open("c:/Users/Catholic/temp.text", "r")
res = f.readline()
print(res)

f.close() """

""" f = open("temp.txt", "r")

for i in range(110):
   res = f.readline()
   print(res)

f.close() """

#readlines
""" f = open("c:/Users/Catholic/temp.text", "r")

res = f.readlines()
print(res)

f.close()  """

# 라인별 처리
""" f = open("c:/Users/Catholic/temp.text", "r")
line = f.readlines()
for l in line :
	print(l)
 
f.close() """

# 파일 객체
""" f = open("c:/Users/Catholic/temp.text", "r")
for line in f :
	print(line)

f.close() """

# 활용

