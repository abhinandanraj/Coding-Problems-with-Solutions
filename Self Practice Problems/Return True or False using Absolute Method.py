"""
Q: Write a function that return True or False using Absolute Method.
   Given an integer n, return True if n is within 10 of either 100 or 200.

   Sample Input: 90 
   Sample Output: True

   Sample Input: 150
   Sample Output: False

"""

def absolute_value(n):
    return (abs(100-n) <=10) or (abs(200-n) <= 10)

if __name__ == "__main__":

    num = int(input())
    print(absolute_value(num))
