
def initialize_solution():
    pass
 
def compare(curr,i): 
    if abs(curr[0])+abs(curr[1])>i: 
        return False
    else: 
        return True 

import operator

def main():
    N=(0,1)
    W=(-1,0)
    E=(1,0)
    S=(0,-1)
    i=0
    #curr=(0,0)
    X,Y,direction=input().split(" ")
    X=int(X)
    Y=int(Y)
    curr=(X,Y)
    length=len(direction)
    if curr==(0,0):
        return 0
    while i<len(direction): 

        
        if i<len(direction) and direction[i]=="N": 
            curr=tuple(map(operator.add,curr,N))
            #curr+=N
        if i<len(direction) and direction[i]=="W": 
            #curr+=W
            curr=tuple(map(operator.add,curr,W))
        if i<len(direction) and direction[i]=="E": 
            #curr+=E
            curr=tuple(map(operator.add,curr,E))
        if i<len(direction) and direction[i]=="S": 
            #curr+=S
            curr=tuple(map(operator.add,curr,S))
            #print(curr)

        i+=1
        if compare(curr,i): 
            return i
        

    return "IMPOSSIBLE"


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

