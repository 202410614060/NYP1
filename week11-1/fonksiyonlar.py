# fonksiyonlar.py

def dosyayi_oku(dosya_adi):
    ogrenci_listesi = []

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()
            numara, ad_soyad, notu = satir.split(",")

            ogrenci = {
                "numara": int(numara),
                "ad_soyad": ad_soyad,
                "not": int(notu)
            }

            ogrenci_listesi.append(ogrenci)

    return ogrenci_listesi


def ortalama(ogrenci_listesi):
    toplam = 0

    for ogrenci in ogrenci_listesi:
        toplam += ogrenci["not"]

    return toplam / len(ogrenci_listesi)


def nota_gore_sirala(ogrenci_listesi):
    return sorted(
        ogrenci_listesi,
        key=lambda ogrenci: ogrenci["not"],
        reverse=True
    )


def arama_yap(ogrenci_listesi, aranan_isim):
    for ogrenci in ogrenci_listesi:
        if ogrenci["ad_soyad"] == aranan_isim:
            return ogrenci
    return None
