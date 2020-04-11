"""
For this question, we need to start by looking at cases 
in the format *"somestring"* because, if the asterisis are 
at both ends, we can append any strings to both side of the asteris
considering extreme cases as such are useful. 
Then we can merge these ones together into one bigger string. 
"""


def solu(inputstot): 
    prefix=[]
    suffix=[]

    for i in inputstot: 
        prefix1=""
        suffix1=""
        l=0
        while i[l]!="*": #find longest prefix 
            prefix1+=i[l]
            prefix.append(prefix1)
            l+=1
        j=len(i)-1
        while i[j]!="*": 
            suffix1+=i[j]
            suffix.append(suffix1)
            j-=1
    if prefix: 
        maxpre=max(prefix,key=len)
    if suffix:
        maxsuf=max(suffix,key=len)

    #maxsuff=maxsuf[::-1]
    #print(maxsuff)
    #print(maxsuf)

    #check if maxpre and maxsuf requirements fulfilled
    if prefix:
        sol=maxpre
    else: 
        sol=""
    for i in inputstot: 
        p=""
        l=0
        while i[l]!="*":
            p+=i[l] 
            l+=1
        if prefix:
            if not maxpre.startswith(p): 
                return "*"
        s=""
        j=len(i)-1
        while i[j]!="*": 
            s+=i[j]
            j-=1
        if suffix:
            if not maxsuf.startswith(s): 
                return "*"
        while l<j:
            if i[l]!="*":
                sol+=i[l]
            l+=1
    sol+=maxsuf[::-1]
    return sol

T=int(input().strip())
for a in range(T): 
    cases=int(input().strip())
    casenum=a+1
    inputstot=[]
    for i in range(cases):
        inputs=str(input().strip())
        inputstot.append(inputs)
    sol=solu(inputstot) # got string object is not callable error
    print("Case #"+str(casenum)+": "+str(sol))
    


