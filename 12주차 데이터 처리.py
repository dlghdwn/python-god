#dataframe
""" import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

print(df)
print("\n--------\n")

print(df[1])
print("\n--------\n")

print(df[1][1])
print("\n--------\n")
 """
#dictionary
""" import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print("\n--------\n")

print(fr["x"])
print("\n--------\n")

print(fr.x)
print("\n--------\n")

print(fr.iloc[2])
print("\n--------\n")

print(fr.loc["y축"])
print("\n--------\n")

#컬럼 추가
frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
frs["t"] = [60, 120, 180]
print(frs)
print("\n--------\n")

#행추가
frs.loc["t축"] = [100, 200, 300, 400]
print(frs)
print("\n--------\n")

#행수정
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)
print("\n--------\n")

#행 삭제
frs.drop("x", axis=1, inplace=True)
print(frs)
print("\n--------\n")

# 열 삭제
frs.drop("x축", inplace=True)
print(frs)
print("\n--------\n") """

#컬럼추가
""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
print("\n--------\n")

print(df["x"])
print("\n--------\n")

print(df.loc["x축"])
print("\n--------\n")

#연산
print(df + 1)
print(df.div(100))
print(df / 100)
print(df.mul(100)) #걍 기호로 해도 가능

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])

print(df.div(df2))
print("\n--------\n")

print(df.div(df2, fill_value=1))
print("\n--------\n") """

#멀티인덱스
""" import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)
print("\n--------\n") 

print(df.iloc[0])
print("\n--------\n") 

print(df.loc["row1"])
print(df.loc[("row2", "val3")])
print("\n--------\n") 

df.loc[("row3", "val3"), "col1"]
print("\n--------\n")  """

#랜덤 데이터 생성
""" import pandas as pd
import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)
print("\n--------\n")

print(df[2])
print("\n--------\n")

print(df.loc[2])
print("\n--------\n")

print(df.loc[3][1])
print("\n--------\n")

#범위 출력
print(df.head(3))
print("\n--------\n")

print(df.tail(3))
print("\n--------\n") 

print(df.sample())
print("\n--------\n") """

#출력
#파일 생성
""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
   f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
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
            temp.color_name() + "\n")
         """
#파일 열기
""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target) """

#print(df)
#print(df.values[0]) #0번째 데이터

#인덱스 설정 확인
#print(df.index)

#print(df.dtypes) 

#print(type(df))

#부분읽기
""" print("\n--------\n")
print(df.head())
print("\n--------\n")
print(df.head(3))
print("\n--------\n")

print(df.tail())
print("\n--------\n")
print(df.tail(3))
print("\n--------\n")

print(df.sample())
print(df.sample(4))
print("\n--------\n")  """

#출력
""" print(df.values)
print("\n--------\n")
print(df.values[3])
print("\n--------\n")
 """
 
#엘레멘트 출력
""" for el in df.values[0] :
    print(el) """

#데이터프레임 정보확인
#print(df.info())

#null값 확인
""" print(df.isnull())
print(df.isnull().sum()) """

#컬럼 행 데이터 확인
""" print(df.name)
print(df.postcode)
print(df.job)
print(df.phone)
print(df.id)
print(df.company)
print(df.catch_parase)
print(df.color)

print(df["name"])
print(df["postcode"])
print(df["job"])
print(df["phone"])
print(df["id"])
print(df["company"])
print(df["catch_parase"])
print(df["color"]) """

#여러 컬럼 확인
""" print(df[["name", "id"]])
print(df[["name", "address", "postcode"]]) """

#컬럼 데이터 상세
""" print(df.postcode.describe())
print(df.color.describe()) """

#컬럼 데이터 갯수
""" print(df.color.count())
print(df.color.value_counts())
 """
#데이터간 연산
""" print(df.postcode.sum())
print( df.name.count()) """

#비교 연산
""" print(df.name == "김병철")
print("\n--------\n")  
print(df.company == "(주) 이이황")
print("\n--------\n")   """
""" temp = df[df.postcode > 70000]
print(temp)
print("\n--------\n") """

#print(df[df.color == "Lime"].head(1))

#res = df[df.postcode > 70000][["name", "postcode","color"]]
#print(res)
#print(res.count())

#temp = df.postcode.mean()
#temp = df.postcode.sum()
#print(temp)

#temp = df[df.color=="Lime"].postcode.mean()
#temp = df[df.color=="Lime"].postcode.sum()
#print(temp)

#temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
#temp = df[df.postcode > df.postcode.mean()]
#print(temp)

#temp = df.company.isnull()
#for el in temp:
#    if el == True:
#        print(el)

#temp = df[df.company.isnull()]
#temp = df[df.company.isnull()][["name"]] 
#print(temp)

#비트연산-nor
 #temp = df[(df.color == "Beige")]
#temp = df[~(df.color == "Beige")]
#print(temp.count())
#print(temp.color.count()) 

#and
""" temp = df[(df.color == "LimeGreen") & (df.postcode > 70000)]
print(temp) """
#or
""" temp = df[(df.color == "LimeGreen") | (df.postcode > 70000)]
print(temp)
 """
#정렬
""" temp = df.sort_values("postcode")
#temp = df.sort_values("name", ascending=False)
print(temp) """

#데이터 재배열
""" import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n========================\n")
print(df.pivot(index='Machine',columns='Country',values='Price'))
#print(df.pivot(index='Brand',columns='Machine',values='Price'))
#print(df.pivot(index='Country',columns='Machine',values='Price'))
#print(df.pivot(index='price',columns='Brand',values='Machine')) """


