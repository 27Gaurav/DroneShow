class Stack:
    
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def push(self,e):# appends an element in the stack
        self._data.append(e)
    def top(self): # returns the topmost element of the stack
        return self._data[-1]
    def pop(self):# returns the topmost element of the stack and knocks it out of the stack
        return self._data.pop()
    def __str__(self):
        return ''.join(str(self._data)) + ">"
def findPositionandDistance(info):
    n=len(info) 
    l=[0,0,0] #initialised an empty list which will keep track of coordinates
    l1=Stack() 
    a=0 #keeps track of the distance covered
    i=0 # counter to go through the input list
    c=1 #multiplier
    while i<n: #goes through the list till the end
        if info[i].isnumeric():#checks if the input is a number
            for j in range (i,n): #for loop to check how long is the number
                if not info[j].isnumeric():
                    break
            b= int(info[i:j]) 
            l1.push(b) #push the number in the array
            c=c*l1.top() # if any new multiplier (new opening bracket) is encountered insert it in the stack and also multiply it with c
            i=j+1 #increment i
        if info[i]==')': # if the loop encouters a closing bracket implies that the latest bracket is closed , so we need to divide the corresponding multiplier
            c=c//l1.pop() # also remove it from the stack
            i+=1
            
                 
            
        elif info[i]=='+':
            a+=1*c # increments the distance according to the current multiplier
            if info[i+1]=='X':
                l[0]+=1*c # increments the coordinates according to the current multiplier
            elif info[i+1]=='Y':
                l[1]+=1*c
            elif info[i+1]=='Z':
                l[2]+=1*c
            i+=2
        elif info[i]=='-':
            a+=1*c
            if info[i+1]=='X':
                l[0]-=1*c
            elif info[i+1]=='Y':
                l[1]-=1*c

            elif info[i+1]=='Z':
                l[2]-=1*c
            i+=2
    return(l+[a])   # returns a list containg coordinates and distance    
