import os

# log_fonksiyonlar.py'nin bulunduğu klasör
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# sonuclar klasörünün tam yolu
SONUCLAR_DIR = os.path.join(BASE_DIR, "sonuclar")


def dosyayi_oku(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        return dosya.readlines()


def istatistikleri_goster(dosya_adi):
    toplam = 0
    info = 0
    warning = 0
    error = 0

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            toplam += 1
            if "INFO" in satir:
                info += 1
            elif "WARNING" in satir:
                warning += 1
            elif "ERROR" in satir:
                error += 1

    print("=== LOG İSTATİSTİKLERİ ===")
    print(f"Toplam satır: {toplam}")
    print(f"INFO: {info} adet")
    print(f"WARNING: {warning} adet")
    print(f"ERROR: {error} adet")


def loglari_ayir(dosya_adi):
    # sonuclar klasörü yoksa oluştur (MUTLAK YOL)
    if not os.path.exists(SONUCLAR_DIR):
        os.mkdir(SONUCLAR_DIR)

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()

    with open(os.path.join(SONUCLAR_DIR, "info.log"), "w", encoding="utf-8") as info_dosya, \
         open(os.path.join(SONUCLAR_DIR, "warning.log"), "w", encoding="utf-8") as warning_dosya, \
         open(os.path.join(SONUCLAR_DIR, "error.log"), "w", encoding="utf-8") as error_dosya:

        for satir in satirlar:
            if "INFO" in satir:
                info_dosya.write(satir)
            elif "WARNING" in satir:
                warning_dosya.write(satir)
            elif "ERROR" in satir:
                error_dosya.write(satir)


def gun_filtrele(dosya_adi, hedef_gun):
    bulunan = 0
    print(f"=== {hedef_gun} GÜNÜNE AİT LOGLAR ===")

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            if satir.startswith(f"[{hedef_gun}"):
                print(satir.strip())
                bulunan += 1

    print(f"\nToplam {bulunan} log bulundu.")
