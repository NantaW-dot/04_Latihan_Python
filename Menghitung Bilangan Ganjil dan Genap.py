print("Ketik 'keluar' untuk menghentikan program.")

while True:
    user_input = input("Masukkan Sebuah Bilangan (atau ketik 'keluar'): ")

    if user_input.lower() == "keluar":
        print("Program berhenti. Terima kasih!")
        break

    if user_input.isdigit():
        angka = int(user_input)

        if angka % 2 == 0:
            print(f"{angka} Adalah Bilangan Genap.\n")
        else:
            print(f"{angka} Adalah Bilangan Ganjil.\n")
    else:
        print("Input tidak valid. Masukkan angka yang benar atau 'keluar'.\n")
