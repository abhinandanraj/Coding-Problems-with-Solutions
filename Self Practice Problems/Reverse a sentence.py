# Reverse the sentence
# ----------Method 1--------------------

def sentence_reverse(text):
  wordlist = text.split()
  reversed_list = wordlist[:: -1]
  reversed_sentence = " ".join(reversed_list)
  return reversed_sentence  

if __name__ == "__main__":
  sentence = input()
  print(sentence_reverse(sentence))

#-----------Method 2------------------
  
sentence = input("Enter a sentence :")
print(" ".join(reversed(sentence.split())))

