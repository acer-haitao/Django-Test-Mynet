from bs4 import BeautifulSoup
import requests
import time
import xlwt
import re


def gettile(i,url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for k in soup.select('title'):
        print(k.text)

def getData(i,url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for k in soup.select('h3 > a'):
        print(k.get("href"))
        gettile(1,k.get("href"))
url = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E6%91%84%E5%BD%B1%E6%8A%80%E5%B7%A7&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1517384243808&lkt=0%2C0%2C0&p=40040108'
getData(1,url)