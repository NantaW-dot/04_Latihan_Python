import site
import sqlite3
import modul_luas
import modul_bilangan

def setup_database():
    """Fungsi untuk membuat database dan tabel jika belum ada."""
    conn = sqlite3.connect('data_pengguna.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def sistem_login(conn):
    """Fungsi untuk menangani proses login dan registrasi."""
    cursor = conn.cursor()
    
    while True:
        print("\n=======================")
        print("     SISTEM LOGIN      ")
        print("=======================")
        print("1. Login")
        print("2. Daftar Akun Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            
            if user:
                print(f"\nLogin berhasil! Selamat datang, {username}.")
                return True 
            else:
                print("\n[!] Username atau password salah. Silakan coba lagi.")
                
        elif pilihan == '2':
            username = input("Buat Username: ")
            password = input("Buat Password: ")
            
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                print("\n[V] Registrasi berhasil! Silakan login menggunakan akun tersebut.")
            except sqlite3.IntegrityError:
                print("\n[!] Username sudah digunakan. Silakan pilih username lain.")
                
        elif pilihan == '3':
            print("Program dihentikan.")
            return False
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def main():
    while True:
        print("\n=======================")
        print("      MENU UTAMA       ")
        print("=======================")
        print("1. Hitung Luas Bangun Datar")
        print("2. Cek Bilangan (Ganjil/Genap & Prima)")
        print("3. Keluar dari Program")
        
        pilihan = input("Pilih program yang ingin dijalankan (1/2/3): ")
        
        if pilihan == '1':
            modul_luas.hitung_luas()
            print() 
        elif pilihan == '2':
            modul_bilangan.jalankan_cek_bilangan()
        elif pilihan == '3':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.\n")

if __name__ == "__main__":
    koneksi = setup_database()
    
    if sistem_login(koneksi):
        main()

    koneksi.close()
