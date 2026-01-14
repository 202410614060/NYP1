ogrenciler = ["Ahmet", "Veli", "Ayşe", "Fatma", "Mehmet", "Sema"]

a_ile_bitenler = []
dortten_uzunlar = []

for ogrenci in ogrenciler:
    if ogrenci.lower().endswith("a"):
        a_ile_bitenler.append(ogrenci)
    if len(ogrenci) > 4:
        dortten_uzunlar.append(ogrenci)

print("A harfi ile bitenler:", a_ile_bitenler)
print("4 harften uzun olanlar:", dortten_uzunlar)
