class Board():
    board = [['', '', '', ''],
             ['', '', '', ''],
             ['', '', '', ''],
             ['', '', '', '']
             ]
    
    # Takes in a string of letters and fill the 2d array 
    def __init__(self, text):

        # Throw error if string is wrong length
        if len(text) != 16:
            raise ValueError
        
        letterPos = 0
        
        for i in range(4):
            for j in range(4):
                self.board[i][j] = text[letterPos]
                letterPos +=1


    # Prints the board to the screen
    def __str__(self):
        output = ""
        for i in range(4):
            for j in range(4):
                output += self.board[i][j] + " "
            output += "\n"

        return output
    
    # Takes in a tuple for char position and returns a set of all adjacent squares
    def getAdjacent(self, pos):
        adj = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Makes sure it is a valid position and not current the position
                if 0 <= pos[0] + i <= 3 and  0 <= pos[1] + j <= 3 and not (i == 0 and j == 0):
                    adj.add((pos[0] + i, pos[1] + j))
        
        return adj
        







def main():
    board = Board("ABCDEFGHIVLOSPIH")
    print(board)
    #print(board.getAdjacent((2, 2)))
    adj = board.getAdjacent((1, 1))

    output = ""

    used = [(0, 0)]

    for x in adj:
        if x in used:
            print(x, " is a used pos")
            continue
        print(x)

    # Tests adj func
    for i in range(4):
        for j in range(4):
            if (i, j) not in adj:
                output += board.board[i][j] + " "
            else:
                output += "# "
        output += "\n"

    print(output)
        


if __name__ == "__main__":
    main()