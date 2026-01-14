# 1. İki sayının ortalamasını hesaplayan fonksiyon
def ortalama(sayi1, sayi2):
    return (sayi1 + sayi2) / 2


# 2. Değişken sayıda parametre alıp toplam döndüren fonksiyon
def toplam(*sayilar):
    return sum(sayilar)


# 3. Hesap makinesi fonksiyonu
def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            return "Sıfıra bölme hatası"
        return sayi1 / sayi2


# 4. Liste işlemleri fonksiyonu
def liste_islemleri(liste, islem):
    if islem == "tek":
        return [x for x in liste if x % 2 == 1]
    elif islem == "cift":
        return [x for x in liste if x % 2 == 0]
    elif islem == "ters":
        return liste[::-1]
    elif islem == "kare":
        return [x ** 2 for x in liste]


# 5. Şifre doğrulama fonksiyonu
def sifre_dogrulama(sifre):
    if len(sifre) < 8:
        return False

    buyuk = False
    kucuk = False
    rakam = False

    for karakter in sifre:
        if karakter.isupper():
            buyuk = True
        elif karakter.islower():
            kucuk = True
        elif karakter.isdigit():
            rakam = True

    return buyuk and kucuk and rakam


# Testler (fotoğraftaki örnekler)
print(ortalama(10, 20))
print(toplam(1, 2, 3, 4))
print(hesap_makinesi(15, 5, "+"))
print(hesap_makinesi(15, 5, "-"))
print(liste_islemleri([1, 2, 3, 4, 5], "tek"))
print(liste_islemleri([1, 2, 3, 4, 5], "kare"))
print(sifre_dogrulama("Python123"))
print(sifre_dogrulama("python"))

