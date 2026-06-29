def hesap_makinesi():
    print("-" * 30)
    print(" Basit Hesap Makinesi (Gelişmiş)")
    print("-" * 30)
    
    while True:
        print("\nYapılacak işlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")

        secim = input("\nSeçiminiz (1/2/3/4/5): ")

        if secim == '5':
            print("Hesap makinesinden çıkılıyor... İyi günler!")
            break

        if secim not in ('1', '2', '3', '4'):
            print("❌ Hata: Geçersiz seçim. Lütfen 1 ile 5 arasında bir değer girin.")
            continue

        try:
            sayi1 = float(input("İlk sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("❌ Hata: Lütfen geçerli bir sayı girin!")
            continue

        if secim == '1':
            print(f"✅ Sonuç: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        elif secim == '2':
            print(f"✅ Sonuç: {sayi1} - {sayi2} = {sayi1 - sayi2}")
        elif secim == '3':
            print(f"✅ Sonuç: {sayi1} * {sayi2} = {sayi1 * sayi2}")
        elif secim == '4':
            if sayi2 == 0:
                print("❌ Hata: Bir sayı sıfıra (0) bölünemez!")
            else:
                print(f"✅ Sonuç: {sayi1} / {sayi2} = {sayi1 / sayi2}")

if __name__ == "__main__":
    hesap_makinesi()
