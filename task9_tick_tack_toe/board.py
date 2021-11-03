def init_game_board():
    """игровая доска"""
    game_board = {1: '1', 2: '2', 3: '3',
                  4: '4', 5: '5', 6: '6',
                  7: '7', 8: '8', 9: '9'}
    return game_board


def print_board(game_board):
    print("")
    print("\t     |     |")
    print(f"\t  {game_board[1]}  |  {game_board[2]}  |  {game_board[3]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {game_board[4]}  |  {game_board[5]}  |  {game_board[6]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {game_board[7]}  |  {game_board[8]}  |  {game_board[9]}")
    print("\t     |     |\n")


if __name__ == "__main__":
    pass
