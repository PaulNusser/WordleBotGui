import random
class gameState:

    def __init__(self) -> None:
        self.guesses = []
        self.secretWord = ""
        self.wordFound = False
        self.attempts = 1
        self.userGuess = ""
        self.validGuesses = []
        self.validSolutions = []
        self.invalidChars = []
        self.fillWordLists()
        self.setHiddenWord()

    
    def updateGuesses(self, guess, numList):
        self.guesses.append(list(zip(guess, numList)))
    

    def checkWord(self, guess):
        numList = [0] * 5  # Initialize all to '0' (grey)
        used_indices = set()  # To track indices already matched exactly or as partial matches

        # First pass: check for exact matches
        for i in range(5):
            if guess[i] == self.secretWord[i]:
                numList[i] = 2
                used_indices.add(i)  # Mark this index as used

        # Second pass: check for partial matches
        for i in range(5):
            if numList[i] == 0:  # Only consider this if it's not an exact match
                for j in range(5):
                    if guess[i] == self.secretWord[j] and j not in used_indices:
                        numList[i] = 1  # Correct letter, wrong place
                        used_indices.add(j)  # Mark this index as used
                        break  # Break after the first unused match

        return numList

    
def fillWordLists(self):
    with open('valid_guesses.txt', 'r') as validGuessesFile:
    # Read lines into a list and strip newline characters
        self.validGuesses = [line.strip() for line in validGuessesFile.readlines()]
    with open('valid_solutions.txt', 'r') as validSolutionsFile:
        self.validSolutions = [line.strip() for line in validSolutionsFile.readlines()]

def setHiddenWord(self):
    random_index = random.randint(a=0, b=(len(gameState.validSolutions) - 1))
    self.secretWord = gameState.validSolutions[random_index]
