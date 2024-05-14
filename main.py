import os

from functii.comis_voiajor_apropiat_vecin_option import show_tsp_nearest_neighbor_option
from functii.comis_voiajor_bkt_rec_option import show_tsp_recursive_backtracking_option
from functii.info_option import show_info
from functii.invalid_option import show_invalid_option
from functii.n_regine_plot_option import show_n_regine_plot
from functii.regine_aplinist_option import show_regine_aplinist_option
from functii.regine_backtracking_option import show_regine_backtracking_option
from functii.regine_genetic_algorithm_option import show_genetic_algorithm_option
from functii.regine_simulated_annealing_option import show_simulated_annealing_option
from functii.utils import print_board, generate_board
from plot.comis_voiajor_plot import plot_tsp_results, plot_tsp_results_option

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
    "h": plot_tsp_results,
    "g":show_tsp_nearest_neighbor_option,
    "f": show_tsp_recursive_backtracking_option,
    "e": show_n_regine_plot,
    "d": show_genetic_algorithm_option,
    "c": show_simulated_annealing_option,
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
