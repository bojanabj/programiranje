import random

def meni():
    print("**************************")
    print("1 - Dodaj knjigu")
    print("2 - Podaci o biblioteci")
    print("3 - Podaci o knjizi")
    print("x - Izlaz ")
    print("**************************")

class biblioteka:

    def __init__(self, imeBib):
        self.naziv = imeBib
        self.knjige = []

class knjiga:

    def __init__(self, naslov, autor, zanr):
        self.isbn = str(random.randint(1, 1000))
        self.naslov = naslov
        self.autor = autor
        self.zanr = zanr
        self.biblioteka = biblioteka

biblioteka = biblioteka("gradska biblioteka")
biblioteka.knjige = [{"Naslov": "Mlada elita", "Autor": "Mari Lu", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Persi Dzekson i Bogovi Olimpa", "Autor": "Rik Riordan", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Evgenije Onjegin", "Autor": "Aleksandar Sergejevic Puskin", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))},
                     {"Naslov": "Ana Karenjina", "Autor": "Lav Nikolajevic Tolstoj", "Zanr": "roman", "ISBN": str(random.randint(1, 1000))}]

def podaci_o_biblioteci():
    print("Biblioteka:", biblioteka.naziv)
    print("Dostupne knjige: ", biblioteka.knjige)

def dodavanje_knjige():
    naslov = input("Unesite naziv: ")
    autor = input("Unesite autora: ")
    zanr = input("Unesite zanr: ")
    nova_knjiga = knjiga(naslov, autor, zanr)
    biblioteka.knjige.append({"Naslov": nova_knjiga.naslov,
                              "Autor": nova_knjiga.autor,
                              "Zanr": nova_knjiga.zanr,
                              "ISBN": nova_knjiga.isbn})
    print("Knjiga je dodata.")

def podaci_o_knjigama():
    pretraga_po_isbn = input("Unesite ISBN knjige: ")

    for knjiga in biblioteka.knjige:
        if pretraga_po_isbn == knjiga["ISBN"]:
            x = 1
            print(knjiga)
            break
        else:
            x = 2
    if x == 2:
        print("Knjiga nije dostupna.")

if __name__ == '__main__':
    while True:
        meni()

        opcija = input(">>> ")

        if opcija == "1":
            dodavanje_knjige()
        if opcija == "2":
            podaci_o_biblioteci()
        if opcija == "3":
            podaci_o_knjigama()
        if opcija == "x":
            break