"""
Q: Write a program to Convert decimal to binary number using recursion.

Sample Input : 34
Sample Output : 100010

Sample Input : 142
Sample Output : 010001110

"""
def DecToBin(number):
    if number >= 1:
        DecToBin(number // 2)
    print(number % 2, end = '')

if __name__ == "__main__":

    value = int(input())
    DecToBin(value)
    print()
