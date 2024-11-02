def new_board():
    board = [[None, None, None], [None, None, None], [None, None, None]]
    return board

board = new_board()

def render(board):
    rows = []
    for y in range(0,3):
        row = []
        for x in range(0, 3):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    print ('  0 1 2 ')
    print ('  ------')
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print ("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print ('  ------')

board[0][0] = 'X'
board[0][1] = 'X'
board[0][2] = 'X'
board[1][0] = 'O'
board[1][1] = 'O'
board[1][2] = 'O'
render(board)


#need a forever game loop until the game is over

# loop forever:

#     current_player =  "something"

#     #need to print the board state
#     render(board)

#     #need to get the current players move coordinates
#     move_coords = get_move()

#     #make the move above on the board
#     make_move(board, move_coords, current_player)

#     #figure out if there is a winner
#     winner = get_winner(board)

#     #if there is a winner, congrats and end loop
#     if winner is not None:
#         print ("Winner is %s!", %s winner)
#         break

#     #no winner and board is full = draw
#     if is_board_full(board):
#         print("Draw")
#         break

#     #repeat until game is over
