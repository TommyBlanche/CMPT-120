import random

selected_category = ""


def main():
    global selected_category

    categories = {
        "college": ["Marist", "Fontaine", "Hancock", "Champagnat", "Fulton"],
        "animals": ["Hippopotamus", "Orangutan", "Elephant", "Penguin", "Leopard"],
        "majors": ["Mathematics", "Physics", "Chemistry", "Communications", "History"]
    }

    selected_category = random.choice(list(categories.keys()))
    word = random.choice(categories[selected_category]).upper()
    print(f"Guess the {selected_category} related word!")

    guessed_letters = set()
    turns = int(input("How many guesses would you like?: "))

    # Game loop
    while turns > 0:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print("\nWord:", display_word)
        print("Turns left:", turns)

        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
        else:
            guessed_letters.add(guess)
            if guess not in word:
                turns -= 1
                print("Incorrect guess!")


        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if turns == 0:
        print("Out of turns! The word was:", word)


def game():
  main()


if __name__ == "__main__":
    game()

