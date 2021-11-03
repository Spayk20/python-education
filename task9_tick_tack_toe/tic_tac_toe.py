from random import randint
from time import sleep

from board import init_game_board, print_board
from logger import logger


class Player:
    """Имя и сторона игрока"""
    def __init__(self, name: str, x_race: str):
        self.name = name
        self.x_race = x_race

    def get_race(self) -> str:
        """получаем сторону"""
        return self.x_race

    def set_race(self, x_race: str):
        """устанавливаем сторону"""
        self.x_race = x_race


def game(first_player: Player = None, second_player: Player = None, revanche_flag=False):
    logger.debug("\t\tGAME START")
    game_board = init_game_board()
    if not revanche_flag:
        first_name, second_name = input_players_name()
        first_player, second_player = get_random_first_player(first_name, second_name)
    player = first_player
    move_count = 1
    while True:
        print_board(game_board)
        print(f"Ходит - {player.name.upper()} ")
        turn(player, game_board)
        if move_count >= 5:
            if is_player_win(game_board):
                win(player, game_board, revanche_flag)
                break
        if move_count == 9:
            standoff(revanche_flag)
            break
        player = swap_player_turn(player, first_player, second_player)
        move_count += 1
    revanche(first_player, second_player)


def input_players_name() -> tuple:
    """принимаем имена игроков"""
    first_name = input("Ведите имя первого игрока: ")
    second_name = input("Ввелите имя второго игрока: ")
    return first_name, second_name


def get_random_first_player(first_name: str, second_name: str) -> tuple:
    """случайным образом выбираем игрока, который делает первый шаг"""
    if randint(0, 1) == 1:
        first_name, second_name = second_name, first_name
    first_player = Player(first_name, "X")
    second_player = Player(second_name, "O")
    logger.debug(f"Первый игрок: {first_player.name.upper()}, игрет '{first_player.get_race()}'. \
                Второй игрок: {second_player.name.upper()}, играет '{second_player.get_race()}'")
    return first_player, second_player


def turn(player: Player, game_board: dict):
    """меняем местами игроков"""
    while True:
        player_pick = int(input("Введите цифру чтобы поставить знак: "))
        if game_board[player_pick] not in ("X", "O"):
            game_board[player_pick] = player.get_race()
            break
    print()


def swap_player_turn(player: Player, first_player: Player, second_player: Player) -> Player:
    """меняем сторону текущего игрока"""
    player = second_player if player.get_race() == 'X' else first_player
    return player


def is_player_win(game_board: dict) -> bool:
    """функия проверки всех выигрышных комбинаций"""
    # строки
    if len(set(map(game_board.get, (1, 2, 3)))) == 1 or\
       len(set(map(game_board.get, (4, 5, 6)))) == 1 or\
       len(set(map(game_board.get, (7, 8, 9)))) == 1:
        return True
    # столбцы
    if len(set(map(game_board.get, (1, 4, 7)))) == 1 or\
       len(set(map(game_board.get, (2, 5, 8)))) == 1 or\
       len(set(map(game_board.get, (3, 6, 9)))) == 1:
        return True
    # диагонали
    if len(set(map(game_board.get, (1, 5, 9)))) == 1 or\
       len(set(map(game_board.get, (3, 5, 7)))) == 1:
        return True
    return False


def win(player, game_board, revanche_flag):
    """победа одного из игроков"""
    print_board(game_board)
    print(f"\tПоздравлем, {player.name} ты победил")
    print("\n\tGame is over\n")
    logger.debug(f"\t\t{player.name.upper()} Победил. Сторона '{player.get_race()}'.")
    if revanche_flag:
        logger.info(f"\t\t{player.name.upper()} Победил. Сторона '{player.get_race()}'.")
    sleep(2)


def standoff(revanche_flag):
    """пишем в логгер"""
    print("\tStandoff")
    print("\n\tGame is over\n")
    logger.debug("\t\tStandoff.")
    if revanche_flag:
        logger.info("\t\tStandoff.")


def revanche(first_player: Player, second_player: Player):
    """предложение реванша с тем же игроком"""
    user_choice = input("Реванш?(Y/N): ")
    print()
    # если игрок согласен, тогда меняем стороны
    if user_choice.lower() in ("y", "yes"):
        first_player, second_player = second_player, first_player
        first_player.set_race("X")
        second_player.set_race("O")
        # пишем лог
        logger.info("\t\tДа начнется игра!")
        logger.info(f"Первый игрок: {first_player.name.upper()}, сторона '{first_player.get_race()}'.\
                    Второй игрок: {second_player.name.upper()}, сторона '{second_player.get_race()}'")
        game(first_player, second_player, revanche_flag=True)
