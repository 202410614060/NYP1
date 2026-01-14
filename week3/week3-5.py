import random
sayi = random.randint(1, 100)
print("1-100 arasında tutulan sayıyı tahmin edin.")

while True:
    tahmin = int(input("Tahmininiz:"))
    if tahmin < sayi:
        print("Daha büyük bir sayı")
    elif tahmin > sayi:
        print("Daha küçük bir sayı")
    else:
        print("Tahmininiz doğru.")
        break
    
