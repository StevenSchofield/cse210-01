# Code created by Steven Schofield. Last updated 1/15/2022
# Made for CSE210-01 Solo Code Submission

# Nested array to keep track of the current board state (setup later)
game_board = []

# Simplify the translation process so I can use numbers in code and letters in display
piece_translation = [" ", "X", "O"]
index_translation = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# Create a board with variable sizes
def setup_board(boardSize:int):
    placeholder = []
    for index in range(0, boardSize):
        placeholder2 = []
        for index2 in range(0, boardSize):
            placeholder2.append(0)
        placeholder.append(placeholder2)
    return placeholder

# Display the current board state, including indexes
def print_board(boardArray):
    # Since it is no longer always set in stone, prepare the various lines for printing
    initialLine = "\n "
    midLine = "-"
    for index in range(len(boardArray)):
        initialLine += "|" + str(index+1)
        midLine += "--"

    print(initialLine)
    for rowIndex in range(0,len(boardArray)):
        print_line = str(index_translation[rowIndex])
        print(midLine)

        for index in boardArray[rowIndex]:
            print_line += "|"
            print_line += piece_translation[index]
        
        print(print_line)
    print("\n")

# Handle play options before the game begins
def setup_play():
    command = input("\nWhat is your command: ")

    if len(command) != 1 or command.isnumeric(): 
        print("Please only use a single letter for commands.")
        setup_play()
    
    command = command.capitalize()

    match command:
        case "R":
            print("\nThe game is played on a grid that is generally three squares by three squares. Example:")
            print_board(setup_board(3))
            print("Player one uses x's. Player two uses o's.")
            print("Players take turns putting their marks in empty squares.")
            print("The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.")
            print("If all nine squares are full and neither player has three in a row, the game ends in a draw.\n")
            print("\nWhile playing, mark a position by putting in the corrdinates displayed on the top and side of the board. " \
                + "Use letter/row followed by number/column. Example: B3")
            return setup_play()
        case "H":
            helpMenu()
            return setup_play()
        case "X":
            customSize = input("Please input the size of board you would like to play on: ")
            if customSize.isdigit():
                customSize = int(customSize)
                if customSize < 3:
                    print("Sorry, that board size is too small. Setting up a 3x3 board instead...")
                    return setup_board(3)
                elif customSize > 9:
                    print("Sorry, that board size is too big. Setting up a 9x9 board instead...")
                    return setup_board(9)
                else:
                    return setup_board(customSize)
            else:
                print("That is not a recognized size. Setting up a default board size...")  
                return setup_board(3)
        case "P":
            return setup_board(3)
        case "Q":
            print("\n\nThank you for playing!\n")
            quit()
        case _:
            print("Unrecognized command, please try again.")
            return setup_play()

# Handle and verify player input
def player_input(playerNumber, boardArray):
    positionIndex = []
    positionString = input("Player " + str(playerNumber) + ", please input which position you would like to mark: ")

    # Adding a quit option because I wanted to
    if positionString == "Q" or positionString == "q":
        print("\n\nSorry to see you leave. Thank you for playing!")
        quit()

    # A position index should only have 2 characters: letter for the row, number for the colum
    if len(positionString) != 2:
        print("\nSorry, that input is the wrong size. Please input a position in the format of \"A1\" or \"B3\".")
        return player_input(playerNumber, boardArray)

    positionIndex.append(positionString[0])
    positionIndex.append(positionString[1])

    # The first character (letter) represents the row, and should be translated to a number
    if type(positionIndex[0]) == type(""):
        for i in range(0, len(boardArray)):
            if index_translation[i] == positionIndex[0].capitalize():
                positionIndex[0] = i
                break
            
            if i == len(boardArray)-1:
                print("\nSorry, the first character represents a position that is out of range. " +\
                    "Please try again.")
                return player_input(playerNumber, boardArray)
    else:
        print("\nSorry, the first character represents a position that is out of range. " +\
            "Please try again.")
        return player_input(playerNumber, boardArray)

    # The second character needs to be a number less than the size of the board (subtract 1 because 0-indexing)
    if positionIndex[1].isdigit() and int(positionIndex[1]) <= len(boardArray) and int(positionIndex[1]) != 0:
        positionIndex[1] = int(positionIndex[1]) - 1
    else:
        print("\nSorry, the second character represents a position that is out of range. " +\
            "Please try again.")
        return player_input(playerNumber, boardArray)  

    # Ensure the selected tile has not been taken already
    if boardArray[positionIndex[0]][positionIndex[1]] != 0:
        print("\nSorry, that position has already been claimed. Please try again.")
        return player_input(playerNumber, boardArray)
    
    return positionIndex

# Run through every cell and check if it is in a line of 3 of itself. Return the winner, or zero
def checkWinCondition(boardArray):
    totalCount = 0
    filledCount = 0

    y = 0
    max = len(boardArray)

    # Loop through every position and check if it is 
    while y < max:
        x = 0

        while x < max:
            # If unmarked, no need to check for completion on this cell
            if boardArray[y][x] != 0:
                filledCount += 1
                # Horizontal check (skip if on edge)
                if x != 0 and x != max-1:
                    if boardArray[y][x-1] == boardArray[y][x] and boardArray[y][x] == boardArray[y][x+1]:
                        return boardArray[y][x]
                # Vertical check (skip if on edge)
                if y != 0 and y != max-1:
                    if boardArray[y-1][x] == boardArray[y][x] and boardArray[y][x] == boardArray[y+1][x]:
                        return boardArray[y][x]
                # Diagonal checks (I could have put them in one of the previous checks, but I think this looks nicer)
                if y != 0 and y != max-1 and x != 0 and x != max-1:
                    if boardArray[y-1][x-1] == boardArray[y][x] and boardArray[y][x] == boardArray[y+1][x+1]:
                        return boardArray[y][x]
                    elif boardArray[y+1][x-1] == boardArray[y][x] and boardArray[y][x] == boardArray[y-1][x+1]:
                        return boardArray[y][x]
            x += 1
            totalCount += 1
        y += 1
    
    if filledCount == totalCount:
        return -1
    else:
        return 0

# Help menu for pre-play
def helpMenu():
    print("\nPossible commands: ")
    print("R - Rules. Official rules and available commands for this version")
    print("H - Help. Repeats this list. Not available during play")
    print("X - Custom game. Create a board of any size from 3-9")
    print("P - Quick play. Start a standard game on a 3x3 board")
    print("Q - Quit. Exits program.")

def gameLoop():
    player = 1

    # Give the player some initial options before playing
    helpMenu()
    game_board = setup_play()

    while checkWinCondition(game_board) == 0:
        print_board(game_board)
        command = player_input(player, game_board)

        game_board[command[0]][command[1]] = player

        if player == 1:
            player = 2
        else:
            player = 1
    
    print_board(game_board)
    results = checkWinCondition(game_board)
    if results == 0:
        print("\nIt's a draw!")
    else:
        print("Player " + str(results) + " wins!")
    
    # There is always a chance for a re-match
    command = input("\n\nPlay again? (Y/N)").capitalize()
    if command == "Y":
        gameLoop()
    else:
        return

def main():
    # Welcome message!
    print("Welcome to Tic-Tac-Toe!\n")
    
    # Run the game (seperate function so now I can use recursion)
    gameLoop()

    # Let them leave on a positive note!
    print("Thank you for playing!\n")

main()