import random
from Words import word_list
from Art import logo, stages

# Random Words to be used
word_list = word_list
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6

# Print blanks for number of letters in chosen word
for _ in range(word_length):
    display += "_"
print(display)

# Dealing with user input
end_of_game = False
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You\'ve already tried {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    if guess not in chosen_word:
        print(f"{stages[lives]}\n {guess} is not in this word")
