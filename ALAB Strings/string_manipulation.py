sentence = input("Enter a sentence: ")

upCase = sentence.upper()
print("Uppercase:", upCase)

#
reverse = sentence[::-1]
print("Reversed:", reverse)

numVowels = 0

print("")
print("Finding vowels in the sentence...")
#find all vowels in the sentence
for char in sentence:
    if char.upper() in 'AEIOU':
        print("Found a vowel.")
        numVowels += 1


print("Number of vowels:", numVowels)
print("")

#Replace the spaces in the sentence with hyphens
hyphenated = sentence.replace(" ", "-")
print("Hyphenated:", hyphenated)