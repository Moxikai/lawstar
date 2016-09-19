#!/usr/bin/env python
#coding:utf-8
"""
法律之星查询平台,通过关键字检索后,下载到本地数据库
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
from time import sleep
from urlparse import urljoin
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
from model import session,Law
class LawStar():

    #初始化
    def __init__(self,
                 titles,
                 rjs5_11=None,
                 rjs5_12=None,
                 rjs5_13=None,
                 rjs5_21=None,
                 rjs5_22=None,
                 rjs5_23=None,
                 contents=None,
                 button=u'查询'):

        self.url = 'http://law1.law-star.com/search'
        self.titles = titles
        self.rjs5_11 = rjs5_11
        self.rjs5_12 = rjs5_12
        self.rjs5_13 = rjs5_13
        self.rjs5_21 = rjs5_21
        self.rjs5_22 = rjs5_22
        self.rjs5_23 = rjs5_23
        self.contents = contents
        self.button = button
        self.dbts = ['chl','iel','lar','hnt','cas','scs','eag','dae','ara','art']
        #请求设置
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate, sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        }

    #获取列表页源码
    def getListPage(self,page=1):
        params = {}
        params['titles'] = self.titles
        params['rjs5_11'] = self.rjs5_11
        params['rjs5_12'] = self.rjs5_12
        params['rjs5_13'] = self.rjs5_13
        params['rjs5_21'] = self.rjs5_21
        params['rjs5_22'] = self.rjs5_22
        params['rjs5_23'] = self.rjs5_23
        params['contents'] = self.contents
        params['dbt']=self.dbts
        params['button']=self.button
        #默认1页,不传递参数
        if page > 1:
            params['p']=page

        r = requests.get(url=self.url,headers=self.headers,params=params,)
        #print r.content
        return r.content

    #检测列表页是否存在翻页
    def checkNext(self,content):
        tree = etree.HTML(content,etree.HTMLParser(encoding='utf-8'))
        nextURL = tree.xpath('//div[@id="fenye"]/a[3]/@href')
        if nextURL:
            return nextURL[0]
        else:
            return False


    #解析列表
    def parseListPage(self,content):

        tree = etree.HTML(content,etree.HTMLParser(encoding='utf-8'))
        titles = tree.xpath('//a[@class="g"]/@title')
        urls = tree.xpath('//a[@class="g"]/@href')
        return [{"title":titles[i],"url":urljoin(self.url,urls[i])} for i in range(len(titles))]


    #下载详细页面
    def getDetailPage(self,url,title):
        r = requests.get(url,headers = self.headers)
        if r.status_code == 200:
            return r.content
        else:
            return False


    #解析详情页面
    def getDetail(self,url,title):
        content = self.getDetailPage(url,title)
        if content:
            tree = etree.HTML(content,etree.HTMLParser(encoding='utf-8'))
            #解析概要信息
            wenhao = tree.xpath('//*[@id="fgzw_right2"]/ul/li[2]/text()') #法规文号
            wenhao = [i.split('】')[-1].strip() for i in wenhao] #清理前缀

            publish_date = tree.xpath('//*[@id="tdat"]/text()') #发布日期
            publish_date = [i.split('】')[-1].strip() for i in publish_date] #清理前缀

            done_date = tree.xpath('//*[@id="fgzw_right2"]/ul/li[4]/text()') #实施日期
            done_date = [i.split('】')[-1].strip() for i in done_date]

            publish_department = tree.xpath('//*[@id="tdpt"]/text()') #发布部门
            publish_department = [i.split('】')[-1].strip() for i in publish_department]

            law_class = tree.xpath('//*[@id="fgzw_right2"]/ul/li[6]/text()') #效力等级
            law_class = [i.split('】')[-1].strip() for i in law_class]

            #转成字符串
            zhengwen = self.parseZhengwen(content)

            #获取url签名
            id = hashlib.sha1(url).hexdigest()
            print 'id是%s'%(id)
            return {'title':title,
                    'id':id,
                    'url':url,
                    'wenhao':wenhao[0],
                    'publish_date':publish_date[0],
                    'done_date':done_date[0],
                    'publish_department':publish_department[0],
                    'law_class':law_class[0],
                    'zhengwen':zhengwen}
        else:
            print '打开详情页面出错!'

    #解析大段正文
    def parseZhengwen(self,content):
        soup = BeautifulSoup(content,'lxml')
        list = soup.find('div',class_='zhengwen').contents
        return ''.join(unicode(s) for s in list if not s is None)

    #深度优先
    def getDataByDepth(self):
        page = 1
        existNext = 1
        while existNext:
            content = self.getListPage(page=page)
            dict_ = self.parseListPage(content)
            for item in dict_:
            #解析详情数据
                data = self.getDetail(item['url'],item['title'])
                sleep(0.5)
                if data:
                #保存
                    self.saveToSQLite(**data)

            #获取下一页
            if self.checkNext(content):
                page += 1
                sleep(1)
            else:
                existNext = 0



    #广度优先
    def getDataByScope(self):
        pass


    #保存到sqlite
    def saveToSQLite(self,**kwargs):
        if kwargs['id'] is None:
            print '程序出错,请检查'
            return False
        #检测数据是否存在
        law = session.query(Law).filter(Law.id == kwargs['id']).all()
        if len(law) > 0:
            pass
            print '数据已存在,不必重复保存'
        else:
            law = Law(id=kwargs['id'],
                      title=kwargs['title'],
                      url=kwargs['url'],
                      wenhao=kwargs['wenhao'],
                      publish_date=kwargs['publish_date'],
                      done_date=kwargs['done_date'],
                      publish_department=kwargs['publish_department'],
                      law_class=kwargs['law_class'],
                      zhengwen=kwargs['zhengwen'])
            session.add(law)
            session.commit()


    #保存到mysql
    def saveToMySQL(self):
        pass

    #保存到excel
    def saveToExcel(self):
        pass

    #保存到csv文件
    def saveToCSV(self):
        pass


if __name__ == '__main__':
    pass
    test= LawStar(titles='传销')
    test.getDataByDepth()



