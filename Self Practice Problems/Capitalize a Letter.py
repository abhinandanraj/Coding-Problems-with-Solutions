""" Q:Write a function that capitalize the letter according to index.

    Sample Input: bootcamp
    sample Output: BootCamp

    Sample Input: workspace
    Sample Output: WorkSpace

"""

def letter_capitalize(letter):
    first_half = letter[:4]
    second_half = letter[4:]

    return first_half.capitalize() + second_half.capitalize()

if __name__== "__main__":
        

    word = input()
    print(letter_capitalize(word))
    
