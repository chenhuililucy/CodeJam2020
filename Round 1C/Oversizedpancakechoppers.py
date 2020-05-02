
def initialize_solution():
    pass
 
def compare(curr,i): 
    pass

import operator

def main():
    N,D=input().strip().split(" ")
    N=int(N)
    D=int(D)
    Slices=input().split(" ")
    a=[]
    for i in Slices: 
        a.append(int(i))
    Slices=a
    Slices.sort()
    i=0
    c=[]
    if D==2:
        for i in range(len(Slices)): 
            if Slices[i] in Slices[i+1:]: 
                return 0
            else: 
                continue 
        return 1
                
    elif D==3: 
        for i in range(len(Slices)): 
           
            if Slices.count(Slices[i])>=3: 
                #print("y")
                return 0 

        for i in range(len(Slices)): 
            if Slices.count(Slices[i])==2: 
                print("y")
                S=Slices[i:]+Slices[:i]
                print(S)
                for a in Slices[i+1:]+Slices[:i]: 
                    
                    if a>Slices[i]: 
                        return 1
            else: 
                if Slices.count(Slices[i])==1: 
                    print("y")
                    for a in Slices[i+1:]+Slices[:i]: 
                        print(a)
                        if a%Slices[i]==0: 
                            return 1
                #if CASE_NUMBER==3: 
                    #print()
                #print("ye")
            return 2
    #if 1 in c: 
        #return 1
        return min(c)

    return "l"


########################################## PROBLEM CONSTANTS

#OUTPUT_PREFIX = ""
OUTPUT_PREFIX = "Case #{}: "
INTERACTIVE = False
INTERACTIVE_WRONG_ANSWER = "WRONG"

#################################################### HELPERS



import sys

def read(callback=int, split=True):
    ipt = input().strip()
    if INTERACTIVE and ipt == INTERACTIVE_WRONG_ANSWER:
        sys.exit()
    if split:
        return list(map(callback, ipt.split()))
    else:
        return callback(ipt)

def write(value, end="\n"):
    if value is None: return
    try:
        if not isinstance(value, str): #checks if the object(first arg) is an instance or subclass of classinfo class(second argument)
            value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)
    if INTERACTIVE:
        sys.stdout.flush()

def solve_testcase():
    result = main()
    if result is not None:
        write(result)

if OUTPUT_PREFIX is None: # output prefix is the 
    solve_testcase() # call main function 
else:
    initialize_solution()

    """

    """

    TOTAL_CASES,= read() #always remember to modify

    for CASE_NUMBER in range(1, TOTAL_CASES+1):
        write(OUTPUT_PREFIX.format(CASE_NUMBER), end="") #want whatevers printed and the next thing printed to be in the same line
        solve_testcase()
