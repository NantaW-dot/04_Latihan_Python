import modul_luas
import modul_bilangan

def main():
    while True:
        print("=======================")
        print("      MENU UTAMA       ")
        print("=======================")
        print("1. Hitung Luas Bangun Datar")
        print("2. Cek Bilangan (Ganjil/Genap & Prima)")
        print("3. Keluar dari Program")
        
        pilihan = input("Pilih program yang ingin dijalankan (1/2/3): ")
        
        if pilihan == '1':
            modul_luas.hitung_luas()
            print() # Memberi jarak baris setelah program selesai
        elif pilihan == '2':
            modul_bilangan.jalankan_cek_bilangan()
        elif pilihan == '3':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.\n")

if __name__ == "__main__":
    main()