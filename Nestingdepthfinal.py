"""


So the observation that the number of parenthesis between 
each number is exactly that number subtract the previous number => then (, 
otherwise, )

"""


def output(cases): 
    global sol
    sol=""
    if len(cases)==1: 
        sol="("*int(cases)+cases+")"*int(cases)
        
    else:
        for i in range(len(cases)-1): 
            if i==0: #def basecase 
                sol+="("*int(cases[i])
            
            if int(cases[i])>int(cases[i+1]): 
                sol+=cases[i]
                sol+=")"*(int(cases[i])-int(cases[i+1]))
                

            if int(cases[i])<int(cases[i+1]): 
                sol+=cases[i]
                sol+="("*(int(cases[i+1])-int(cases[i]))
                

            if int(cases[i])==int(cases[i+1]): 
                sol+=cases[i]

        sol+=cases[len(cases)-1]
        sol+=int(cases[len(cases)-1])*")"
    return sol 


T=int(input().strip())
for a in range(T): 
    cases=str(input().strip())
    casenum=a+1
    output(cases)
    print("Case #"+str(casenum)+": "+str(sol))
    
