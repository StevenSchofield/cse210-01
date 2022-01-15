# Nested array to keep track of the current board state
from operator import truediv


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

# Function to handle and verify player input
def player_input(playerNumber, boardArray):
    positionIndex = []
    positionString = input("Player " + str(playerNumber) + ", please input which position you would like to mark: ")

    # A position index should only have 2 characters: letter for the row, number for the colum
    if len(positionString) != 2:
        print("\nSorry, that input is the wrong size. Please input a position in the format of \"A1\" or \"B3\".")
        return player_input(playerNumber)

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

def checkWinCondition(boardArray, runs):
    if runs == 9:
        return False
    else:
        return True


def main():
    player = 1

    runs = 1

    # Welcome message!
    print("Thank you for playing Tic-Tak-Toe today! Remember: first to get 3 in a row wins!\n\n")

    while checkWinCondition(game_board, runs):
        runs += 1
        print_board(game_board)
        input = player_input(player, game_board)

        game_board[input[0]][input[1]] = player

        if player == 1:
            player = 2
        else:
            player = 1
    
    print("Thank you for playing!")

main()