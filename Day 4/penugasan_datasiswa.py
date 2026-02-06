import tkinter as tk
from tkinter import messagebox

def simpan():
    data = {
        "Nama": entry_nama.get(),
        "Tanggal Lahir": entry_ttl.get(),
        "Asal Sekolah": entry_sekolah.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "No HP": entry_hp.get(),
        "Alamat": text_alamat.get("1.0", tk.END)
    }
    messagebox.showinfo("Simpan", "Data berhasil disimpan")

def hapus():
    entry_nama.delete(0, tk.END)
    entry_ttl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("MainWindow")
root.geometry("600x600")

# Judul
judul = tk.Label(root, text="DATA SISWA BARU",
                 bg="#9ee7ea", font=("Arial", 16, "bold"))
judul.pack(fill="x")

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(fill="both", expand=True)

def buat_label_entry(text):
    tk.Label(frame, text=text).pack(anchor="w")
    e = tk.Entry(frame, width=60)
    e.pack(pady=3)
    return e

entry_nama = buat_label_entry("Nama Lengkap")
entry_ttl = buat_label_entry("Tanggal Lahir")
entry_sekolah = buat_label_entry("Asal Sekolah")
entry_nisn = buat_label_entry("NISN")
entry_ayah = buat_label_entry("Nama Ayah")
entry_ibu = buat_label_entry("Nama Ibu")
entry_hp = buat_label_entry("Nomor Telepon / HP")

tk.Label(frame, text="Alamat").pack(anchor="w")
text_alamat = tk.Text(frame, height=4, width=60)
text_alamat.pack(pady=3)

# Tombol
btn_frame = tk.Frame(root, pady=10)
btn_frame.pack()

tk.Button(btn_frame, text="Hapus", width=10,
          bg="#c96b4b", fg="white", command=hapus).pack(side="left", padx=10)

tk.Button(btn_frame, text="Simpan", width=10,
          bg="#c96b4b", fg="white", command=simpan).pack(side="left", padx=10)

root.mainloop()
