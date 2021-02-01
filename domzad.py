class krug:
    def __init__(self, poluprecnik):
        self.poluprecnik = poluprecnik
    def obimkruga(self, obim):
        return f"obim kruga je {obim}"
    def povrsinakruga(self, povrsina):
        return f"povrsina kruga je {povrsina}"


class pravougaonik:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obimpravougaonika(self, obim):
        return f"obim pravougaonika je {obim}"
    def povrsinapravougaonika(self, povrsina):
        return f"povrsina pravougaonika je {povrsina}"

class kvadrat:
    def __init__(self, a):
        self.a = a
    def obimpravougaonika(self, obim):
        return f"obim kvadrata je {obim}"
    def povrsinapravougaonika(self, povrsina):
        return f"povrsina kvadrata je {povrsina}"


if __name__ == '__main__':
    poluprecnikkruga = float(input("Unesite poluprecnik kruga: "))
    krug = krug(poluprecnikkruga)
    obimkr = (2*krug.poluprecnik)*3.14
    print(krug.obimkruga(obimkr))
    povrsinakr = (krug.poluprecnik*krug.poluprecnik)*3.14
    print(krug.povrsinakruga(povrsinakr))

    a = float(input("Unesite stranicu a pravouganika: "))
    b = float(input("Unesite stranicu b pravouganika: "))
    pravougaonik = pravougaonik(a, b)
    obimp = 2*(pravougaonik.a+pravougaonik.b)
    print(pravougaonik.obimpravougaonika(obimp))
    povrsinap = pravougaonik.a*pravougaonik.b
    print(pravougaonik.povrsinapravougaonika(povrsinap))

    ak = float(input("Unesite stranicu kvadrata: "))
    kvadrat = kvadrat(a)
    obimkv = 4 * kvadrat.a
    print(kvadrat.obimpravougaonika(obimkv))
    povrsinakv = kvadrat.a * kvadrat.a
    print(kvadrat.povrsinapravougaonika(povrsinakv))