from board import Board
from wordBank import WordBank

# TODO this is not generating all the words, it is missing some
# ex: RTIICAHWUOTNENRU
# RTII
# CAHW
# UOTN
# ENRU
# is missing thorn


class WordSearch():

    board = None
    wordBank = None
    # Keeps a dict of all solutions, keyed by length attached to a set of all words
    solutions = dict()


    def __init__(self, wordBankFile):
        self.wordBank = WordBank(wordBankFile)
        print("-------------------------------\nDictionary Loaded\n-------------------------------")


    def loadBoard(self, boardTxt):
        self.board = Board(boardTxt)
        print("-------------------------------Board Loaded-------------------------------")


    def runner(self):
        # Loops through all possible board positions
        for i in range(4):
            for j in range(4):
                self.search(self.board.board[i][j], (i, j), [(i, j)])

        self.displaySolutions()



    # Given a starting base position, recursively finds all words and adds them to solutions
    def search(self, currWord, currPos, usedPos):

        for adj in self.board.getAdjacent(currPos):
            nextWord = currWord + self.board.board[adj[0]][adj[1]]

            # Checks if test word is in bank, otherwise moves onto next position
            # Also checks that it is not a previously used position
            if adj in usedPos or not self.wordBank.isPrefix(nextWord):
                continue
            # Checks if test word is a complete word
            if self.wordBank.isCompleteWord(nextWord):
                self.addSolution(nextWord)

            
            # Contiues to search along this word path
            newUsed = usedPos.copy()
            newUsed.append(adj)
            self.search(nextWord, adj, newUsed)



    # Adds a given word to the solution dictionary
    def addSolution(self, word):
        if len(word) in self.solutions.keys():
            # Makes sure not to overwrite if a word is already included
            if word not in self.solutions[len(word)]:
                self.solutions[len(word)].append(word)
        else:
            self.solutions[len(word)] = [word]


    # Hopefully neatly displays the solutions by descending length
    def displaySolutions(self):
        for i in range(17):
            if i in self.solutions.keys():
                print(i, ": ", self.solutions[i])
                print("\n")





def main():

    # Pre-loads dictionary
    wordsearch = WordSearch("ScrabbleList.txt")
    
    boardText = input("Board Letters:\n").upper()
    #boardText = "RTIICAHWUOTNENRU"

    wordsearch.loadBoard(boardText)
    
    wordsearch.runner()




if __name__ == "__main__":
    main()