def sortuj(katalog, opcja, malejaca):
    x = dir(katalog[0])
    try:
        import operator
    except ImportError:
        keyfun = lambda x: x.Marka
    else:
        keyfun = operator.attrgetter(x[opcja])
    katalog.sort(key=keyfun, reverse=malejaca)
