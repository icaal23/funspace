#Hitung luas segitiga sederhana
def luas_segitiga():
    a = int (input("Masukkan alas segitiga : "))
    t = int (input("Masukkan tinggi segitiga : "))
    luas = a * t / 2
    print("Luas segitiga adalah : ", luas)
    luas_segitiga()

    #Hitung Luas Persegi Panjang
    def luas_persegi_panjang():
        p = int (input("Masukkan Panjang Persegi"))
        l = int (input("Masukkan Lebar Persegi"))

        luas = p * l
        print("Luas Persegi adalah: ", luas)
    luas_persegi_panjang()