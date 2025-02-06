import requests
import re
url='https://www.weather.com.cn/weather40d/101010100.shtml'
resp=requests.get(url)
resp.encoding='utf-8'
print(resp.text)


city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)
print(city)
print(weather)
print(wd)
print(zs)

lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
print(lst)
for i in lst:
    print(i)


'''<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">26/16℃</span>
<span class="zs">适宜</span>
'''