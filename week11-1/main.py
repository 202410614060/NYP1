# main.py

import os
from fonksiyonlar import dosyayi_oku, ortalama, nota_gore_sirala, arama_yap

# Dosya yolu (çalışma dizini hatası olmaması için)
BASE_DIR = os.path.dirname(__file__)
DOSYA_YOLU = os.path.join(BASE_DIR, "ogrenciler.txt")

# Dosyadan öğrencileri oku
ogrenciler = dosyayi_oku(DOSYA_YOLU)

# Ortalama hesapla
print("Sınıf Ortalaması:", ortalama(ogrenciler))

# Nota göre sırala ve yazdır
print("\nNota Göre Sıralı Liste:")
sirali_liste = nota_gore_sirala(ogrenciler)
for ogrenci in sirali_liste:
    print(
        ogrenci["numara"],
        ogrenci["ad_soyad"],
        ogrenci["not"]
    )

# Öğrenci arama
print("\nÖğrenci Arama:")
aranan_isim = "Zeynep Şahin"
sonuc = arama_yap(ogrenciler, aranan_isim)

if sonuc:
    print(
        sonuc["ad_soyad"],
        "numara:",
        sonuc["numara"],
        "not:",
        sonuc["not"]
    )
else:
    print("Öğrenci bulunamadı")

