matris_A = [[1, 2], [3, 4]]
matris_B = [[5, 6], [7, 8]]

# Matris toplaması
toplam = []
for i in range(2):
    satir = []
    for j in range(2):
        satir.append(matris_A[i][j] + matris_B[i][j])
    toplam.append(satir)

# Matris çarpımı
carpim = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            carpim[i][j] += matris_A[i][k] * matris_B[k][j]

# Matrisi düzleştirme
duz_liste = []
for satir in matris_A:
    for eleman in satir:
        duz_liste.append(eleman)

print("Matris Toplamı:", toplam)
print("Matris Çarpımı:", carpim)
print("Düzleştirilmiş Matris A:", duz_liste)
