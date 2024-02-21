# board_length = int(input("Enter the width of the board. "))
# board_height = int(input("Enter the height of the board. "))
# board_size = (board_length, board_height)
board_size = (3, 5)
board = [" "] * board_size[0] * board_size[1]
end_condition = False  # if True, end game
game_key = [0]
win_condition_in_a_row = 3 #change if want to change game
flag = 0


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
    global flag
    new_board = []
    if game_key[0] == board_size[0] * board_size[1]: # all squares are filled
        end_condition = 0
    for z in range(board_size[1]): # iterates through all row
        output2 = ""
        for i in range(board_size[0]): # each row
            output2 += board[i+(z*board_size[0])] # i is the number in specific row and the others is accounting for previous rows
        new_board.append(output2)
    print(new_board)
    for a in range(board_size[1]):
        for b in range(board_size[0]):
            if new_board[a][b] != " ":
                try:
                    if new_board[a][b] == new_board[a+(win_condition_in_a_row-1)][b]: # b stays constant, checking for vertical win
                        for p in range(1, win_condition_in_a_row): #since last line checked that there is possibility of 3 in a row, this checks if true
                            if new_board[a][b] != new_board[a + p][b]:
                                flag = -1
                        if flag != -1:
                            end_condition = 1
                            flag = new_board[a][b]
                except:
                    pass
                if flag == 0:
                    try:
                        pass #placeholder
                    except:
                        pass



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

if end_condition == 0:
    print("Draw")
elif end_condition == 1:
    if flag == "X":
        print("Player 1 has won.")
    else:
        print("Player 2 has won.")