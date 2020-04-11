


def output(inputstot,casenum): 
    w1=[]
    w2=[]
    mid=[]

    for i in inputstot:
        if i[-1]=="*":
            w1.append(i)
        elif i[0]=="*": 
            w2.append(i)
        else:
            mid.append(i)

    if w1:
        w1.sort(key=len)
        maxkey1=w1[0][:len(maxkey1)-1]

    if w2:
        w2.sort(key=len)
        maxkey2=w2[0][1:]

    if w2:
        for i in range(1,len(w2)): 
            if not w2[i][1:].endswith(maxkey2): 
                return "*" 
            if len(w2[i])!=0:
                maxkey2=w2[i][1:]

    if w1:
        for i in range(1,len(w1)): 
            if not w1[i][:len(maxkey1)-1].startswith(maxkey1): 
                return "*" 
            if len(w1[i])!=0:
                maxkey1=w1[i][:len[maxkey1]-1]
    
    if w1 and w2:
        if len(maxkey2)>len(maxkey1): 
            maxkey=maxkey2[1:]
        else: 
            maxkey=maxkey1[:len(maxkey1)-1]
    elif not w2: 
        maxkey=maxkey1 
    elif not w1: 
        maxkey=maxkey2

    if mid:
        for i in mid: 
            a=i.index("*")
            string1=i[:a-1]
            string2=i[a+1:]
            if not maxkey.startswith(string1) or not maxkey.endswith(string2): 
                return "*"

    return maxkey


T=int(input().strip())
for a in range(T): 
    cases=int(input().strip())
    casenum=a+1
    inputstot=[]
    for i in range(cases):
        inputs=str(input().strip())
        inputstot.append(inputs)
    sol=output(inputstot,casenum)
    print("Case #"+str(casenum)+": "+str(sol))
    

