import random
import time

# List of words for the typing test
word_list = ["python", "programming", "example", "practice", "keyboard", "challenge", "developer", "speed", "accuracy"]

def typing_speed_test():
    input("Press Enter to start the typing test...")
    start_time = time.time()
    words_typed = 0

    while True:
        word = random.choice(word_list)
        print(f"Type the word: {word}")
        user_input = input()
        if user_input == word:
            words_typed += 1
        else:
            print("Incorrect! Try again.")

        if time.time() - start_time >= 60:  # Adjust the time limit (in seconds) as needed
            break

    end_time = time.time()
    elapsed_time = end_time - start_time
    words_per_minute = (words_typed / elapsed_time) * 60

    print(f"Words typed: {words_typed}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {words_per_minute:.2f} words per minute")

if __name__ == "__main__":
    typing_speed_test()


