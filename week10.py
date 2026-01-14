import random

def sayi_bulma_oyunu():
    tutulan_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    print("1 ile 100 arasında bir sayı tuttum.")
    print("Tahmininizi girin (Çıkmak için q):")

    while True:
        tahmin = input("Tahmininiz: ")

        if tahmin.lower() == "q":
            print("Oyundan çıkıldı.")
            break

        if not tahmin.isdigit():
            print("Hatalı giriş! Lütfen bir sayı girin.")
            continue

        tahmin = int(tahmin)
        deneme_sayisi += 1

        if tahmin < tutulan_sayi:
            print("Daha büyük bir sayı girin")
        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayı girin")
        else:
            print("Tebrikler! Doğru bildiniz.")
            print("Deneme sayısı:", deneme_sayisi)
            break

# Oyunu başlat
sayi_bulma_oyunu()
