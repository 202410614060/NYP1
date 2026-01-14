sifre = input("Şifre girin: ")

uzunluk = len(sifre) >= 8
buyuk_harf = any(harf.isupper() for harf in sifre)
kucuk_harf = any(harf.islower() for harf in sifre)
rakam = any(harf.isdigit() for harf in sifre)
bosluk = any(harf.isspace() for harf in sifre)

if uzunluk and buyuk_harf and kucuk_harf and rakam and not bosluk:
    print("Güçlü Şifre")
else:
    print("Zayıf Şifre")
