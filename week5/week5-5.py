liste = [3, 'a', 1, 'c', 5, 2, 'b', 4]

sayilar = []
harfler = []

# Veri türüne göre ayırma
for eleman in liste:
    if type(eleman) == int:
        sayilar.append(eleman)
    elif type(eleman) == str:
        harfler.append(eleman)

# Ayrı ayrı sıralama
sayilar.sort()
harfler.sort()

# Birleştirme
sonuc = sayilar + harfler

print(sonuc)
