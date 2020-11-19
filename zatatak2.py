def spoj():
    string1 = input("Unesite prvi string (min 3 karaktera): ")
    string2 = input("Unesite drugi string (min 3 karaktera): ")
    string_prvi = string1[0:3]
    string_poslednji = string2[-3:]
    novi_string = string_prvi + string_prvi + string_poslednji
    print(novi_string)

if __name__ == '__main__':
    spoj()