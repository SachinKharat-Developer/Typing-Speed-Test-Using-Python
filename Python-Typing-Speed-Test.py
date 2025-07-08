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
typed = input("Start typing:\n").strip()

# End time
end_time = time.time()

# Time taken
time_taken = round(end_time - start_time, 2)

# Handle empty input
if not typed:
    print("\n❗ You didn't type anything. Please try again.")
else:
    # Split words
    typed_words = typed.split()
    sentence_words = sentence.split()

    # Count correct words
    correct_words = sum(1 for tw, sw in zip(typed_words, sentence_words) if tw == sw)

    # Calculate accuracy
    accuracy = round((correct_words / len(sentence_words)) * 100, 2)

    # Calculate speed based on correct words only
    wpm = round((correct_words / time_taken) * 60) if time_taken > 0 else 0

    # Output results
    print("\n--- Results ---")
    print(f"Time Taken     : {time_taken} seconds")
    print(f"Typing Speed   : {wpm} WPM")
    print(f"Accuracy       : {accuracy}%")
