from collections import Counter
file=open("file1.txt","r")
print(Counter(file.read().split()))




