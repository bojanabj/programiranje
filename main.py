inventar = {}

def meni():
    print("------- MENI -------")
    print("1. Ispis zivotinja.")
    print("2. Unos nove zivotinje.")
    print("3. Izmena vec unete zivotinje.")
    print("4. Uklanjanje zivotinje.")
    print("5. Kraj programa.")
    print("--------------------")

def ispis_zivotinja():
    for vrsta_zivotinje, mesto_zivljenja in inventar.items():
        print(vrsta_zivotinje, mesto_zivljenja)

def unos_zivotinja():
    print("------- Unos zivotinje ------- ")
    vrsta_zivotinje = input("Vrsta zivotinje: ")
    mesto_zivljenja = input("Mesto na kom zivotinja zivi: ")
    inventar[vrsta_zivotinje] = mesto_zivljenja
    print(inventar)

def izmena_zivotinje():
    vrsta_zivotinje = input("Unesite vrstu zivotinje kojoj zelite da promenite mesto stanovanja: ")
    print("Pre promene: ")
    print(inventar)
    promena = input("Novo prebivaliste zivotinje: ")
    inventar[vrsta_zivotinje] = promena
    print("Posle promene: ")
    print(inventar)

def uklanjanje_zivotinje():
    begone = input("Unesite vrstu zivotinje koju zelite da uklonite: ")
    inventar.pop(begone)
    print("Zivotinja je uklonjena.")
    print(inventar)

if __name__ == '__main__':
    while True:
        meni()

        opcija = input("Izaberite opciju od 1 do 5: ")

        if opcija == '1':
            ispis_zivotinja()
        elif opcija == '2':
            unos_zivotinja()
        elif opcija == '3':
            izmena_zivotinje()
        elif opcija == '4':
            uklanjanje_zivotinje()
        elif opcija == '5':
            print("Kraj programa.")
            break