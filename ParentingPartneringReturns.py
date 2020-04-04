""" 
Range intersections => assign either C or J to the first task, if range intersection is not none, assign to the other person, for every step 
return new set and the person assigned
""" 


T=int(input().strip())


def optimize(matrix,dimension): 
    global sol
    global final
    final=""
    sol=""
    for i in range(dimension): 
        a, b= matrix[i][0],matrix[i][1]
        if i==0: 
            Cbest=range(a,b)
            setCbest=set(Cbest)
            setVbest=set()
            sol=sol+"C"
        else: 
            temp1=set(range(a, b))
            temp=range(a, b)
            if len(set.intersection(temp1,setCbest))== 0: 
                sol=sol+"C"
                setCbest.update(temp)
            else: 
                if len(set.intersection(temp1,setVbest))==0:                  
                    sol=sol+"J"
                    setVbest.update(temp)
                else: 
                    return False
    final=sol

def out(casenum,matrix,dimension): 
    optimize(matrix,dimension)
    if final=="":
        print("Case #"+str(casenum)+": IMPOSSIBLE")
    else: 
        print("Case #"+str(casenum)+": "+final)


for i in range(T): 
    casenum=i+1
    dimension=int(input().strip())
    matrix=[[] for i in range(dimension)]
    for i in range(dimension): 
        beg,end=input().strip().split(" ")
        beg=int(beg)
        end=int(end)
        matrix[i].append(beg)
        matrix[i].append(end)
    out(casenum,matrix,dimension)
