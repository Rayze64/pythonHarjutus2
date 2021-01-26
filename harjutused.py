import random


# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
# Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
# Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".

def h1():
    arv = int(input("Sisesta arv"))
    if 0 < arv <= 101:
        print("Arv on vahemikus 0st 100ni")
    elif 101 < arv <= 1000:
        print("Arv on vahemikus 101st 1000ni")


# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
# Kui arv on negatiivne, siis printige see välja

def h2():
    arvud = [5, 9, 1, -2, 6, -15, -20]
    for num in arvud:
        if num < 0:
            print(num)


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus

def h3():
    sisend = [1, 3, 4, 3]
    for num in sisend:
        print("$" * num)


# Harjutus 4
# Palun luua funktsioon, mis genereerib etteantud pikkusega parooli, mis koosneb suvalistest tähtedest ja sümbolitest.
# Tähed võivad suvaliselt olla kas suured või väikesed tähed.

def h4():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ!"#%&/()=1234567890'
    pwlength = int(input("Type password length: "))
    password = ""
    for x in range(pwlength):
        password += random.choice(letters)
    print(password)


h4()
