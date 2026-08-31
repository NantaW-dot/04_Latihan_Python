print("Pilih bangun datar yang ingin dihitung:")
print("1. Persegi Panjang")
print("2. Persegi")

pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == '1':
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas Persegi Panjang adalah: {luas}")
    
elif pilihan == '2':
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    print(f"Luas Persegi adalah: {luas}")
    
else:
    print("Pilihan tidak valid. Silakan jalankan ulang program dan pilih 1 atau 2.")
