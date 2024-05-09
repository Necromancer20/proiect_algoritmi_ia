import os

from functii.info_option import show_info
from functii.invalid_option import show_invalid_option
from functii.regine_aplinist_option import show_regine_aplinist_option
from functii.regine_backtracking_option import show_regine_backtracking_option
from functii.utils import print_board, generate_board

main_menu_text = f"""\
a. Problema celor N regine (backtracking recursiv)
b. Problema celor N regine (alg. alpinistului)
c. Problema celor N regine (alg. calirii simulate)
d. Problema celor N regine (alg. genetic)
e. Plotare grafice problema celor N regine
f. Problema comis-voiajorului (backtracking recursiv)
g. Problema comis-voiajorului (alg. celui mai apropiat vecin)
h. Plotare grafice problema comis-voiajorului
x. Info
y. Exit

Input option:
>>> """

option_to_func = {
    "y": exit,
    "x": show_info,
    "b": show_regine_aplinist_option,
    "a": show_regine_backtracking_option,
}


def main_menu():
    while True:
        os.system("cls")
        print(main_menu_text, end="")
        option = input().lower()

        func = option_to_func.get(option, show_invalid_option)
        func()


if __name__ == '__main__':
    generate_board(15)
    main_menu()
