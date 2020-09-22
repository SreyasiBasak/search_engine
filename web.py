import requests,webbrowser
from bs4 import BeautifulSoup
user=input("enter search item: ")
#print("googling..")
res1=requests.get("https://www.google.com/search?q="+user)
soup1=BeautifulSoup(res1.text,'html.parser')
search1=soup1.select('a')
print(soup1.prettify())
print(search1)
for link in search1[2:3]:
    actual1=(link.get('href'))
    #print(actual)
    webbrowser.open("https://www.google.com/"+actual1)

res2=requests.get("https://www.bing.com/"+user)
soup2=BeautifulSoup(res2.text,'html.parser')
search2=soup2.select('a')
print(search2)
for link2 in search2[:1]:
    actual2=(link.get('href'))
    #print(res2)
    webbrowser.open("https://www.bing.com/"+actual2)

#   Yahoo facing problem !
# res3=requests.get("https://in.search.yahoo.com/search?p="+user)
# soup3=BeautifulSoup(res3.text,'html.parser')
# search3=soup3.select('a')
# print(search3)
# for link3 in search3[:3]:
#     actual3=(link3.get('href'))
#     #print(actual3)
#     webbrowser.open("https://in.search.yahoo.com/"+actual3)