import os
from log_fonksiyonlar import (
    dosyayi_oku,
    istatistikleri_goster,
    loglari_ayir,
    gun_filtrele
)

# main.py'nin bulunduğu klasörün yolu
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# log.txt dosyasının tam yolu
dosya_adi = os.path.join(BASE_DIR, "log.txt")


def menu_goster():
    print("\n=== LOG ANALİZ SİSTEMİ ===")
    print("1 - Log dosyasını oku")
    print("2 - Log istatistiklerini göster")
    print("3 - Logları türlerine göre ayır")
    print("4 - Belirli bir güne ait logları göster")
    print("5 - Çıkış")


def main():
    while True:
        menu_goster()
        secim = input("Seçiminizi girin (1-5): ")

        if secim == "1":
            satirlar = dosyayi_oku(dosya_adi)
            print("\n--- LOG KAYITLARI ---")
            for satir in satirlar:
                print(satir)

        elif secim == "2":
            print()
            istatistikleri_goster(dosya_adi)

        elif secim == "3":
            loglari_ayir(dosya_adi)
            print("\nLoglar başarıyla 'sonuclar' klasörüne ayrıldı.")

        elif secim == "4":
            tarih = input("Filtrelenecek tarihi girin (YYYY-AA-GG): ")
            print()
            gun_filtrele(dosya_adi, tarih)

        elif secim == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Hatalı seçim! Lütfen 1-5 arasında bir değer girin.")


if __name__ == "__main__":
    main()


