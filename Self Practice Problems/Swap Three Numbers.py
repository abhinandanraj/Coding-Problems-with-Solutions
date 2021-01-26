# Write a program to Swap Three Numbers.

n1=int(input())
n2=int(input())
n3=int(input())

n1=n1+n2+n3
n2=n1-n2-n3
n3=n1-n2-n3
n1=n1-n2-n3

print("After Swapping")
print(n1)
print(n2)
print(n3)
