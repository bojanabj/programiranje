def akronimf():
    fraza = input("Unesite frazu: ")
    r = fraza.split()
    akronim = ""
    for i in r:
        akronim = akronim + i[0].upper()
    print("Akronim je ",akronim)

if __name__ == '__main__':
    akronimf()