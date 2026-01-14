veriler = [12, 45, 23, 67, 34, 89, 12, 45, 67]

# Tekrar edenleri temizleme
temiz_liste = []
for eleman in veriler:
    if eleman not in temiz_liste:
        temiz_liste.append(eleman)

# Büyükten küçüğe sıralama
temiz_liste.sort(reverse=True)

print("Tekrarsız ve sıralı liste:", temiz_liste)
