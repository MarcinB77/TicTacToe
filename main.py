from os import system, name

num_board = """  7  |  8  |  9  
-----------------
  4  |  5  |  6  
-----------------
  1  |  2  |  3  
  """
play_board = """     |     |     
-----------------
     |     |       
-----------------
     |     |     
     """
positions = {
    "1": 76,
    "2": 82,
    "3": 88,
    "4": 38,
    "5": 44,
    "6": 50,
    "7": 2,
    "8": 8,
    "9": 14
}
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
game = True


def clear():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')
    return x


def check_result():
    global game, play_board
    for c in winning_combinations:
        if play_board[positions[str(c[0])]] == play_board[positions[str(c[1])]] == play_board[positions[str(c[2])]]:
            if play_board[positions[str(c[0])]] == "X":
                game = False
                print("<<< X wins! >>>")
                print(play_board)
            elif play_board[positions[str(c[0])]] == "0":
                game = False
                print("<<< 0 wins! >>>")
                print(play_board)
        else:
            pass


def input_x():
    global play_board
    choice = input("Player 'X' - choose field number:  ")
    s_table = list(play_board)
    if s_table[positions[str(choice)]] != "0" and s_table[positions[str(choice)]] != "X":
        s_table[positions[str(choice)]] = "X"
        s = """"""
        play_board = s.join(s_table)
    else:
        print("This field is taken, choose another one.")
        input_x()


def input_0():
    global play_board
    choice = input("Player '0' - choose field number:  ")
    s_table = list(play_board)
    if s_table[positions[str(choice)]] != "X" and s_table[positions[str(choice)]] != "0":
        s_table[positions[str(choice)]] = "0"
        s = """"""
        play_board = s.join(s_table)
    else:
        print("This field is taken, choose another one.")
        input_0()


def round_x():
    global num_board, play_board
    print(num_board)
    print(play_board)
    input_x()
    check_result()


def round_o():
    global num_board, play_board
    print(num_board)
    print(play_board)
    input_0()
    check_result()


while game:
    round_x()
    if not game:
        break
    clear()
    round_o()
    if not game:
        break
    clear()
