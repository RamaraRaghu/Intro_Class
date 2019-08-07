#Rakshith Raghu (rr5de)

vowel = ['a','e','i','o','u','y']

word = str(input("Please give me a word: ")).lower()

syllables = 0

for i in range(len(word)-1):
    if(word[i] in vowel):
            if(word[i+1] in vowel):
                syllables = syllables + 1
            elif(word[i-1] in vowel):
                syllables = syllables
            else:
                syllables = syllables + 1

if(word[-1] in vowel):
    if(word[-2] in vowel):
        syllables = syllables
    elif(word[-1] != vowel[1]):
        syllables = syllables + 1
if(syllables == 0):
    syllables = 1
print("The word", word, "has",syllables, "syllables.")

