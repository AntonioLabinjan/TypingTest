import time
import random

def load_text(filename):
    with open(filename, "r") as file:
        return file.read()

def typing_test(text):
    print("Welcome to the Typing Test!")
    input("Press Enter to start...")
    
    print("\nType the following text:")
    print(text)
    
    input("\nPress Enter when you're ready to start typing...")
    
    start_time = time.time()
    user_input = input("\nStart typing here:\n")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = text.split()
    user_words = user_input.split()
    error_count = sum(1 for a, b in zip(words, user_words) if a != b)
    
    words_per_minute = len(user_words) / (elapsed_time / 60)
    
    print("\nTyping Test Results:")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Words Typed: {len(user_words)}")
    print(f"Words Per Minute: {words_per_minute:.2f}")
    print(f"Errors: {error_count}")

if __name__ == "__main__":
    text_file = "text.txt"  # Postavite ovdje ime datoteke s tekstom
    text_to_type = load_text(text_file)
    
    typing_test(text_to_type)
