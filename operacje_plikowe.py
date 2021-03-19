import pickle


def zapis(katalog):
    plik = open("baza.bin", "wb")
    pickle.dump(katalog, plik)
    plik.close()


def wczytanie():
    plik = open("baza.bin", "rb")
    katalog = pickle.load(plik)
    plik.close()
    return katalog
