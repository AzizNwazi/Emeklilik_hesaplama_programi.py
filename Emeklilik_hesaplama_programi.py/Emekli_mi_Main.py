from Emekli_mi_modul import * #Modulumuzu Çağır

i = 1 # sayaç

while True:
    print("\n*********************************\n")
    print(i, ".Kullanici:")

    # Kullanıcıdan doğum tarihi ve emeklilik yaşını girmesini isteyelim
    dogum_tarihi = int(input("Dogum yili tarihinizi giriniz: "))
    emeklilik_yasi = int(input("Emeklilik yasinizi giriniz: "))

    # Emekli_mi_modul'den Kullanıcının yaşını hesaplayan fonksiyonu çağırın
    yasHesapla(dogum_tarihi)
    emeklilikHesapla(dogum_tarihi, emeklilik_yasi)

    i += 1
    if i >= 4: # 3 kullanicinin bilgilerini hesaplamak istediğimiz icin 4.ye gelince programı sonlandırsın
        print("\n\nDerleme tamamlandi...")
        break
