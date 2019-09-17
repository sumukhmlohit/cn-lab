x=input("Enter a number")
ones=["one","two","three","four","five","six","seven","eight","nine"]
tens=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
one=x%10
ten=(x-one)/10
print(tens[ten-1])
print(ones[one-1])
