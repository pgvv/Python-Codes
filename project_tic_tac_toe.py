board = [" "
         for i in range(9)]

def print_board():
    row1 = "|{}| |{}| |{}|".format(board[0], board[1], board[2])
    row2 = "|{}| |{}| |{}|".format(board[3], board[4], board[5])
    row3 = "|{}| |{}| |{}|".format(board[6], board[7], board[8])

    print()     #prints blank line
    print(row1)
    print(row2)
    print(row3)
    print()     # prints blank line

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number =2

    print("Your turn player {}".format(number))

    while True:
        choice = int(input("Enter your move(1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            break
        else:
            print()
            print("Invalid move!")
            print("Your turn player {}".format(number))

def victory(icon):
    if(board[0] == board[1] == board[2] == icon) or \
      (board[3] == board[4] == board[5] == icon) or \
      (board[6] == board[7] == board[8] == icon) or \
      (board[0] == board[3] == board[6] == icon) or \
      (board[1] == board[4] == board[7] == icon) or \
      (board[1] == board[4] == board[7] == icon) or \
      (board[0] == board[4] == board[8] == icon) or \
      (board[2] == board[4] == board[6] == icon):    
          return True
    else:
        return False

def draw():
    if " " not in board:
        return True
    else:
        return False
  
                
while True:
    print_board()
    player_move("X")
    print_board()
    
    if victory("X"):
        print("Congratulations Player 1, You Win!")
        break
    elif draw():
        print("It is a draw!")
        break
    
    player_move("O")

    
    if victory("O"):
        print_board()
        print("Congratulations Player 2, You Win!")
        break
    elif draw():
        print("It is a draw!")
        break
 
