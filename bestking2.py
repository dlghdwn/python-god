#식별 연산
""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)   """

""" a = 5
b = 5
print(a is b)
print(a is not b) """

""" a = 5 #int
b = 5.0 #float
print (a == b)
print(a is b)
print(a is not b)
 """

""" a = [3 , 5, 1]
b = a

print(a is b)

a[0] = 2

print (a,b)
print(a is b) """

""" #연산자 우선순위
#a = 2 + 3 * 4
#a = 10 / 5 / 2
#a = 2 ** 3 ** 2
#a = 2 ** (3 ** 2)
#a = 10 % 3 % 2
#a = 1 + 2 > 3 and 4 - 1 < 2
#a = not False and True
#a = not True or False and True
#a = 1 & 2 | 3 ^ 4
#a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
#a = 2 * -3 // 2
#a = 1 == 2 
a= 1 == 2 != 3

print (a) """

#조건문
""" #x = 10
x = -1
#x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero") """

# if 짝수 홀수
""" num = 23
#num - 24

if num % 2 == 0:
    print("짝수")
else:
    print("홀수") """
    
# if 두 수 비교
""" a = 5
b = 7
if a == b:
    print("같다")
else:
    print("다르다") """
    
# if a인지 b인지
""" char = "a" 
#char = "b"
#char = "c"

if char == "a" or char =="b":
    print("'a' 또는 'b'입니다")
else:
    print("'a' 또는 'b'가 아닙니다")
     """
    
# 반복문
# for 예시
""" fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) """
    
#이중 for문 예시
""" my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num) #0의 0번째부터 순차적으로 출력 0 123 1 123 2 123
"""

# for 0 ~ 9 까지 출력
""" for i in range(10): 
        print(i) """
        
# 문자 한글자씩 출력
""" for char in "kinggod":
    print(char) """

# 리스트 역순 출력 reversed
""" fruits = ["apple", "banana", "cherry"]
for fruit in reversed (fruits):
    print(fruit) """
    
# 리스트 역순 출력 sorted
""" fruits = ["apple", "banana", "cherry"]
for fruit in sorted (fruits, reverse=True):
    print(fruit)
    
for fruit in sorted (fruits, reverse=False):
    print(fruit) """
    
# 구구단 출력(이중 for)
""" for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(i,'x',j,"=",result) """
        
# for ~else문
""" rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process") """
 
# 반복문 제어
""" for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 3:
         print("continue", i)
         continue
    else:
         print("pass", i)
         pass

    print(i)  """

# while 문
""" i = 1

while i <= 5:
    print(i)
    i += 1 """
    
# 0 ~ 9 출력
""" i = 0

while i <= 9:
    print(i)
    i += 1  """
    
# 문자열 한글자씩 출력
""" str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1 """
    
# 1부터 10가지의 총합
""" sum = 0
i = 1
while  i <=10:
    sum += i
    i += 1
    
print(sum) """

# 1에서 100까지의 짝수, 홀수 출력
""" i = 1
while i <= 100:
 if i % 2 == 0:
    print(i,"짝수")
 else:
    print(i,"홀수") 
 i += 1  """

# 1에서 100까지의 7의 배수만 출력
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1