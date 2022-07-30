import requests
from bs4 import BeautifulSoup


url = 'https://docs.python.org/3/library/turtle.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
prelink = 'https://docs.python.org/3/library/turtle.html'
filename = 'turt.txt'

f=open('C:\\giz\\'+filename, 'w')
f.write('')
f.close()
f=open('C:\\giz\\'+filename, 'a')

urls=[]
for link in soup.find('div', 'sphinxsidebar', True).find_all('a'):
    urls.append(link.get('href')) if (((urls.count(link.get('href')) < 1) and ('..' not in link.get('href'))) and ('.html' not in link.get('href'))) and ('.rst' not in link.get('href')) else ''

count=0
for link in urls:
    count+=1
    print('grabbing '+str(count)+'\\'+str(len(urls))+'\t'+str(link.translate(link.maketrans('', '', '#'))))
    biglink = prelink+str(link)
    reqs=requests.get(biglink)
    soup=BeautifulSoup(reqs.text, 'html.parser')
    # f.write(str(soup.get_text())+'\n')
    page=str(soup.find('section').get_text()).encode('utf-8').decode('ascii', 'ignore')
    # mytable=page.maketrans('\n', chr(32))
    f.write('**********************'+link.translate(link.maketrans('', '', '#'))+'**********************\n\n'+page+'\n\n')
f.close()