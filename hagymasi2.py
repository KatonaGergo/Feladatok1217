varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

varos = input("Írj be egy városnevet!")

if varos in varosok:
    index = varosok.index(varos)
    if index < len(varosok):
        print(f"A következő város: {varosok[index+1]}")
    else:
        print("Ez az utolsó város, nincs következő")
        
else:
    print("Felveszem a várost a listába, mivel nem szerepel benne!")
    varosok.append(varos)