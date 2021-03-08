def vowel_count(string1):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in string1:
        if alphabet in vowel:
            count = count +1
    print(count)

string1 = input()
vowel_count(string1)
