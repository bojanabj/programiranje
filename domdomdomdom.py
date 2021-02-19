hoteli = [
    {"Naziv": "Park", "Broj zvezdica": "5", "Adresa": "Novosadski Sajam 35", "Mesto": "Novi Sad"},
    {"Naziv": "Prezident", "Broj zvezdica": "5", "Adresa": "Futoska 109", "Mesto": "Novi Sad"},
    {"Naziv": "Hotel Fontana", "Broj zvezdica": "3", "Adresa": "Vrsacka 11", "Mesto": "Novi Sad"},
    {"Naziv": "Hotel Moskva", "Broj zvezdica": "4", "Adresa": "Bulevar Jase Tomica 1", "Mesto": "Veternik"}]

def meni():
    print("**************************")
    print("1. Dodavanje novog hotela \n"
          "2. Ispis svih hotela\n"
          "x Izlaz")
    print("**************************")

class hotel:
    def __init__(self, naziv, adresa, mesto):
        self.naziv = naziv
        self.adresa = adresa
        self.mesto = mesto
    def __str__(self):
        return f"Naziv: {self.naziv}" \
               f"Adresa: {self.adresa}" \
               f"Grad: {self.mesto}"

class Hotel(hotel):
    def __init__(self, brzvezdica):
        hotel.__init__(self)
        self.brzvezdica = brzvezdica

    def __str__(self):
        return f"Naziv: {self.naziv}, Adresa: {self.adresa}, Broj zvezdca: {self.brzvezdica}, Mesto: {self.mesto}"

    def dodavanje_hotela(self):
        self.naziv = input("Naziv hotela: ")
        self.mesto= input("Mesto u kom se hotel nalazi: ")
        self.brzvezdica = input("Broj zvezdica hotela: ")
        self.adresa = input("Adresa hotela: ")
        hoteli.append({"Naziv": self.naziv, "Adresa": self.adresa, "Broj zvezdica": self.brzvezdica, "Mesto": self.mesto})

if __name__ == '__main__':
    while True:
        meni()

        opcija = input("")

        if opcija == '1':
            h = Hotel
            Hotel.dodavanje_hotela(h)
            print("Hotel je dodat.", end='\n')
        elif opcija == '2':
            i = 0
            for a in hoteli:
                print(hoteli[i], end='\n')
                i = i + 1
        elif opcija == 'x':
            print("Kraj.")
            break
        else:
            print("Nepravilan unos, pokusajte ponovo.")