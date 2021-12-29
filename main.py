# Wheel of Fortune Game Assessment - Korby
import random
import json
import time


# Quick reference to time.sleep(x) with x as # of seconds. Base func call is set to 1 second sleep
def wait(sec=1.0):
    time.sleep(sec)


# Welcome message to game
def welcome():
    print("Welcome to the Wheel of Fortune!")
    time.sleep(1)
    print("Let's welcome our guests...")
    time.sleep(1)
    for char in players:
        print(f"{players[char]['name']}")
        time.sleep(1)
    print("\nLets get started!\n")
    time.sleep(1)


# Gets random category from read file and picks random word from within that category
def get_word(file):
    # get categories with: file.keys())
    # get words/phrases from category with: file["category"] ex. file["Title"]
    rand_category = random.choice(list(file.keys()))
    rand_phrase = random.choice(list(file[rand_category]))
    return rand_category.upper(), rand_phrase.upper()


# Function creates padded text output used to display our game board(puzzle), easily distinguished from statements
def fill_word():
    puzzle = ""
    for character in phrase:
        if character not in letters:
            puzzle += character
        elif character in guesses:
            puzzle += character
        else:
            puzzle += '_'
    padded_puzzle = "=" * len(puzzle) + "\n" + puzzle + "\n" + "=" * len(puzzle)
    return padded_puzzle


# Asks user for a numerical input and cycles until user conditions are met
def get_number_input(lower_bound=1, upper_bound=3):
    while True:
        number_input = input("Choice: ")
        if number_input.isnumeric():
            if int(number_input) in range(lower_bound, upper_bound + 1):
                break
            else:
                print(f"Input was out of bounds {lower_bound} - {upper_bound}. Please retry")
        else:
            print("Input was not an integer, please input an integer.")

    return int(number_input)


# Asks user for a consonant input, loops if not a letter or not 1 letter
def get_consonant_input():
    while True:
        consonant_input = input("Choose a consonant: ").strip().upper()

        if len(consonant_input) == 1 and consonant_input in letters:
            break
        else:
            print("Bad input, try again.")
    return consonant_input


# Asks user for a vowel input, loops if not a letter or not 1 letter
def get_vowel_input():
    while True:
        vowel_input = input("Choose a vowel: ").strip().upper()

        if len(vowel_input) == 1 and vowel_input in letters:
            break
        else:
            print("Bad input, try again.")
    return vowel_input


# Returns true or false based on the provided guess and type, prints statement for any failed guesses
def check_guess(guess, letter_type):
    if guess in guesses:
        print("That letter was already called.")
        return False
    else:
        if guess in vowels and letter_type == "consonant":
            print("That's not a consonant...")
            return False
        elif guess in consonants and letter_type == "vowel":
            print("That's not a vowel...")
            return False
        else:
            guesses.append(guess)
            if guess in phrase:
                return True
            else:
                print(f"There are no {guess}'s.")
                return False


# Returns a random value from wheel
def spin_wheel():
    return random.choice(wheel)


# Handles the spin wheel portion of a players turn. returns false if a bad spin or guess, true if good spin and guess
def player_spin():
    print("---Wheel Spin---")
    spin = spin_wheel()
    wait(0.5)
    if spin == "Lose Turn":
        print("You spun: 'Lose Turn'")
        wait()
        return False
    elif spin == "Bankrupt":
        print("You spun: 'Bankrupt'")
        players[active_player]['bank'] = 0
        wait()
        return False
    else:
        print(f"You spun: ${spin}")
        wait()
        print(fill_word())

        check = check_guess(get_consonant_input(), "consonant")
        if check is False:
            wait()
            return False
        else:
            print(f"That's in the puzzle! You gained ${spin}\n")
            players[active_player]['bank'] += spin
            wait()
            return True


# Buy vowel part of players turn. Removes vowel cost from active players bank and checks if it is in the puzzle
def player_vowel():
    players[active_player]['bank'] -= vowel_cost
    check = check_guess(get_vowel_input(), "vowel")
    if check is False:
        wait()
        return False
    else:
        print(f"That's in the puzzle!\n")
        wait()
        return True


# Called after a player gets the first spin guess right. Allows user to choose which action to take. Returns a continue
# bool as True if the player got the action correct and a win bool as True if player solved the puzzle correctly
def player_choice():
    return_val = False
    win_bool = False
    while True:
        print(fill_word())
        print(f"{players[active_player]['name']}, you have ${players[active_player]['bank']} in the bank.")
        print(f"Choose what you would like to do:\n1. Spin Wheel\n2. Buy a Vowel for ${vowel_cost}\n3. Solve Puzzle")
        user_choice = get_number_input()
        print("")

        if user_choice == 1:
            if player_spin() is False:
                break
        elif user_choice == 2:
            if players[active_player]['bank'] < vowel_cost:
                print("You don't have enough to buy a vowel. Spin the wheel or solve the puzzle.")
                wait()
            else:
                if player_vowel() is False:
                    break
        elif user_choice == 3:
            print(fill_word())
            if solve_puzzle() is True:
                win_bool = True
                break
            else:
                return_val = False
                break

    return return_val, win_bool


