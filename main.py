# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Casino import Casino
from Joueur import Joueur
from Roulette import Roulette
from MachineASous import MachineASous


def main():
    casino = Casino(100000)
    jeu1 = Roulette("my wheel", casino)
    jeu2 = MachineASous("bandit manchot", casino)
    joueur = Joueur("Clement", 1000)
    joueur.entrer_casino(casino)
    joueur.jouer()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a = 0
    for i in range(0,10):
        a += 2*i
    print(a)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
