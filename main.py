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


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    x = Pojazd("Audi", "TT", 2004, 1800, 200000, typ_skrzyni.Manualna)
    x.wypisz()


