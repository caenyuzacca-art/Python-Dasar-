import tkinter as tk

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        masuk = int(entry_masuk.get())
        keluar = int(entry_keluar.get())
        lama = keluar - masuk

        if lama < 0:
            label_biaya.config(text="Biaya: Error")
        else:
            total = lama * BIAYA_PER_JAM
            label_biaya.config(text=f"Biaya: Rp.{total}")
    except:
        label_biaya.config(text="Biaya: Error")

root = tk.Tk()
root.title("Aplikasi Parkir")

# Input
tk.Label(root, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(root)
entry_plat.grid(row=0, column=1)

tk.Label(root, text="Waktu Masuk (jam)").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(root)
entry_masuk.grid(row=1, column=1)

tk.Label(root, text="Waktu Keluar (jam)").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(root)
entry_keluar.grid(row=2, column=1)

# Button
tk.Button(root, text="Hitung Biaya", command=hitung_biaya).grid(row=3, column=1, pady=5)

# Output
label_biaya = tk.Label(root, text="Biaya: Rp.0")
label_biaya.grid(row=4, column=1)

# Info biaya
tk.Label(root, text="Biaya Per Jam").grid(row=0, column=2, padx=20)
tk.Label(root, text="Rp. 2.000", fg="red", font=("Arial", 16, "bold")).grid(row=1, column=2, rowspan=2)

root.mainloop()
