print("Ketik 'keluar' untuk menghentikan program.")

while True:
  user_input = input("Masukkan angka (atau ketik 'keluar'): ")

  if user_input.lower() == "keluar":
    print("Program berhenti. Terima kasih!")
    break

  if user_input.isdigit():
    angka = int(user_input)

    for i in [angka]:
      if i % 2 == 0:
        print(f"Angka {i} adalah bilangan GENAP.\n")
      else:
        print(f"Angka {i} adalah bilangan GANJIL.\n")
  else:
    print("Input tidak valid. Masukkan angka yang benar atau 'keluar'.\n")