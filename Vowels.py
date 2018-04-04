userinput = input("please enter a word")

vowels = frozenset("aeiou")

print(userinput)

newWord = set(userinput).difference(vowels)

print(newWord)