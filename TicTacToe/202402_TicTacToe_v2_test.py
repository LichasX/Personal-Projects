board_length = int(input("Enter the width of the board. "))
board_height = int(input("Enter the height of the board. "))
board_size = (board_length, board_height)
board = [" "] * board_size[0] * board_size[1]
end_condition = False  # if 0, draw, if 1, win by a player
game_key = [0]


def print_board():
    index_num = 0
    for y in range(board_size[1]):  # repeat row (y value)
        output = "| "
        for x in range(board_size[0]):  # print row (x value)
            output += board[index_num] + " | "
            index_num += 1
        print(output)


def turn_rotation(game_round):
    game_round += 1  # first round is round 1
    if game_round % 2 != 0:
        return [game_round, 1]
    else:
        return [game_round, 2]


def win_check():
    global end_condition, flag
    new_board = []
    if game_key[0] == board_size[0] * board_size[1]:  # all squares are filled
        end_condition = 2
    for z in range(board_size[1]):  # iterates through all row
        output2 = ""
        for i in range(board_size[0]):  # each row
            output2 += board[i+(z*board_size[0])]  # i is the number in specific row and the others is accounting for previous rows
        new_board.append(output2)  # new_board is an optimised version of board to check for win
    print(new_board)
    for y_value in range(-2*min((board_size[1]-3), 3), board_size[1]-2):  # used to run through each item in list new_board
        for x_value in range(-2*min((board_size[0]-3),3), board_size[0]-2):  # used to run through each item in each item in new_board, the convoluted thing is from trial and error that shifting the entire range by 2 is needed for board sizes 4 and up, but not 3 and below
            if new_board[y_value][x_value] != " " and new_board[y_value][x_value] == new_board[y_value+1][x_value] == new_board[y_value+2][x_value]:
                end_condition = 1
                if new_board[y_value][x_value] == "X":
                    flag = "X"
                else:
                   flag = "O"
            elif new_board[y_value][x_value] != " " and new_board[y_value][x_value] == new_board[y_value][x_value+1] == new_board[y_value][x_value+2]:
                end_condition = 1
                if new_board[y_value][x_value] == "X":
                    flag = "X"
                else:
                    flag = "O"
            elif new_board[y_value][x_value] != " " and new_board[y_value][x_value] == new_board[y_value+1][x_value+1] == new_board[y_value+2][x_value+2]: # diagonal top left to bottom right
                end_condition = 1
                if new_board[y_value][x_value] == "X":
                    flag = "X"
                else:
                    flag = "O"
            elif new_board[y_value][x_value] != " " and new_board[y_value][x_value] == new_board[y_value + 1][x_value - 1] == new_board[y_value + 2][x_value - 2]:
                end_condition = 1
                if new_board[y_value][x_value] == "X":
                    flag = "X"
                else:
                    flag = "O"


while not end_condition:
    print_board()
    game_key = turn_rotation(game_key[0])
    while True:
        move_coord = str(input(f"Round:{game_key[0]}\nPlayer {game_key[1]}, enter your move in the form of coordinates xy where x is the column and y is the row your move is at. "))
        move_board = (int(move_coord[1])-1) * board_size[0] + (int(move_coord[0])-1) # converts coordinate form of move to index form to be used in board list
        if board[move_board] == " ":
            break
        else:
            print("Error. Enter valid move.")
    if game_key[1] == 1:
        board[move_board] = "X"
    else:
        board[move_board] = "O"
    win_check()

print_board()
if end_condition == 2:
    print("Draw")
elif end_condition == 1:
    if flag == "X":
        print("Player 1 has won.")
    elif flag == "O":
        print("Player 2 has won.")
