
def satisfied(l): 
    if l==[]: 
        return False
    s,e=[sum(x) for x in zip(*l)] #whereby l is a list of tuples
    if (x,y)==(s,e): 
        return True 

def generategeometricsequence(): 
    global lofvisited
    a=1
    lofvisited=[[]*10000]
    #l=[]
    l=[]
    directions=["n","s","w","e"]
    ct=0
    
    while not satisfied(l):
        ct+=1
        l=[] #want to initiate new list
        l1=[]
        s=""
        for i in range(0,5): 
            
            curr_term=a*pow(2,i)
            #print(curr_term)
            if not satisfied(l): 
                for el in directions: 
                    if satisfied(l): 
                        break
                    s+=el
                    if i>len(s): 
                        break
                    if len(lofvisited)>a:
                        if s not in lofvisited[a]:
                            print(s)
                            a=len(s)-1
                            lofvisited[a]+=s
                            lofvisited.append([])
                            if el=="n":
                                l.append((0,1*curr_term))
                                l1.append("N")
                                break
                            elif el=="s": 
                                l.append((0,-1*curr_term))
                                l1.append("S")
                                break
                            elif el=="w": 
                                l.append((-1*curr_term,0))
                                l1.append("W")
                                break
                            elif el=="e": 
                                l.append((1*curr_term,0))
                                l1.append("E")
                                break

        if ct==1000: 
            return "IMPOSSIBLE"
            break 

    st=""
    for i in l1: 
        st+=i
    return st
                            

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
                    
                    
                
                


