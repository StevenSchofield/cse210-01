# Nested array to keep track of the current board state
game_board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

# Simplify the translation process so I can use numbers in code and letters in display
piece_translation = [" ", "X", "O"]
index_translation = ["A", "B", "C"]

# Display the current board state, including indexes
def print_board(boardArray):
    print("\n |1|2|3")
    for rowIndex in range(0,3):
        print_line = str(index_translation[rowIndex])
        print("--------")

        for index in boardArray[rowIndex]:
            print_line += "|"
            print_line += piece_translation[index]
        
        print(print_line)
    print("\n")

# Handle and verify player input
def player_input(playerNumber, boardArray):
    positionIndex = []
    positionString = input("Player " + str(playerNumber) + ", please input which position you would like to mark: ")

    # A position index should only have 2 characters: letter for the row, number for the colum
    if len(positionString) != 2:
        print("\nSorry, that input is the wrong size. Please input a position in the format of \"A1\" or \"B3\".")
        return player_input(playerNumber, boardArray)

    positionIndex.append(positionString[0])
    positionIndex.append(positionString[1])

    # The first character (letter) represents the row, and should be translated to a number
    if type(positionIndex[0]) == type(""):
        for i in range(0, 3):
            if index_translation[i] == positionIndex[0].capitalize():
                positionIndex[0] = i
                break
            
            if i == 2:
                print("\nSorry, the first character needs to be one of the letters \"A\", \"B\", or \"C\". " +\
                    "Please try again.")
                return player_input(playerNumber, boardArray)
    else:
        print("\nSorry, the first character needs to be one of the letters \"A\", \"B\", or \"C\". " +\
            "Please try again.")
        return player_input(playerNumber, boardArray)

    # The second character needs to be a number less than 3 (note that the input will be 1 larger than the actual index)
    if positionIndex[1].isdigit() and int(positionIndex[1]) <= 3 and int(positionIndex[1]) != 0:
        positionIndex[1] = int(positionIndex[1]) - 1
    else:
        print("\nSorry, the second character needs to be a number between 1 and 3. " +\
            "Please try again.")
        return player_input(playerNumber, boardArray)  

    # Ensure the selected tile has not been taken already
    if boardArray[positionIndex[0]][positionIndex[1]] != 0:
        print("\nSorry, that position has already been claimed. Please try again.")
        return player_input(playerNumber, boardArray)
    
    return positionIndex

# Run through every cell and check if it is in a line of 3 of itself. Return the winner, or zero
def checkWinCondition(boardArray):
    y = 0
    max = len(boardArray)

    # Loop through every position and check if it is 
    while y < max:
        x = 0

        while x < max:
            # If unmarked, no need to check for completion on this cell
            if boardArray[y][x] != 0:
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
        y += 1
    
    return 0


def main():
    player = 1

    runs = 1

    # Welcome message!
    print("Thank you for playing Tic-Tak-Toe today! Remember: first to get 3 in a row wins! X is always player 1.\n\n")

    while checkWinCondition(game_board) == 0 and runs <= 9:
        print_board(game_board)
        input = player_input(player, game_board)

        game_board[input[0]][input[1]] = player

        if player == 1:
            player = 2
        else:
            player = 1
        
        runs += 1
    
    print_board(game_board)
    results = checkWinCondition(game_board)
    if results == 0:
        print("\nIt's a draw!\n")
    else:
        print("Player " + str(results) + " wins!")

    print("Thank you for playing!")
main()