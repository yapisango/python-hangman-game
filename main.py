import random

words = ("apple", "banana", "pineapple", "orange", "coconut",)

hangman_art = {
    6: (
        "   O ",
        "  /|\\ ",
        "  / \\ "
    ),
    5: (
        "   O ",
        "  /|\\ ",
        "  / \\ "
    ),
    4: (
        "   O ",
        "  /|\\ ",
        "       "
    ),
    3: (
        "   O ",
        "  /| ",
        "      "
    ),
    2: (
        "   O ",
        "   | ",
        "       "
    ),
    1: (
        "   O  ",
        "      ",
        "      "
    ),
    0: (
        "      ",
        "   |  ",
        "      "
    )
}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess not in "abcdefghijklmnopqrstuvwxyz" or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)
        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
            if "_" not in hint:
                display_answer(answer)
                is_running = False
        else:
            wrong_guesses += 1
            if wrong_guesses == 6:
                display_man(wrong_guesses)
                display_answer(answer)
                is_running = False


if __name__ == "__main__":
    main()
