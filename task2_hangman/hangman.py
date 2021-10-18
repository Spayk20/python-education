import re
import random
from time import sleep
from datetime import datetime

from hangman_pics import LEN_HANGMAN, HANGMAN_PICS

# All words must be in "words.txt" file. Each word starts new line.
WORDS_LIBRARY_FILE = "F:\python-education\task2_hangman\words.txt"


def menu() -> str:
    print("HANGMAN")
    print("Начать(нажми 1)\nПосмотреть прошлые слова(нажми 2)\nВыйти(нажми 3)")
    print("Для экстренного выхода в любой момент жми - command+F2")
    while True:
        user_choice = input()
        if user_choice in ("1", "2", "3"):
            break
        print("Выберите нужный пункт меню")
    return user_choice


def game():
    secret_word = random_word()

    # initialize missed_letters, correct_letters, win_flag
    missed_letters = ""
    correct_letters = ""
    win_flag = "Win"
    while True:
        display_board(secret_word, missed_letters, correct_letters)

        user_letter = user_input(missed_letters, correct_letters)

        # check is letter in word or no. check if player won or loose
        if user_letter in secret_word:
            correct_letters = correct_letters + user_letter
            # print(set(secret_word), set(correct_letters))
            if set(secret_word) == set(correct_letters):
                print("You Win!")
                break
            print("Yes!!")
            sleep(1)
        else:
            missed_letters = missed_letters + user_letter
            if len(missed_letters) == LEN_HANGMAN:
                print("Ты проиграл, загаданное слово:", secret_word)
                win_flag = "Lose"
                break
            print("No!!")
            sleep(1)
    write_in_file(secret_word, win_flag)


def random_word() -> str:
    """Open file. Define random word (4<= word <12) from library. Strip() and lower() it"""
    with open(WORDS_LIBRARY_FILE, "r") as f:
        words_library_list = list(f)
    # number of words in file
    len_words_library_list = len(words_library_list) - 1
    while True:
        # find random line
        random_line = random.randint(0, len_words_library_list)
        # len of word must be more than 3 and less then 12
        if len(words_library_list[random_line]) in range(4, 12):
            break
    return words_library_list[random_line].strip().lower()


def display_board(secret_word: str, missed_letters: str, correct_letters: str):
    """only display: hangman pic, mistakes quantity and missed letters"""
    print(HANGMAN_PICS[len(missed_letters)])
    for i in secret_word:
        if i in correct_letters:
            print(i, end='')
        else:
            print("_", end='')
    print()
    print("Ошибки({})".format(len(missed_letters)), missed_letters)
    print("Ваша буква:", end="")


def user_input(missed_letters: str, correct_letters: str) -> str:
    """Return the players entered letter."""
    while True:
        user_letter = input().lower()
        # match only russian alphabet
        match = re.match("[а-я]", user_letter)
        if user_letter in correct_letters or user_letter in missed_letters:
            print("Зачем вводить уже известную букву")
        elif len(user_letter) == 1 and match:
            break
    return user_letter


def write_in_file(secret_word: str, win_flag: str):
    """Open file and append word, win or lose game and datetime"""
    with open("log_file.txt", "a") as f:
        f.write(secret_word + " " + win_flag + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")


def read_file():
    """Open file and print it out"""
    with open("log_file.txt", "r") as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    user_choice = menu()
    # game
    if user_choice == "1":
        while True:
            game()
            exit_flag = input("Хочешь выйти?(y/n)")
            if exit_flag.lower() != "n":
                break
    # display games history
    elif user_choice == "2":
        read_file()
        pass
    else:
        print("Заходи еще")
