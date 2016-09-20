from bs4 import BeautifulSoup

file = '/Users/zhuyuliang/PycharmProjects/law/.cache/66807d65e560b5ab16b6a6803a0c0dce68d96251.html'
with open(file,'r') as f:
    content = f.read()

soup = BeautifulSoup(content,'lxml')
list = [(tr.find_all('td')[1].get_text(),
         tr.find_all('td')[2].get_text(),
         tr.find_all('td')[5].get_text()) for tr in soup.find_all('tr') if tr.td]
for item in list:
    print item,'\n'
