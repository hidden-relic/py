from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)
import json

def main():
    datarawfile="C:\\giz\\dataraw.json"
    f=open(datarawfile, 'r').read()
    datarawlua=lua.table(f)
    datarawpy=dict(datarawlua)
    
    count=0
    for v in iter(datarawpy[1]):
        count+=1
        file=open('C:\\giz\\dataraw\\'+v+'.json', 'w')
        file.write(v)
        file.close()
        
    print('DONE. '+str(count)+' written.')
             

if __name__ == '__main__':
    main()

main()