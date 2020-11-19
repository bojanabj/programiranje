def ispis_korisnika():
    file = open("korisnici.txt", "r")
    for line in file.readlines():
        korisnik = line.split("|")
        username = korisnik[0]
        password = korisnik[1]
        print("Korisnicko ime: " + username)
        print("Lozinka: " + password)
    file.close()


if __name__ == '__main__':
    ispis_korisnika()