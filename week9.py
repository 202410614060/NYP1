# 1. [1,2,3,4,5] listesindeki sayıların küpü
sayilar = [1, 2, 3, 4, 5]

# lambda ile
kup_lambda = list(map(lambda x: x**3, sayilar))
print(kup_lambda)

# lambda olmadan
def kup(x):
    return x**3

kup_fonksiyon = list(map(kup, sayilar))
print(kup_fonksiyon)


# 2. [1, 3, 5, 15, 20, 30, 7, 9] listesindeki 3'e ve 5'e tam bölünenler
sayilar2 = [1, 3, 5, 15, 20, 30, 7, 9]

# lambda ile
bolunenler_lambda = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, sayilar2))
print(bolunenler_lambda)

# lambda olmadan
def bolunen(x):
    return x % 3 == 0 and x % 5 == 0

bolunenler_fonksiyon = list(filter(bolunen, sayilar2))
print(bolunenler_fonksiyon)


# 3. [-4, 5, -2, 0, 3] listesinin mutlak değerleri (map ile)
sayilar3 = [-4, 5, -2, 0, 3]

mutlak_degerler = list(map(abs, sayilar3))
print(mutlak_degerler)


# 4. 0-10 arasındaki sadece çift sayıların kareleri (liste üreteci)
cift_kareler = [x**2 for x in range(11) if x % 2 == 0]
print(cift_kareler)


# 5. String listesi işlemleri
kelimeler = ["python", "java", "c", "javascript", "go"]

# 4 harften uzun olanları filtrele
uzun_kelimeler = list(filter(lambda x: len(x) > 4, kelimeler))
print(uzun_kelimeler)

# Büyük harfe çevir (map ile)
buyuk_harfler = list(map(str.upper, uzun_kelimeler))
print(buyuk_harfler)


# 6. Öğrenci listesinden notu 50'den yüksek olanların isimlerini büyük harfle listele
ogrenciler = [
    {"ad": "merve", "not": 65},
    {"ad": "ayse", "not": 45},
    {"ad": "mehmet", "not": 80},
    {"ad": "fatma", "not": 30}
]

basarili_ogrenciler = [
    ogrenci["ad"].upper()
    for ogrenci in ogrenciler
    if ogrenci["not"] > 50
]

print(basarili_ogrenciler)


# 7. İki listeyi birleştirerek sözlük oluşturma
anahtarlar = ["isim", "yas", "sehir"]
degerler = ["Ahmet", 25, "Ankara"]

sozluk = dict(zip(anahtarlar, degerler))
print(sozluk)


# 8. Generator expression
liste = [10, "ali", 3.5, None, 7, "45"]

kareler_generator = (x**2 for x in liste if isinstance(x, (int, float)))
print(list(kareler_generator))
