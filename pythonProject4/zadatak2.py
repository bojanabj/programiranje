sek = input("sekundi: ")
sek = int(sek)
if sek < 0 or sek > 86400:
    print("Greska.")
else:
    hh = sek // 3600
    sek = sek - (hh * 3600)
    mm = sek // 60
    sek = sek - (mm * 60)
    ss = sek
    print(str(hh) + " sati, " + str(mm) + " minuta i " + str(ss) + " sekundi. ")
