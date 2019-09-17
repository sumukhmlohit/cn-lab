n=int(input('enter the number of elements in the dictionary'))
d={}
for i in range(1,n+1):
	key=int(input("Enter key"))
	ndet=int(input("enter the number of details"))
	v=[]        
	for j in range(0,ndet):
		u=raw_input("Enter details")
		v.append(u)
	d[key]=v

	print(d)	

newdi=(key:value for (key:value) in d.items() if key%2==0}
print(newdi)
		

