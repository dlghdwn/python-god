#HTML
# 태그찾기
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

pres = res_html.find("h1")
print(pres)
print("\n1---------------------------\n")
print(pres.get_text().strip())
print("\n2---------------------------\n")
print(pres.next_element.get_text().strip())
print("\n6---------------------------\n")
print(pres.get_text())

tres = res_html.find("title")
print(tres)
print("\n3---------------------------\n")
print(tres.next_element)
print("\n4---------------------------\n")
print(tres.get_text().strip())

fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())

print("\n5---------------------------\n")

clres = res_html.findAll(class_ = "doc-title")
print(clres)

print("\n6---------------------------\n")
clrs = res_html.find(class_ = "head_top")
print(clrs)
print(clrs.get_text())
 """

#셀렉터로 찾기
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text()) """

#select
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
print("\n-----------------\n")

for i in iss :
    issue = i.get_text()
    print(issue)

print("\n-----------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs ["data-tiara-custom"]
    print(c + "\n") """




