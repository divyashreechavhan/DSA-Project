import random
import time
import json

def update_leaderboard(username, wpm, leaderboard_file):
    leaderboard = load_words_from_json(leaderboard_file)
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)
    leaderboard = leaderboard[:10]  # Keep only the top 10 scores
    save_leaderboard(leaderboard, leaderboard_file)

def show_leaderboard(leaderboard_file):
    leaderboard = load_words_from_json(leaderboard_file)
    print("Leaderboard:")
    for i, entry in enumerate(leaderboard):
        print(f"{i + 1}. {entry['username']} - {entry['wpm']} WPM")

def load_words_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data

def save_leaderboard(leaderboard, leaderboard_file):
    with open(leaderboard_file, 'w') as file:
        json.dump(leaderboard, file)

def get_user_input(prompt):
    return input(prompt)

def print_typing_feedback(expected, actual):
    if expected == actual:
        print("Correct!")
        return True
    else:
        print("Incorrect. Try again.")
        return False

def main():
    leaderboard_file = "leaderboard.json"
    words_file = "words.json"

    words_data = load_words_from_json(words_file)
    username = get_user_input("Enter your username: ")
    while True:
        

        option = get_user_input("Choose an option:\n1. Start Typing Test\n2. Show Leaderboard\n3. Exit\n")
        
        if option == "1":
            language = get_user_input("Choose a programming language (C, Python, Java, JavaScript, Ruby, C++, Go, C#, TypeScript, Rust): ")
            
            if language in words_data:
                words = words_data[language]
                num_words_to_practice = int(get_user_input("How many words to practice (1-25): "))
                num_words_to_practice = max(1, min(num_words_to_practice, 25))  # Ensure it's within the range 1-25
                selected_words = random.sample(words, num_words_to_practice)

                random.shuffle(selected_words)
                print("Words to type:")
                
                start_time = time.time()
                words_typed = 0
                correct_words = 0

                for word in selected_words:
                    print(f"Type: {word}")
                    user_input = get_user_input("Your input: ")
                    words_typed += 1
                    if print_typing_feedback(word, user_input):
                        correct_words += 1

                    
                    if user_input.lower() == '\x1b':  
                        print("Game exited. Goodbye!")
                        save_leaderboard(username, correct_words, leaderboard_file)
                        exit()

                end_time = time.time()
                time_taken = end_time - start_time
                wpm = int(correct_words / (time_taken / 60))

                print("\nTyping Metrics:")
                print(f"Words Typed: {words_typed}")
                print(f"Correct Words: {correct_words}")
                print(f"Time Taken: {time_taken:.2f} seconds")
                print(f"Words Per Minute (WPM): {wpm}")

                update_leaderboard(username, wpm, leaderboard_file)
            else:
                print("Invalid language. Please choose a valid programming language.")

        elif option == "2":
            show_leaderboard(leaderboard_file)

        elif option == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
