import time

def typing_speed_test():
    print("Welcome to the Typing Speed Tester!")
    print("You will have 30 seconds to type the text shown below.")
    
    text = "Python is a powerful programming language used for web development, data science, automation, and more."
    print("\nYour text to type:")
    print(text)
    
    input("\nPress Enter when you are ready to start...")

    print("\nStart typing now! (Timer: 30 seconds)")
    start_time = time.time()
    typed_text = ""

    # Keep taking input until time is up
    while time.time() - start_time < 30:
        try:
            line = input()
            typed_text += " " + line
        except EOFError:
            break

    elapsed_time = time.time() - start_time
    word_count = len(typed_text.strip().split())

    print("\nTime's up!")
    print(f"You typed {word_count} words in {elapsed_time:.2f} seconds.")
    wpm = word_count * (60 / elapsed_time)
    print(f"Your typing speed: {wpm:.2f} words per minute (WPM).")

if __name__ == "__main__":
    typing_speed_test()
