# Korby_WoF_Assessment
## Description
In this project, I recreated the popular game 'Wheel of Fortune' using Python to test my coding knowledge and abilities learnt through our stage3talent course. 

This project encompasses several key elements of coding in general, those are:
- Variables
- String Manipulation
- Flow Control
- Collections (list, types, sets, and dictionaries)
- Functions
- File I/O

## Gameplay
There are 3 pre-set characters who you will play as: Bob E Flay, Sue E Chop, and Tone E Stark. 

Each turn consists of a initial spin and letter guess, choice of: spin, buy a vowel or solve the puzzle. Once a puzzle is solved, the round ends and continues to the next round. After the third round, the game ends.

### Wheel Wedges
The wheel contains wedges of various types, with each wedge have 3 slots in which the players spin can land in.

There are wedges with cash values starting from $100, incrementing by $50, up to $900. 

There are also three types of special wedges: 
- Lose a Turn: Player loses nothing but is not allowed any action until their next turn. Play continues with the next player.
- Bankrupt: Players bank is set to $0 and player is not allowed any action until their next turn. Play continues with the next player.
- Million Dollar Wedge: A wedge with two Bankrupt slots and one $1,000,000 slot. If a player lands on the million dollar slot, they may guess a consonant and that cash is added directly to their bank. *This value is included in the overall bank total when deciding the player who procedes to the final round.

### Turn Start
To start a players turn, the wheel is automatically spun and a statement is printed based on what wedge of the wheel you landed on. If the spin is a cash value, $X, they are able to guess a consonant to gain X money in their bank. If they guess a consonant correctly, that cash value is added to their bank and are able to choose one of three options. If the spin is other than a cash value, the associated event takes effect and play continues with the next player. 

### Turn Continued
The player can chose between the following:
- Spin The Wheel
- Buy A Vowel
- Solve Puzzle

#### Spin The Wheel 
Same rules as 'Turn Start'

#### Buy A Vowel
If a player choses to buy a vowel, they must have $250 in their bank. If they do, $250 is deducted from their bank and the player is allowed to guess a vowel. If the vowel is a part of the puzzle, the players turn continues at 'Turn Continued'

#### Solve Puzzle
If a player choses to solve the puzzle, they are allowed to guess the puzzle. They must enter the **exact** spelling of the puzzle, including symbols and spaces. If correct, the puzzle is solved and the round ends.

## Install and Run
Download main.py and the data folder containing the phrases.json file. Once installed and the python file and folder are in the same directory, you can run the python file in command line using 'py main.py'

## Disclaimer
This game was created as an educational tool, not purposed for sale and free to use by the public. 

## Resources
[WoF Phrases](https://gist.github.com/michaelmotzkus/de82e06c8538399909103108049788b9)
