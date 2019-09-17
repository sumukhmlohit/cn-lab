li=[1,2,3,4,5,6]

newli=[i*3 for i in li]

print(newli)

lisum =reduce((lambda x,y:x+y),li)

print(lisum)

newlisum =reduce((lambda x,y:x+y),newli)

print(newlisum)

 
