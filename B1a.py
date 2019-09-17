lis=[]
x=input('Enter no of nos')
for i in range(1,x+1):
	n=input('Enter a no')
	lis.append(n)
print(lis)	
res = [] 
for i in lis: 
    if i not in res: 
        res.append(i) 
   
print ("The list after removing duplicates : " + str(res)) 
re=[i for i in lis if i%2==0]
print(re)
res.reverse()
print(res)

