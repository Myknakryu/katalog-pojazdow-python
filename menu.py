
opcje_menu = ["Wczytaj bazę", "Zapisz bazę", "Wypisz bazę", "Wprowadź pojazd do bazy",
              "Usuń element z bazy", "Wyświetl szczegóły pojazdu", "Sortuj",
              "Wyszukaj", "Wyjdź z programu"]


def generuj_menu():
    txt = "{}. {}"
    i = 0
    for opcja in opcje_menu:
        i += 1
        print(txt.format(i, opcja))
    pass


def wybor_elementu(katalog, wiadomosc):
    txt = "{} \n Zakres od 0 do {} "
    while len(katalog) > 0:
        opcja = int(input(txt.format(wiadomosc, len(katalog)-1)))
        if 0 <= opcja < len(katalog):
            return opcja


def wybor_atrybutu(element):
    txt = "{}. {}"
    i = 0
    for atrybut in dir(element)[0:5]:
        print(txt.format(i, atrybut))
        i += 1
    opcja = int(input("Wybierz opcje: "))
    return opcja
