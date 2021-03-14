import re
import requests
import json
import os

url = "http://h5.cyol.com/special/daxuexi/daxuexiall/m.html?t=1"
headers = {
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent': 'Mobile/16D57 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN',
  'Content-Type': 'text/html; charset=utf-8',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

str1 = requests.request("GET", url, headers=headers)
a=re.finditer(r"h5.cyol.com/special/daxuexi/daxuexiall[0-9]+/m.html\?t=1",str1.content.decode())
link1=""
for match in a: 
  link1=match.group()
link1="http://"+link1

str2 = requests.request("GET", link1, headers=headers)
b=re.finditer(r"h5.cyol.com/special/daxuexi/([a-z0-9]+)/m.html\?t=1",str2.content.decode())
result=""
link2=""
for match in b: 
  result=match.group(1)

link2="http://h5.cyol.com/special/daxuexi/"+result+"/m.html?t=1"
str3 = requests.request("GET", link2, headers=headers)
str3.encoding="utf-8"
c=re.finditer(r"<title>(.*?)</title>",str3.content.decode())
title=""
for match in c: 
  title=match.group(1)

link3="http://h5.cyol.com/special/daxuexi/"+result+"/images/end.jpg"

if not os.path.exists("page"):
  os.mkdir("page")
with open("page/index.html",'w',encoding='utf8')as f1:
  f1.write("<!doctype html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>")
  f1.write(title)
  f1.write("</title>\n</head>\n<body>\n<div>\n<img src=\"")
  f1.write(link3)
  f1.write("\" style=\"position: absolute;width: 100%;height: 100%;top:0;left: 0 ;\">\n</div>\n</body>\n</html>\n")
