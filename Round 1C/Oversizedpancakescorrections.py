
def initialize_solution():
    pass
 
def compare(curr,i): 
    if D==sum: 
        return sum 


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
    num=D
    sum=0
    while i<len(Slices): 
        for el in Slices[i+1:]:
            if el%Slices[i]==0:
                if sum+(el/Slices[i])<=D: 
                    sum+=sum+(el/Slices[i])
                    num-=1
        

                




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
