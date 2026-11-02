# Lab 5 - runs minimax and alpha-beta
import platform

from src import lab5_alphabeta, lab5_compare, lab5_minimax


def main():
    print("AI Lab 5: Adversarial Search, Minimax & Alpha-Beta | Mohammed Emad ALaini")
    print("Python %s, standard library only" % platform.python_version())
    print()
    lab5_minimax.main()
    print()
    lab5_alphabeta.main()
    print()
    lab5_compare.main()


if __name__ == "__main__":
    main()
