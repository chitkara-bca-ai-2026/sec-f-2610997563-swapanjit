

sentence = input("Enter a sentence: ")

# Initialize counters
words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for ch in sentence:

    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch == " ":
        spaces += 1

    else:
        special_characters += 1

total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("\n" + "=" * 40)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 40)

print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)

print("\n--- Summary ---")
print("Total letters:", total_letters)
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)