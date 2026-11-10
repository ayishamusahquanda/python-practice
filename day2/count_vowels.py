sentence = input("Enter a sentence: ")
vowels = "aeiou"
vowel_count = 0

for s in sentence:
    if s.lower() in vowels:
        vowel_count += 1

print(f"Total vowels found: {vowel_count}")

