import random

words = ['ruby','java','swift','python','javascript','c']

chosen_word = random.choice(words)

blanks = ["_" for _ in chosen_word]



attempts = 8

while attempts > 0 and '_' in blanks:
    print(" ".join(blanks))
    guess= input("Enter the guess letter: ").lower()
    if guess in chosen_word:
        print("You found a letter. hoorayy!")
        for index,letter in enumerate(chosen_word):
            if guess ==  letter:
                blanks[index] = guess
    else:
        attempts -=1
        print("You lost the attempt try again!")

if "".join(blanks) == chosen_word:
    print("".join(blanks))
    print("You win")
else:
    print("You lose")

