import time
import random

# Sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed tests are fun and useful.",
    "Practice makes a person perfect at typing.",
    "Consistency is the key to improvement."
]

# Random sentence
sentence = random.choice(sentences)
print("\n--- Typing Speed Test ---\n")
print("Type the following:\n")
print(sentence)
print("\nPress Enter when you're ready...")
input()

# Start time
start_time = time.time()

# User input
typed = input("Start typing:\n")

# End time
end_time = time.time()

# Time taken
time_taken = end_time - start_time
time_taken = round(time_taken, 2)

# Speed calculation
words = len(typed.split())
wpm = round((words / time_taken) * 60)

# Accuracy calculation
correct_chars = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct_chars += 1

accuracy = round((correct_chars / len(sentence)) * 100, 2)

# Results
print("\n--- Results ---")
print(f"Time Taken     : {time_taken} seconds")
print(f"Typing Speed   : {wpm} WPM")
print(f"Accuracy       : {accuracy}%")
