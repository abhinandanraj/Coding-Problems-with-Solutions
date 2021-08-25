def palindrome(string):
    revString = string[::-1]
    if string == revString:
        print('{} is Palindrome'.format(string))
    else:
        print('{} is not Palindrome'.format(string))

if __name__ == '__main__':
    userInput = str(input('Enter a string to check for Palindrome: '))
    palindrome(userInput)
