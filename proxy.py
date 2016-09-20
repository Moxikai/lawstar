#coding:utf-8
"""
抓取西祠代理,存入文件
"""
import time
import os
import random
import hashlib
from urlparse import urljoin
import sys

import requests
from bs4 import BeautifulSoup

class Xicidaili():

    def __init__(self):

        #文件路径
        self.baseDir = os.path.dirname(__file__)
        self.proxyPath = os.path.join(self.baseDir,'proxy.txt')
        #网页缓存文件夹路径
        self.htmlCachePath = os.path.join(self.baseDir,'.cache')
        #伪装头部
        self.headers = {'Host':'www.xicidaili.com',
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Refer':'http://www.xicidaili.com/',
                        'Accept-Encoding':'gzip, deflate, sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        }
        #起始网址
        self.start_urls = ['http://www.xicidaili.com/nn/',
                           'http://www.xicidaili.com/nt/',
                           'http://www.xicidaili.com/wn/',
                           'http://www.xicidaili.com/wt/']
        #页面过期时间
        self.htmlExpireTime = 3600

    #下载网页
    def downloadPage(self,url):

        r = requests.get(url=url,headers=self.headers)
        if r.status_code == 200:
            return r.content
        else:
            return False

    #缓存网页
    def saveHtmlCache(self,content,name):
        try:
            filepath = os.path.join(self.htmlCachePath,name+'.html')
            with open(filepath,'w') as f:
                f.write(content)
        except Exception as e:
            print '写入文件出错,请检查','\n',e

    #检测网页缓存是否存在
    def checkExistCache(self,name):

        filePath = os.path.join(self.htmlCachePath,name+'.html')
        if os.path.exists(filePath):
            return True
        else:
            return False


    #加载网页缓存
    def loadHtmlCache(self,name):
        pass
        try:
            filepath = os.path.join(self.htmlCachePath,name+'.html')
            with open(filepath,'r') as f:
                return f.read()
        except Exception as e:
            print '读取混存文件出错,请检查!','\n',e
            return False
    #获取签名
    def getSignName(self,string):

        return hashlib.sha1(string).hexdigest()

    #解析列表页
    def parseListPage(self,content):
        pass
        soup = BeautifulSoup(content,'lxml')
        #获取tr标签
        try:

            return [[tr.find_all('td')[1].get_text(),
                     tr.find_all('td')[2].get_text(),
                     tr.find_all('td')[5].get_text()] for tr in soup.find_all('tr') if tr.td]
        except Exception as e:
            print '解析列表页出现错误:','\n','e'
            return False

    #获取下一页
    def parseNextUrl(self,content,url):

        soup = BeautifulSoup(content,'lxml')
        link = soup.find('a',rel='next')
        return urljoin(url,link)

    #输出数据到文件
    def saveToFile(self,*args):
        string = ''
        for item in args:
            string += ','.join(item)+'\n'
        print string
        try:
            with open(self.proxyPath,'w') as f:
                f.write(string)
            print '代理已保存至文件'
        except Exception as e:
            print '写入代理出错,请检查!'

    #忽略缓存版本
    def getByNoCache(self):

        lists = []
        for url in self.start_urls:
            name = self.getSignName(url)
            content = self.downloadPage(url)
            self.saveHtmlCache(content,name)
            lists += self.parseListPage(content)
            time.sleep(2)
        self.saveToFile(*lists)

    #依赖缓存版本
    def getByCache(self):

        lists = []
        for url in self.start_urls:
            name = self.getSignName(url)
            if not self.checkExistCache(name):
                content = self.downloadPage(url)
                self.saveHtmlCache(content,name)
            else:
                content = self.loadHtmlCache(name)
            lists += self.parseListPage(content)
        self.saveToFile(*lists)

    #检测命令行参数
    def run(self):
        
        if len(sys.argv) == 1:
            self.getByCache()
        elif sys.argv[1] == 1:
            self.getByNoCache()

if __name__ == '__main__':
    test = Xicidaili()
    test.run()










