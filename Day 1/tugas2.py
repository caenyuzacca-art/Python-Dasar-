import math

print("=== MENGHITUNG VOLUME TABUNG ===")
r = float(input("Masukkan jari-jari tabung: "))
t_tabung = float(input("Masukkan tinggi tabung: "))

volume_tabung = math.pi * r * r * t_tabung
print("Volume Tabung =", volume_tabung)

print("\n=== MENGHITUNG VOLUME BALOK ===")
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t_balok = float(input("Masukkan tinggi balok: "))

volume_balok = p * l * t_balok
print("Volume Balok =", volume_balok)
