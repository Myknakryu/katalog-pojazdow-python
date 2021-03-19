from pojazd import *
from operacje_plikowe import *
from menu import generuj_menu

if __name__ == '__main__':
    katalog = []
    while True:
        generuj_menu()
        opcja = int(input("Wybierz opcje: "))
        if opcja == 1:
            katalog = wczytanie()
        elif opcja == 2:
            zapis(katalog)
        elif opcja == 3:
            for pojazd in katalog:
                pojazd.wypisz()
        elif opcja == 4:
            katalog.append(wczytaj_pojazd())
        elif opcja == 9:
            break
