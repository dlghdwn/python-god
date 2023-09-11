#집합
my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print (my_set)
print (setItem)

#집합 활용
my_set = {5, 8, 3, 7, 1, "h"}
print (my_set) #순서 정렬
print (*my_set)

my_set = ([5, 8, 3, 7, 1, "h"])
print (my_set) #그대로 나옴

set_tmp = set("hello")
print(set_tmp)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}

print(my_set | set_item) #합집합
print(my_set.union(set_item))

print(my_set - set_item) #차집합
print(my_set.difference(set_item))

print(my_set & set_item) #교집합
print(my_set.intersection(set_item))

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.add(9) #추가
print(my_set)


my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.update([5, 9, 7, 4]) #추가
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.clear() #전체 삭제
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.remove(5) #삭제
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2) #없는걸 지워도 오류 안남
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item) #공통된 요소 삭제
print(my_set)

#타입 변환
my_int = 10
print(my_int)
print(my_int + 10)

my_str = str(my_int)
print(my_str)
#print(my_str + 10)
print(my_str + "hello")


my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

""" my_int2 = int("ten")
print(my_int2) """