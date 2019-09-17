def Atomic_Dictionary():	
	dict={}

	n=input('Enter no of elements')

	for i in range(1,n+1):
		x=raw_input("Enter key")
		val=raw_input("Enter value")
		dict[x]=val

	print(dict)

	print(len(dict))	

	y=raw_input('Enter element symbol to search')
	print(dict[y])



