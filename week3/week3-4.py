sayi = int(input("Bir sayı girin:"))

faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i

print("Faktöriyel:", faktoriyel)
