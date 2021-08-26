def isPalindrome(n):  
    
    reverse = 0
    reminder = 0
    while(n != 0):
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = int(n / 10)
    return reverse

num = int(input('Enter the number: '))

reverse = isPalindrome(num)
if(num == reverse):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')
