def oopc():
    print("Opcije: \n 1. Ponovni unos \n 2. Kraj")

if __name__ == '__main__':
    while True:
        ime = input("Korisnicko ime: ")
        lozinka = input("Sifra: ")
        file = open("korisnici.txt", "a")
        file.write(ime)
        file.write("|")
        file.write(lozinka)
        file.write("\n")
        print("Unos uspesan.")
        file.close()
        oopc()
        opc = input("Izaberite opciju: ")
        if opc == '2':
            break