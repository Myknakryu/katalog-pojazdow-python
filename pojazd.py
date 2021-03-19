from enum import Enum


class typ_skrzyni(Enum):
    Manualna = 0
    Automatyczna = 1


class Pojazd:
    def __init__(self, marka, model, rocznik, pojemnosc, przebieg, skrzynia):
        self.Marka = marka
        self.Model = model
        self.Rocznik = rocznik
        self.Pojemnosc = pojemnosc
        self.Przebieg = przebieg
        self.Skrzynia = skrzynia

    def wypisz(self):
        txt = "{} {} - {} - {} cm³ - {}km - {}"
        print(txt.format(self.Marka, self.Model, self.Rocznik, self.Pojemnosc, self.Przebieg, self.Skrzynia.name))


def wczytaj_pojazd():
    marka = input("Podaj markę pojazdu: ")
    model = input("Podaj model pojazdu: ")
    rocznik = int(input("Z którego roku jest pojazd: "))
    pojemnosc = int(input("Podaj pojemność silnika: "))
    przebieg = int(input("Podaj przebieg: "))
    skrzynia = typ_skrzyni.Manualna
    if int(input("Wprowadz 1 jeśli skrzynia jest automatyczna: ")) == 1:
        skrzynia = typ_skrzyni.Automatyczna
    return Pojazd(marka, model, rocznik, pojemnosc, przebieg, skrzynia)
