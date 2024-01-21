# Dictionary has '\n' between at the end of words

# Uses dictionaries to make trie of words
# If a word has ended, includes _end_ : True
# Key value pair
class WordBank():

    wordBank = dict()


    # Loads given file into dict structure
    def __init__(self, filename):

        currDict = self.wordBank

        # Ignores all words <2 or >16 characters 
        with open(filename) as file:
            for line in file:

                # Skips the line if the word doesn't meet length requirements
                if len(line)-1 < 3 or len(line) > 16:
                    continue

                for char in line:
                    # Makes sure current char isn't a linebreak
                    if str.isalpha(char):
                        
                        # Gets value of specified key, if it doesn't exist adds it
                        currDict = currDict.setdefault(char, dict())

                    # If current char is a linebreak adds end tag
                    else:
                        currDict.setdefault("_end_", True)                 

                # Returns to root dictionary between words
                currDict = self.wordBank
                    
    
    def __str__(self):
        return str(self.wordBank)
    

    # Checks if current word is building up towards another word
    def isPrefix(self, word):
        currDict = self.wordBank

        for char in word:
            if char not in currDict.keys():
                return False
            
            currDict = currDict[char]
        
        return True

    # Checks if given word is valid
    def isCompleteWord(self, word):
        currDict = self.wordBank

        for char in word:
            currDict = currDict[char]

        if "_end_" in currDict.keys():
            return True
        
        return False



def main():
    #dict = WordBank("testDict.txt")
    dict = WordBank("ScrabbleList.txt")
    #print(dict)
    print(dict.isCompleteWord("THORN"))


if __name__ == "__main__":
    main()