def yasHesapla(dogum_tarihi):
    # Bugünün yılı olan 2023'ten doğum tarihini çıkartarak yaş hesaplanır.
    yas = 2023 - dogum_tarihi
    print("Yasiniz : ", yas)


def emeklilikHesapla(dogum_tarihi, emeklilik_yasi):
    # Bugünün yılı olan 2023'ten doğum tarihini çıkartarak yaş hesaplanır.
    yas = 2023 - dogum_tarihi

    # Emeklilik yaşına kaç yıl kaldığını hesaplayın
    kalanYil = emeklilik_yasi - yas

    if emeklilik_yasi > yas:
        # Emeklilik yaşına daha fazla yıl varsa bu kısım çalışır.
        print("Emekli olmaniza", kalanYil, "yil kalmistir.")

    elif kalanYil == 0:
        # Eğer kalan yıl 0 ise bu sene emekli olduğunu belirtir.
        print("Bu sene emekli oldunuz")

    elif emeklilik_yasi < yas:
        # Emeklilik yaşınızı geçtiyseniz, kaç yıldır emekli olduğunuzu gösterir.
        emekli = yas - emeklilik_yasi
        print("Zaten", emekli, "yildir emeklisiniz")
