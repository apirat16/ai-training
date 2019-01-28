# Hangman Game

## Build and Run
```bash
$ python main.py
```

## Practice
The Hangman Game source code does not completed yet. Since the guested characters
are including the correct characters, please modify the class to show only incorrect
characters. Also when the player guess with incorrect character, the system must 
penalize the player by hanging him like the picture below and then the game is over. 
```bash
   +--------+
   |        |
   |        O
   |       /|\
   |        |
   |       / \
   | 
=======
```

Nevertheless, current system accept only input by character not the word. 
Please modify the game to be able to process the word. For example if the player
input "joke" the game will take "j", "o", "k", "e" as the input. 
