import tkinter as tk
from tkinter import messagebox
import sqlite3
import modul_bilangan

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Penghitung Matematika")
        self.root.geometry("420x480")
        
        self.bg_color = "#e6f2ff"  
        self.root.configure(bg=self.bg_color)
        
        init_db()
        self.tampilkan_menu_login()

    def bersihkan_jendela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tampilkan_menu_login(self):
        self.bersihkan_jendela()
        
        # Judul baru
        tk.Label(
            self.root, 
            text="Selamat Datang di Website\nPenghitung Matematika", 
            font=("Arial", 14, "bold"), 
            bg=self.bg_color,
            justify="center"
        ).pack(pady=20)

        tk.Label(self.root, text="Username:", bg=self.bg_color).pack()
        self.ent_username = tk.Entry(self.root, width=30)
        self.ent_username.pack(pady=5)

        tk.Label(self.root, text="Password:", bg=self.bg_color).pack()
        self.ent_password = tk.Entry(self.root, width=30, show="*")
        self.ent_password.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.proses_login, width=15, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Daftar Akun Baru", command=self.proses_daftar, width=15).pack()

    def proses_login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Berhasil", f"Selamat datang, {username}!")
            self.tampilkan_menu_utama()
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

    def proses_daftar(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!")
            return

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Berhasil", "Registrasi Berhasil! Silakan klik Login.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Gagal", "Username sudah terdaftar!")
        finally:
            conn.close()

    def tampilkan_menu_utama(self):
        self.bersihkan_jendela()
        
        tk.Label(self.root, text="MENU UTAMA", font=("Arial", 16, "bold"), bg=self.bg_color).pack(pady=20)

        tk.Button(self.root, text="Hitung Luas Bangun Datar", command=self.tampilkan_gui_luas, width=25, height=2).pack(pady=10)
        tk.Button(self.root, text="Cek Bilangan (Ganjil/Prima)", command=self.tampilkan_gui_bilangan, width=25, height=2).pack(pady=10)
        
        tk.Button(self.root, text="Logout", command=self.tampilkan_menu_login, width=15, bg="#f44336", fg="white").pack(pady=30)

    def tampilkan_gui_luas(self):
        self.bersihkan_jendela()
        
        tk.Label(self.root, text="HITUNG LUAS BANGUN DATAR", font=("Arial", 14, "bold"), bg=self.bg_color).pack(pady=15)

        self.pilihan_bangun = tk.StringVar(value="Persegi Panjang")
        
        frame_radio = tk.Frame(self.root, bg=self.bg_color)
        frame_radio.pack()
        tk.Radiobutton(frame_radio, text="Persegi Panjang", variable=self.pilihan_bangun, value="Persegi Panjang", command=self.update_form_luas, bg=self.bg_color).pack(side="left")
        tk.Radiobutton(frame_radio, text="Persegi", variable=self.pilihan_bangun, value="Persegi", command=self.update_form_luas, bg=self.bg_color).pack(side="left")

        self.frame_input = tk.Frame(self.root, bg=self.bg_color)
        self.frame_input.pack(pady=15)

        self.lbl_1 = tk.Label(self.frame_input, text="Panjang:", bg=self.bg_color)
        self.lbl_1.grid(row=0, column=0, padx=5, pady=5)
        self.ent_1 = tk.Entry(self.frame_input, width=15)
        self.ent_1.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_2 = tk.Label(self.frame_input, text="Lebar:", bg=self.bg_color)
        self.lbl_2.grid(row=1, column=0, padx=5, pady=5)
        self.ent_2 = tk.Entry(self.frame_input, width=15)
        self.ent_2.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Hitung Luas", command=self.proses_hitung_luas, bg="#2196F3", fg="white").pack(pady=10)
        
        self.lbl_hasil_luas = tk.Label(self.root, text="Hasil: -", font=("Arial", 12, "bold"), bg=self.bg_color)
        self.lbl_hasil_luas.pack(pady=10)

        tk.Button(self.root, text="Kembali ke Menu Utama", command=self.tampilkan_menu_utama).pack(pady=10)

    def update_form_luas(self):
        if self.pilihan_bangun.get() == "Persegi":
            self.lbl_1.config(text="Sisi:")
            self.lbl_2.grid_remove()
            self.ent_2.grid_remove()
        else:
            self.lbl_1.config(text="Panjang:")
            self.lbl_2.grid(row=1, column=0, padx=5, pady=5)
            self.ent_2.grid(row=1, column=1, padx=5, pady=5)

    def proses_hitung_luas(self):
        try:
            val1 = float(self.ent_1.get())
            if self.pilihan_bangun.get() == "Persegi":
                hasil = val1 * val1
                self.lbl_hasil_luas.config(text=f"Hasil Luas Persegi: {hasil}")
            else:
                val2 = float(self.ent_2.get())
                hasil = val1 * val2
                self.lbl_hasil_luas.config(text=f"Hasil Luas Persegi Panjang: {hasil}")
        except ValueError:
            messagebox.showerror("Error Input", "Masukkan angka yang valid!")

    def tampilkan_gui_bilangan(self):
        self.bersihkan_jendela()
        
        tk.Label(self.root, text="CEK GANJIL / GENAP & PRIMA", font=("Arial", 14, "bold"), bg=self.bg_color).pack(pady=15)

        tk.Label(self.root, text="Masukkan Angka:", bg=self.bg_color).pack(pady=5)
        self.ent_bilangan = tk.Entry(self.root, width=20)
        self.ent_bilangan.pack(pady=5)

        tk.Button(self.root, text="Cek Angka", command=self.proses_cek_bilangan, bg="#2196F3", fg="white").pack(pady=10)

        self.lbl_hasil_ganjil = tk.Label(self.root, text="", font=("Arial", 11), bg=self.bg_color)
        self.lbl_hasil_ganjil.pack(pady=5)

        self.lbl_hasil_prima = tk.Label(self.root, text="", font=("Arial", 11), bg=self.bg_color)
        self.lbl_hasil_prima.pack(pady=5)

        tk.Button(self.root, text="Kembali ke Menu Utama", command=self.tampilkan_menu_utama).pack(pady=20)

    def proses_cek_bilangan(self):
        try:
            angka = int(self.ent_bilangan.get())
            
            res_ganjil = modul_bilangan.cek_bilangan(angka)
            is_prima = modul_bilangan.cek_prima(angka)
            
            res_prima = f"{angka} Adalah Bilangan Prima." if is_prima else f"{angka} Bukan Bilangan Prima."
            
            self.lbl_hasil_ganjil.config(text=res_ganjil)
            self.lbl_hasil_prima.config(text=res_prima)
        except ValueError:
            messagebox.showerror("Error Input", "Masukkan bilangan bulat yang valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
