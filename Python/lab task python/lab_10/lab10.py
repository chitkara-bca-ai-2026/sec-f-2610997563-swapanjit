print("=" * 40)
print("       TEXT PROCESSING TOOL")
print("=" * 40)

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# 2. Display a character at a specific position
position = int(input("Enter position for indexing: "))

if 0 <= position < len(sentence):
    print("Character at position", position, ":", repr(sentence[position]))
else:
    print("Invalid position!")

# 3. Extract a portion using string slicing
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))

print("Sliced string:", repr(sentence[start:end]))

# 4. Convert the sentence to uppercase
print("Uppercase             :", sentence.upper())

# 5. Convert the sentence to lowercase
print("Lowercase             :", sentence.lower())

# 6. Replace a word with another word
word = input("Enter word to replace: ")
replacement = input("Enter replacement word: ")

new_sentence = sentence.replace(word, replacement)
print("After replace         :", new_sentence)

# 7. Display the length of the sentence
print("Length of sentence    :", len(sentence))

print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)