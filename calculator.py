def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("Yapılacak işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminiz (1/2/3/4): ")

    sayi1 = int(input("İlk sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    if secim == '1':
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

    elif secim == '2':
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)

    elif secim == '3':
        print(sayi1, "*", sayi2, "=", sayi1 * sayi2)

    elif secim == '4':
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)

    else:
        print("Geçersiz seçim")

hesap_makinesi()
