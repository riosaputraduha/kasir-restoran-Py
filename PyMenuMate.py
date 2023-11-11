print("-------------------- PROGRAM KASIR SEDERHANA PYMENUMATE --------------------")

pembeli = input("Masukkan Nama Pelanggan : ")
print('\n')
print("Nama Pelanggan :", pembeli)

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    print("\n-------------------- Menu Makanan --------------------")
    print("1. Nasi Goreng - Rp 25000")
    nomor = int(input("Masukkan No. Pilihan : "))
    porsi = int(input("Berapa Porsi : "))
    
    if nomor == 1:
        totalmkn = porsi*25000
        print(porsi," porsi Nasi Goreng = Rp", totalmkn)
        mkn = ("Nasi Goreng")
    else:
        print("Pilihan tidak ada, silakan masukkan lagi!")
        fungsimakanan()

def fungsiminuman():
    global totalmnm
    global mnm
    global gelas
    print("\n-------------------- Menu Minuman --------------------")
    print("1. Es Teh - Rp 5000")
    nomor = int(input("Masukkan Pilihan : "))
    gelas = int(input("Berapa Gelas : "))
    
    if nomor == 1:
        totalmnm = gelas*5000
        print(gelas," gelas Es Teh = Rp", totalmnm)
        mnm = ("Es Teh")
    else:
        print("Pilihan tidak ada, silakan masukkan lagi!")
        fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua = totalmkn+totalmnm


