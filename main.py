from pojazd import *
from operacje_plikowe import *
from funkcje import *
from menu import *


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
        elif opcja == 5:
            x = wybor_elementu(katalog, "Podaj element do usunięcia: ")
            katalog.pop(x)
        elif opcja == 6:
            x = wybor_elementu(katalog, "Podaj element do wyświetlenia")
            katalog[x].wypisz()
        elif opcja == 7:
            atrybut = wybor_atrybutu(katalog[0])
            rosnaca = False
            if int(input("Wprowadź (1) aby sortować rosnąco: ")) == 1:
                rosnaca = True
            sortuj(katalog, atrybut, rosnaca)
        elif opcja == 8:
            import datetime
            rok =  datetime.datetime.now().year - 2
            print("Pojazdy wyprodukowane po {}:".format(rok))
            for x in katalog:
                if x.Rocznik >= rok:
                    x.wypisz()
        elif opcja == 9:
            break
