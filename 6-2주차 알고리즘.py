""" #큐(선입선출 방식)
qlist = []

def enqueue(qlist,data):
    qlist.append(data)
    
def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data
enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

enqueue(qlist, 4)
print(qlist)

enqueue(qlist)
print(qlist) """

#알고리즘
#O(1) 일정한 복잡도(상수복잡도)(입력값과 상관없이 즉시 결과 출력, 이론적으론 가능하지만 구현 힘듦)
""" arr = [1, 2, 3, 4, 5]

def ret_01(idx) :
    return arr[idx]

print(ret_01(2)) #3출력됨 """

# O(1) 시간
""" import time
arr = [1, 2, 3, 4, 5]

def ret_01(idx) :
    return arr[idx]

start = time.time()
print(ret_01(2))
end = time.time()

print(f"{end - start : 5f} sec") #0.000 소요된다고 출력 """

# O(n) 선형복잡도 (일반적, 입력값과 실행시간이 비례함)
""" arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)

print_elements(arr) """

# O(n) 시간
""" import time
arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)

start = time.time()
print_elements(arr)
end = time.time()

print(f"{end - start : 5f} sec")
 """
 
# O(log n) 로그 복잡도 (입력데이터를 받을 때마다 빨라짐, 곡선모양)
""" import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
    
start = time.time()
result = binary_search(my_list, 4)
end = time.time()

print(f"{end - start : 5f} sec") """

# O(n2) 2차 복잡도 (입력증가, 제곱수 비율로 실행시간 증가)
""" import time

def mul_for() :
    for i in range(5) :
        for j in range(5) :
            print(i,j)
            

start = time.time()
mul_for()
end = time.time()

print(f"{end - start : 5f} sec")  """

#O(2n) 지수시간, 기하급수적 복잡도 (실행시간이 2배씩 증가, 쓰레기)

# 정렬 알고리즘
# 버블 정렬(두 개씩 비교하면서 순서 정렬, 포도송이 모양)
""" def bobble_sort(arr):
    N = len(arr) #데이터의 갯수 : 5
    for i in range(N):#01234
        #print(i,arr)
        for j in range(N-i-1): #4321
            if arr[j] > arr[j+1]:
                #print(arr[j+1], arr[j])
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(i, j, arr, arr[i], arr[j])
    return arr       
lrr = [1, 9, 2, 7, 5]
print(bobble_sort(lrr)) """

# 퀵 정렬(기준을 정하고 왼쪽 오른쪽 비교 후 정렬)
""" def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) //2] #가운데 값을 피벗으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv", pivot)
    print("left", left)
    print("middle", middle)
    print("right", right)
    
    return quick_sort(left) + middle + quick_sort(right)

my_list = [1, 9, 6, 4, 5, 7, 3, 2]
print(len(my_list))

sorted_list = quick_sort(my_list)

print(sorted_list) """

#서드파티 모듈 4-2주차
""" import requests

res = requests.get('https://www.google.com')
print(res)
print(res.content)
 """
 
#numpy
""" import numpy as np

#1차배열 생성
a = np.array([1, 2, 3])
print(a)

#2차 3행 배열, 0으로 초기화
b = np.zeros((2, 3))
print(b)

#2차 3행 배열, 1로 초기화
c = np.ones((2,3))
print(c)

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

#배열간 연산
f = d + e
g = d - e
h = d * e
i = d / e 

print(f)
print(g)
print(h)
print(i) """

#pandas
""" import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print(df)

#age 관련 속성
#print(df['Age'].describe())

#Sort the dataframe by age in descending order
print(df.sort_values(by='Age', ascending = False))
print("===================")
print(df.sort_values(by='Age', ascending = True))
print("===================")
print(df.sort_values(by='Name', ascending = True)) """

#matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# 리스트 구성
plt.plot(x, y)

# 제목 추가
plt.xlabel('time')
plt.ylabel('n')
plt.title('python')

# 출력
plt.show()