import time

import requests
from bs4 import BeautifulSoup


def gettile(i,url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for k in soup.select('title'):
        print(k.text)
    time.sleep(2)
    return k.text
def getData(i,url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    for k in soup.select('h3 > a'):
        print(k.get("href"))
        title = gettile(1,k.get("href"))
        with open("D:\DjangoTest\Django-Test-Mynet\photo1.txt",'a+',encoding='utf-8') as f:
            f.write(str(title)+":"+str(k.get("href"))+"\n")
    time.sleep(2)
url = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E6%91%84%E5%BD%B1%E6%8A%80%E5%B7%A7&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1517384243808&lkt=0%2C0%2C0&p=40040108'
url2 = 'http://weixin.sogou.com/weixin?oq=&query=%E6%91%84%E5%BD%B1%E6%8A%80%E5%B7%A7&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=0&_sug_=n&type=2&sst0=1517384243808&page=9&ie=utf8&p=40040108&dp=1&w=01015002&dr=1'
def test():
    for i in range(1,11):
        tmp = "%E6%91%84%E5%BD%B1%E6%8A%80%E5%B7%A7&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=0&_sug_=n&type=2&sst0=1517384243808"
        utltest = "http://weixin.sogou.com/weixin?oq=&query=%s&page=%s&ie=utf8&p=40040108&dp=1&w=01015002&dr=1"%(tmp,i)
        print(utltest)
        getData(1,utltest)
#test()