# Get user input to solve for the puzzle(Rounds 1 and 2). Returns true if they got it correct, otherwise false
def solve_puzzle():
    user_solve = input("Solve: ").strip().upper()
    if user_solve == phrase:
        print("Correct!")
        return True
    else:
        print("That was an incorrect guess.")
        return False


# Gets the index of the player with the largest bank value
def get_final_player_index():
    # stackoverflow
    top_bank_dict = max(list(players.values()), key=lambda x: x['bank'])
    keys = list(players.keys())

    return keys[list(players.values()).index(top_bank_dict)]


# Program starts here
if __name__ == '__main__':
    # Letters used for checking user inputs and cost for vowels
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'AEIOU'
    vowel_cost = 250

    # Wheel values increment by 50, 3 segments per value, million dollar space has two extra bankrupt spaces included
    wheel = [100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350, 350, 350, 400, 400, 400,
             450, 450, 450, 500, 500, 500, 550, 550, 550, 600, 600, 600, 650, 650, 650, 700, 700, 700, 750, 750, 750,
             800, 800, 800, 850, 850, 850, 900, 900, 900, "Lose Turn", "Lose Turn", "Lose Turn", "Bankrupt", "Bankrupt",
             "Bankrupt", "Bankrupt", 1000000, "Bankrupt"]
    active_wheel_value = 0

    # set up characters to be referenced/played as in the game
    # players[outer-key][inner-key] -> outer-key = active_player && inner-key = key_name
    players = {1: {"name": "Bob E. Flay",
                   "bank": 0},
               2: {"name": "Sue E. Chop",
                   "bank": 0},
               3: {"name": "Tone E. Stark",
                   "bank": 0}}
    active_player = 1

    # set up word list for puzzles
    with open("data/phrases.json") as f:
        data = json.load(f)

    # Welcome message
    welcome()

    # Game handler - Go through each round, cycling through players until the puzzle is solved
    for Round in [1, 2, 3]:
        win = False
        guesses = []
        (category, phrase) = get_word(data)
        if Round in [1, 2]:
            print(f"Round: {Round}")
            wait()
            print(f"Category: {category}")
            wait()

            while win is False:  # Run players turns so long as the puzzle isn't solved
                # Player Turn
                print(f"\n{players[active_player]['name']}, you're up!")
                print(f"You have ${players[active_player]['bank']} in the bank.\n")
                wait()

                # If player gets the first spin and guesses correctly, they move on to choosing what action to take
                if player_spin() is True:
                    while True:
                        (ret, win) = player_choice()
                        if win is True or ret is False:
                            break

                if win is False:
                    if active_player == 3:
                        active_player = 1
                    else:
                        active_player += 1

            guesses.clear()
        else:
            active_player = get_final_player_index()
            answer_guesses = []
            letters = 'RSTLNE'

            print("Time to move on to our final round.")
            wait()
            print(f"The contestant that will be proceeding is: {players[active_player]['name']}")
            wait()
            print(f"The category for this round is: {category}")
            wait()
            print(f"You start with the letters: {letters}")
            wait()
            print(fill_word())
            wait()
            print("Choose 3 consonants and a vowel")
            for letter in [1, 2, 3, 4]:
                time.sleep(0.5)
                if letter in [1, 2, 3]:
                    while True:
                        user_input = get_consonant_input()
                        if user_input not in guesses:
                            break
                        else:
                            print("That has already been called. Try another letter.")
                else:
                    while True:
                        user_input = get_vowel_input()
                        if user_input not in guesses:
                            break
                        else:
                            print("That has already been called. Try another letter.")

            print("You will have 15 seconds to answer the puzzle. Good luck!")
            print(fill_word())
            wait(0.25)
            start = time.time()
            while (time.time() - start) < 15:
                user_input = input("Solve: ").strip().upper()
                if user_input == phrase:
                    print("Correct!")
                    win = True
                    break
            if win is False:
                print("Sorry, you didn't solve the puzzle in time.")

        if win is True:
            print(f"{players[active_player]['name']} won the round!\n")
        wait()

    # Final send off
    print(f"Congratulations {players[active_player]['name']}, you've won ${players[active_player]['bank']}")
    wait()
    print("Thank you for playing my game. Buh-bye!")
    wait(5)
