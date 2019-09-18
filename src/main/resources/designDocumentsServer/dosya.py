import re
def degistir(basla,bitir,sayfa,veri):
    """TODO: Docstring for degistir.
    :returns: TODO

    """
    f=open(sayfa,"r+")
    lines=f.readlines()
    f.seek(0)
    wlines=[]
    c=0
    flag=False
    print(veri)
    for line in lines:
        end=re.search(bitir,line)
        begin=re.search(basla,line)
        if begin:
            flag=True
            print ("basla")
            wlines.append(line)

        if end:
            flag=False
            print("bitir")
        if flag:
            print(flag)
            if c<len(veri):
                wlines.append(veri[c])
                print("eklenen yeni:%s" % veri[c])
            else:
                pass
            c+=1
        if not flag:
            wlines.append(line)
    print(wlines)
    f.seek(0)
    f.truncate()
    for line in wlines:
        f.write(line)
