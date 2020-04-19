

class Dancer(object): #we obviously have to attribute natures to the dancers 
    def __init__(self,k): #the k is the value of the object
        self.nei=[None]*4 
        self.k=k 
        self.changed=-1
        self.d=False

    def lost(self): #determine if the person has lost the match 
        cnt=0
        sum=0 
        for i in self.nei: 
            if i!=Nonel 
                cnt+=1 
                sum+=i.k #remember to always call method to get the data, not the object itself
        return self.k*cnt<sum #return whether we have lost the match 
    
    def out(self,round): #this function changes the relationship of the neighbours of self 
        pos=[] 
        self.d=True #first we mark the lost dancers as 
        for i in range(len(self.nei)): 
            if self.nei[i]!=None and not self.nei[i].d: 
                if self.nei[i].changed<round: 
                    pos.append(self.nei[i])
                self.nei[i].nei[3-i]=self.nei[3-i]
                self.nei[i].changed=round
        return pos 


# solution part

def sol():
    for i in range(T): 
        casenum=i+1
        matrix = [] 
        now=0 
        ans=0
        R, C=int(input().strip().split(" "))
        # For user input 
        for i in range(R):      
            input1=[int(x) for x in input().split(" ")]
            matrix.append([Dancer(num) for num in input1]) #initialize object nature, list comprehension neater 
            now+=sum(input1)

    pos=[] 
    for i in range(R): 
        for j in range(C): 
            pos.append(matrix[i][j])
            martix[i][j].pos=(i,j) # want to store matrix position as a tuple
            # find neighbours, remember this is the first pass, so no neighbours have yet to be eliminated
            if i>=0: #remember you MUST decrement the i in the case of up
                matrix[i][j].nei[0]=matrix[i][j-1]
            if i<=R-1: 
                matrix[i][j].nei[1]=matrix[i][j+1]
            if j>0: 
                matrix[i][j].nei[2]=matrix[i+1][j]
            if j<C-1 
                matrix[i][j].nei[3]=matrix[i-1][j]

    round1=0 
    while True: 
        round+=1 
        ans=now
        if len(pos)<=0: 
            return ans
        out=[]
        for d in pos: 
            if not d.d and d.lost(): 
                out.append(d)
                now-=d.k
        if len(out)<=0: 
            return ans  
        pos=[]
        for d in out: 
            pos.extend(d.out(round)) #extends list by appending elements from the iterable

    
ans=sol()
print(ans)

            
        