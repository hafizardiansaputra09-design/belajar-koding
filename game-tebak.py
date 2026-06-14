angka_rahasia = 7

print ("===GAME TEBAK ANGKA ===")
print ("gua udah siapin angka dari 1-10")

for kesempatan in range(3):

    tebakan = int(input("coba tebak angka yg menurut lu bener bre!"))

    if tebakan == angka_rahasia:
       print("Gokil bre!, tebakan lu bener. lu menang!")
       break

    else:
       print("Salah cuk, insting lu kurang tajem. Coba lagi!")

print("Game Over! Lu orangnya kurang gokil bre!")
