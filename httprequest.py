import requests
from bs4 import BeautifulSoup


url = 'https://docs.python.org/3/library/tk.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
f=open('C:\\giz\\tk.txt', 'w')
f.write('')
f.close()
f=open('C:\\giz\\tk.txt', 'a')

urls = ['tkinter.html#module-tkinter', 'tkinter.tix.html#module-tkinter.tix', 'tkinter.html#architecture', 'tkinter.html#tkinter-modules', 'tkinter.html#tkinter-life-preserver', 'tkinter.html#a-hello-world-program', 'tkinter.html#important-tk-concepts', 'tkinter.html#understanding-how-tkinter-wraps-tcl-tk', 'tkinter.html#how-do-i-what-option-does', 'tkinter.html#navigating-the-tcl-tk-reference-manual', 'tkinter.html#threading-model', 'tkinter.html#handy-reference', 'tkinter.html#setting-options', 'tkinter.html#the-packer', 'tkinter.html#packer-options', 'tkinter.html#coupling-widget-variables', 'tkinter.html#the-window-manager', 'tkinter.html#tk-option-data-types', 'tkinter.html#bindings-and-events', 'tkinter.html#the-index-parameter', 'tkinter.html#images', 'tkinter.html#file-handlers', 'tkinter.colorchooser.html', 'tkinter.font.html', 'dialog.html', 'dialog.html#module-tkinter.simpledialog', 'dialog.html#module-tkinter.filedialog', 'dialog.html#native-load-save-dialogs', 'dialog.html#module-tkinter.commondialog', 'tkinter.messagebox.html', 'tkinter.scrolledtext.html', 'tkinter.dnd.html', 'tkinter.ttk.html', 'tkinter.ttk.html#using-ttk', 'tkinter.ttk.html#ttk-widgets', 'tkinter.ttk.html#widget', 'tkinter.ttk.html#standard-options', 'tkinter.ttk.html#scrollable-widget-options', 'tkinter.ttk.html#label-options', 'tkinter.ttk.html#compatibility-options', 'tkinter.ttk.html#widget-states', 'tkinter.ttk.html#ttk-widget', 'tkinter.ttk.html#combobox', 'tkinter.ttk.html#options', 'tkinter.ttk.html#virtual-events', 'tkinter.ttk.html#ttk-combobox', 'tkinter.ttk.html#spinbox', 'tkinter.ttk.html#id1', 'tkinter.ttk.html#id2', 'tkinter.ttk.html#ttk-spinbox', 'tkinter.ttk.html#notebook', 'tkinter.ttk.html#id3', 'tkinter.ttk.html#tab-options', 'tkinter.ttk.html#tab-identifiers', 'tkinter.ttk.html#id4', 'tkinter.ttk.html#ttk-notebook', 'tkinter.ttk.html#progressbar', 'tkinter.ttk.html#id5', 'tkinter.ttk.html#ttk-progressbar', 'tkinter.ttk.html#separator', 'tkinter.ttk.html#id6', 'tkinter.ttk.html#sizegrip', 'tkinter.ttk.html#platform-specific-notes', 'tkinter.ttk.html#bugs', 'tkinter.ttk.html#treeview', 'tkinter.ttk.html#id7', 'tkinter.ttk.html#item-options', 'tkinter.ttk.html#tag-options', 'tkinter.ttk.html#column-identifiers', 'tkinter.ttk.html#id8', 'tkinter.ttk.html#ttk-treeview', 'tkinter.ttk.html#ttk-styling', 'tkinter.ttk.html#layouts', 'tkinter.tix.html', 'tkinter.tix.html#using-tix', 'tkinter.tix.html#tix-widgets', 'tkinter.tix.html#basic-widgets', 'tkinter.tix.html#file-selectors', 'tkinter.tix.html#hierarchical-listbox', 'tkinter.tix.html#tabular-listbox', 'tkinter.tix.html#manager-widgets', 'tkinter.tix.html#image-types', 'tkinter.tix.html#miscellaneous-widgets', 'tkinter.tix.html#form-geometry-manager', 'tkinter.tix.html#tix-commands']
for link in urls:
    print('grabbing '+str(link))
    biglink = 'https://docs.python.org/3/library/'+str(link)
    reqs=requests.get(biglink)
    soup=BeautifulSoup(reqs.text, 'html.parser')
    # f.write(str(soup.get_text())+'\n')
    page=str(soup.get_text().encode('utf-8'))
    f.write('**********************'+link+'**********************\n\n'+page+'\n\n')
f.close()