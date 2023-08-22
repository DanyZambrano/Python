nota = 15

if nota > 12 and nota < 16:
    print("Aprobo")
else:
    print("Reprobo")


if nota >= 17:
    print("Aprobo")
else:
    print("Reprobo")


if nota > 10 or nota == 16:
    print("Aprobo")
else:
    print("Reprobo")


if nota == 12:
    print("Aprobo")
elif nota >= 15:
    print("Aprobo con +")
elif nota >= 17:
    print("Aprobo con ++")
elif nota >= 19:
    print("Aprobo con Master")
else:
    print("Reprobo")