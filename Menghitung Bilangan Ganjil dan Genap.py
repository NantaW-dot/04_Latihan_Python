def cek_bilangan(angka):
    """Fungsi untuk menentukan apakah bilangan ganjil atau genap."""
    if angka % 2 == 0:
        return f"{angka} Adalah Bilangan Genap."
    else:
        return f"{angka} Adalah Bilangan Ganjil."

def main():
    """Fungsi utama untuk menjalankan perulangan dan menerima input pengguna."""
    print("Ketik 'keluar' untuk menghentikan program.")

    while True:
        user_input = input("Masukkan Sebuah Bilangan (atau ketik 'keluar'): ")

        if user_input.lower() == "keluar":
            print("Program berhenti. Terima kasih!")
            break

        if user_input.isdigit():
            angka = int(user_input)
            
            hasil = cek_bilangan(angka)
            print(hasil + "\n")
            
        else:
            print("Input tidak valid. Masukkan angka yang benar atau 'keluar'.\n")

if __name__ == "__main__":
    main()
