organizasyon = input("Organizasyon adını girin: ")

kisalma = ""
for kelime in organizasyon.split():
    kisalma += kelime[0]

print("Kısaltma:", kisalma.upper())
