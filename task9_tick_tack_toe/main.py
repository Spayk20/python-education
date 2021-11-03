import os
import tic_tac_toe


def main():
    """Здесь пишем пункты меню"""
    while True:
        user_choice = menu()
        # старт игры
        if user_choice == "1":
            tic_tac_toe.game()
        # история игр
        elif user_choice == "2":
            display_log_files()
        # очистить историю игр
        elif user_choice == "3":
            clean_log_files()
        # выход
        else:
            print("Заходи еще")
            break


def menu() -> str:
    """Главное меню"""
    print("\tTIC-TAC-TOE")
    print(
        "Играть (нажми 1)\n"
        "История игр (нажми 2)\n"
        "Очистить историю (нажми 3)\n"
        "Выйти (нажми 4)"
        )

    while True:
        user_choice = input()
        if user_choice in ("1", "2", "3", "4"):
            break
        print("Выберите нужный пункт меню")
    return user_choice


def display_log_files():
    """История игр - лог файл"""
    def display_log_file(file_name: str):
        print(f"\n{file_name.upper()}\n")
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл: {OSError.filename} - {OSError.strerror}.")
    display_log_file("matches.log")
    display_log_file("revanche.log")


def clean_log_files():
    """Очистка истории - лог файла"""
    def clean_log_file(file):
        # пробуем удалить файл
        try:
            os.remove(file)
        except OSError:  # пишем ошибку если нечего удалять
            print(f"Error: {OSError.filename} - {OSError.strerror}.")
    clean_log_file("matches.log")
    clean_log_file("revanche.log")


if __name__ == "__main__":
    main()
