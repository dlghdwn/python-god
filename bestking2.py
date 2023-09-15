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

#연산자 우선순위
a = 2 + 3 * 4
a = 10 / 5 / 2
a = 2 ** 3 ** 2
a = 2 ** (3 ** 2)
a = 10 % 3 % 2
a = 1 + 2 > 3 and 4 - 1 < 2
a = not False and True
a = not True or False and True
a = 1 & 2 | 3 ^ 4
a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
a = 2 * -3 // 2
a = 1 == 2 
a= False != 3

print (a)