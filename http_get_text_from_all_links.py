import requests
from bs4 import BeautifulSoup
import os

url = 'https://lua-api.factorio.com/latest/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
prelink = 'https://lua-api.factorio.com/latest/'


urls=[]
names=[]
for link in soup.find('ul', 'panel-hole', True).find_all('a'):
    print(link.get('href'))
    urls.append(link.get('href'))
    names.append(link.get('href').replace('#', '').replace('.html', '.txt'))

urls = set(urls)
count=0
for link in urls:
    f=open('C:\\giz\\factorio\\'+names[count], 'w')
    count+=1
    print('grabbing '+str(count)+'\\'+str(len(urls))+'\t'+str(link.translate(link.maketrans('', '', '#'))))
    biglink = prelink+str(link)
    reqs=requests.get(biglink)
    soup=BeautifulSoup(reqs.text, 'html.parser')
    # f.write(str(soup.get_text())+'\n')
    page=str(soup.find('div', 'docs-content', True).get_text(   )).encode('utf-8').decode('ascii', 'ignore').replace('\n\n', '\n')
    # mytable=page.maketrans('\n', chr(32))
    f.write('**********************'+link.translate(link.maketrans('', '', '#'))+'**********************\n\n'+page+'\n\n')
    f.close()
    os.remove('C:\\giz\\factorio\\'+link.replace('#', ''))