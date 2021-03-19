
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

