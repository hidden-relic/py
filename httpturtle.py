import requests
from bs4 import BeautifulSoup

url = 'https://lua-api.factorio.com/latest/LuaGuiElement.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
# prelink = 'https://docs.python.org/3/library/turtle.html'
filename = 'fact_gui_elements.txt'

f=open('C:\\giz\\'+filename, 'w').close()
f=open('C:\\giz\\'+filename, 'a')

text=str(soup.find('ul').get_text()).encode('utf-8').decode('ascii', 'ignore')
text+='\n#######################\n'
text+=str(soup.find('div', 'class-attributes-sorted').get_text()).encode('utf-8').decode('ascii', 'ignore')
text+='\n#######################\n'
text+=str(soup.find(id="LuaGuiElement.add").get_text()).encode('utf-8').decode('ascii', 'ignore')
text+='\n#######################\n'
f.write(text)
f.close()
f=open('C:\\giz\\'+filename, 'r')
# a=[line.strip().replace("\n", "") for line in f.readlines() if line == "\n"]
# a=[line.strip() for line in f.readlines()]
a=[line.strip().replace(chr(32), '') if line == chr(32) else line.strip() for line in f.readlines()]
print(str(a))
f.close()
f=open('C:\\giz\\'+filename, 'w').close()
f=open('C:\\giz\\'+filename, 'a')
[f.write(line+"\n") if line != '' else f.write(line) for line in a]
f.close()
print('done')

# text=soup.find('div', 'sphinxsidebar', True).find_all('a'):
#     urls.append(link.get('href')) if (((urls.count(link.get('href')) < 1) and ('..' not in link.get('href'))) and ('.html' not in link.get('href'))) and ('.rst' not in link.get('href')) else ''

# count=0
# for link in urls:
#     count+=1
#     print('grabbing '+str(count)+'\\'+str(len(urls))+'\t'+str(link.translate(link.maketrans('', '', '#'))))
#     biglink = prelink+str(link)
#     reqs=requests.get(biglink)
#     soup=BeautifulSoup(reqs.text, 'html.parser')
#     # f.write(str(soup.get_text())+'\n')
#     page=str(soup.find('section').get_text()).encode('utf-8').decode('ascii', 'ignore')
#     # mytable=page.maketrans('\n', chr(32))
#     f.write('**********************'+link.translate(link.maketrans('', '', '#'))+'**********************\n\n'+page+'\n\n')
# f.close()