import requests
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

requests.get(url)

with open('logo.png','wb') as f:
    f.write(requests.get(url).content)
    lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])