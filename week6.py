# -----------------------------
# 1. ÜRÜN FİYATLARI
# -----------------------------
urun_fiyatlari = {
    "laptop": 12000,
    "telefon": 8000,
    "tablet": 5000,
    "kulaklik": 1500
}

# 6000 TL'den yüksek ürünler
pahali_urunler = [urun for urun, fiyat in urun_fiyatlari.items() if fiyat > 6000]
print("6000 TL'den pahalı ürünler:", pahali_urunler)

# %10 zamlı fiyatlar
zamli_fiyat = {urun: fiyat * 1.10 for urun, fiyat in urun_fiyatlari.items()}
print("Zamlı fiyatlar:", zamli_fiyat)

# En pahalı ve en ucuz ürün
en_pahali = max(urun_fiyatlari, key=urun_fiyatlari.get)
en_ucuz = min(urun_fiyatlari, key=urun_fiyatlari.get)

print("En pahalı ürün:", en_pahali, urun_fiyatlari[en_pahali])
print("En ucuz ürün:", en_ucuz, urun_fiyatlari[en_ucuz])


# -----------------------------
# 2. ÖĞRENCİLERİ NOTA GÖRE GRUPLAMA
# -----------------------------
ogrenciler = [
    {"ad": "Ali", "not": 85},
    {"ad": "Ayşe", "not": 45},
    {"ad": "Mehmet", "not": 85},
    {"ad": "Zeynep", "not": 60}
]

gruplama = {}

for ogrenci in ogrenciler:
    notu = ogrenci["not"]
    adi = ogrenci["ad"]

    if notu not in gruplama:
        gruplama[notu] = []

    gruplama[notu].append(adi)

print("Notlara göre gruplama:", gruplama)


# -----------------------------
# 3. NOT ORTALAMASI HESAPLAMA
# -----------------------------
ogrenciler = [
    {"ad": "Ali", "notlar": [85, 90, 78]},
    {"ad": "Veli", "notlar": [70, 65, 80]},
    {"ad": "Ayşe", "notlar": [95, 88, 92]}
]

for ogrenci in ogrenciler:
    ortalama = sum(ogrenci["notlar"]) / len(ogrenci["notlar"])
    ogrenci["ortalama"] = ortalama

print("Ortalamalar eklendi:", ogrenciler)

# En yüksek ortalamaya sahip öğrenci
en_yuksek = max(ogrenciler, key=lambda x: x["ortalama"])
print("En yüksek ortalama:", en_yuksek["ad"], en_yuksek["ortalama"])

# Sınıf ortalaması
sinif_ort = sum(o["ortalama"] for o in ogrenciler) / len(ogrenciler)
print("Sınıf ortalaması:", sinif_ort)


# -----------------------------
# 4. KÜME İŞLEMLERİ
# -----------------------------
urunler_A = {"elma", "armut", "muz", "kiraz", "soğan"}
urunler_B = {"muz", "kiraz", "çilek", "karpuz", "sarımsak"}

# Birleşim
birlesim = urunler_A | urunler_B
print("Birleşim:", birlesim)

# Sadece meyveler (sebzeleri çıkar)
sebzeler = {"soğan", "sarımsak"}
meyveler = (urunler_A | urunler_B) - sebzeler
print("Sadece meyveler:", meyveler)

# Ortak elemanlar
ortak = urunler_A & urunler_B
print("Ortak ürünler:", ortak)


# -----------------------------
# 5. KİTAPLIK UYGULAMASI
# -----------------------------
kitaplar = {
    1: {"ad": "Suç ve Ceza", "yazar": "Dostoyevski"},
    2: {"ad": "Kürk Mantolu Madonna", "yazar": "Sabahattin Ali"}
}

def kitap_ekle(id, ad, yazar):
    kitaplar[id] = {"ad": ad, "yazar": yazar}

def yazar_guncelle(id, yeni_yazar):
    if id in kitaplar:
        kitaplar[id]["yazar"] = yeni_yazar

def kitaplari_listele():
    for id, bilgi in kitaplar.items():
        print(id, bilgi)

kitap_ekle(3, "1984", "George Orwell")
yazar_guncelle(1, "F. Dostoyevski")
kitaplari_listele()


# -----------------------------
# 6. ALIŞVERİŞ FİŞİ UYGULAMASI
# -----------------------------
urunler = {
    "elma": 5,
    "muz": 8,
    "ekmek": 7,
    "sut": 15
}

sepet = {}

while True:
    urun = input("Ürün adı girin (tamam için 'tamam'): ").lower()

    if urun == "tamam":
        break

    if urun not in urunler:
        print("Geçersiz ürün!")
        continue

    miktar = input("Miktar girin: ")

    if not miktar.isdigit() or int(miktar) <= 0:
        print("Geçersiz miktar!")
        continue

    miktar = int(miktar)

    if urun in sepet:
        sepet[urun] += miktar
    else:
        sepet[urun] = miktar

print("\n--- FİŞ ---")
toplam = 0

for urun, miktar in sepet.items():
    tutar = urunler[urun] * miktar
    toplam += tutar
    print(f"{urun} x {miktar} = {tutar} TL")

print("Genel Toplam:", toplam, "TL")
