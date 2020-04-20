
#second try, memory limit exceeded in last big test case
def satisfied(l): 
    if l==[]: 
        return False
    if (x,y)==l: 
        return True 
    return False


def generategeometricsequence(): 

    if x%2==y%2: 
        return "IMPOSSIBLE"
    
    l=[]
    l1=[[]]
    directions=["N","S","W","E"]
    i=-1
    p=1
    while not satisfied(l): 
        i+=1
        #l=[]
        s=""
        curr_term=p*pow(2,i)
        if i==0: #define base case
            for el in directions: 
                if el=="N" and not satisfied(l):
                    curr_dir="N"
                    curr_sum=(0,1*curr_term)
                    l1[i].append([curr_dir,curr_sum])
                    #print(i)
                    l=l1[i][0][1]
                    v=0

                elif el=="S" and not satisfied(l):
                    curr_dir="S"
                    curr_sum=(0,-1*curr_term)
                    l1[i].append([curr_dir,curr_sum]) # use append, do not use add
                    l=l1[i][1][1]
                    v=1
                    
                elif el=="W" and not satisfied(l): 
                    curr_dir="W"
                    curr_sum=(-1*curr_term,0)
                    l1[i].append([curr_dir,curr_sum])
                    l=l1[i][2][1]
                    v=2
                                    
                elif el=="E" and not satisfied(l): 
                    curr_dir="E"
                    curr_sum=(1*curr_term,0)
                    l1[i].append([curr_dir,curr_sum])
                    l=l1[i][3][1]
                    v=3

            if satisfied(l): 
                return l1[i][v][0]
        l1.append([])

        v=-1
        
        for e in l1[i-1]:
            if e:
                a,b=e
            else: 
                b=(0,0)
            for el in directions: 
                v+=1
                if el=="N" and not satisfied(l):
                    curr_dir=a+"N"
                    curr_sum=tuple(map(sum, zip((0,1*curr_term), b)))
                    l1[i].append([curr_dir,curr_sum])
                    #[sum(x) for x in zip(*l)]
                    l=l1[i][v][1]

                elif el=="S" and not satisfied(l):
                    curr_dir=a+"S"
                    curr_sum=tuple(map(sum, zip((0,-1*curr_term), b)))
                    l1[i].append([curr_dir,curr_sum])
                    l=l1[i][v][1]
                    
                elif el=="W" and not satisfied(l): 
                    curr_dir=a+"W"
                    curr_sum=tuple(map(sum, zip((-1*curr_term,0), b)))
                    l1[i].append([curr_dir,curr_sum])
                    l=l1[i][v][1]
                                    
                elif el=="E" and not satisfied(l): 
                    curr_dir=a+"E"
                    curr_sum=tuple(map(sum, zip((1*curr_term,0), b)))
                    l1[i].append([curr_dir,curr_sum])
                    l=l1[i][v][1]

                if satisfied(l): 
                    return l1[i][v][0]
        l1.append([]) #create new list


T=int(input().strip())
for i in range(T): 
    casenum=i+1 
    x,y=input().strip().split(" ")
    x=int(x)
    y=int(y)
    target=(x,y)
    st=generategeometricsequence()
    print("Case #"+str(casenum)+": "+str(st))
    # print(lofvisited)
                    
                    
                
                