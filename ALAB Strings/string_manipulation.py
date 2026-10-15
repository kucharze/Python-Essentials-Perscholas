sentence = input("Enter a sentence: ")

upCase = sentence.upper()
print("Uppercase:", upCase)

reverse = sentence[::-1]
print("Reversed:", reverse)

numVowels = 0

print("")

for char in sentence:
    if char.upper() in 'AEIOU':
        print("Found a vowel.")
        numVowels += 1

print("")
print("Number of vowels:", numVowels)