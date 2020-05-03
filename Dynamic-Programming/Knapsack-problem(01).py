# 0/1 Knapsack Problem

val=list(map(int,input().split())) # value
wt=list(map(int,input().split())) # weights for each value
weight=int(input())  # Required weight
t=[]
for i in range(len(val)):
    t.append([0]*8)
for i in range(1,len(val)):
    for j in range(1,weight+1):
        if j<wt[i]:
            t[i][j]=t[i-1][j]	# stores previous values 
        else:
            t[i][j]=max(val[i]+t[i-1][j-wt[i]],t[i-1][j])
print(t[-1][-1])
a=t[-1][-1]
j=weight
i=len(wt)-1
b=[] # stores the weights which are taken
while(j>=0 and i>=0):
    if t[i][j]==a:
        i=i-1
    else:
        b.append(wt[i+1])
        a=t[i][j-wt[i+1]]
        j=j-wt[i]
for _ in range(len(b)):
    print(b.pop(),end=' ') # Displays each weight which are taken to find required weiht
