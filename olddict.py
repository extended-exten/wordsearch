# Dictionary has '\n' between at the end of words
class Dictionary():

    wordBank = list()


    def __init__(self, filename):

        currList = self.wordBank

        # Ignores all words <2 or >16 characters 
        with open(filename) as file:
            for line in file:

                # Skips the line if the word doesn't meet length requirements
                if len(line)-1 < 3 or len(line) > 16:
                    continue

                for char in line:
                    # Makes sure current char isn't a linebreak
                    if str.isalpha(char):

                        if currList[self.convertInt(char)] is not None:


                            print(char + ": ", self.convertInt(char), str.isalpha(char))

                currList = self.wordBank
                    


    # Converts a char to its alphabetic respective value 1-26
    def convertInt(self, char):
        return ord(char)-65



def main():
    dict = Dictionary("testDict.txt")


if __name__ == "__main__":
    main()