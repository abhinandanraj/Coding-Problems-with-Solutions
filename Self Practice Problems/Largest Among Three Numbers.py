n1=int(input())
n2=int(input())
n3=int(input())

if(n1>n2) and (n1>n3):
    largest=n1
elif(n2>n1) and (n2>n3):
    largest=n2
else:
    largest=n3
print(largest)
