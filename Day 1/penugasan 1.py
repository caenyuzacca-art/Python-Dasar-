# Persegi
sisi = float(input("Masukkan sisi persegi: "))
luas_persegi = sisi * sisi
keliling_persegi = 4 * sisi

print("Luas Persegi =", luas_persegi)
print("Keliling Persegi =", keliling_persegi)

# Persegi Panjang
panjang = float(input("\nMasukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas_pp = panjang * lebar
keliling_pp = 2 * (panjang + lebar)

print("Luas Persegi Panjang =", luas_pp)
print("Keliling Persegi Panjang =", keliling_pp)

# Trapesium
a = float(input("\nMasukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
t = float(input("Masukkan tinggi: "))
c = float(input("Masukkan sisi miring kiri: "))
d = float(input("Masukkan sisi miring kanan: "))

luas_trapesium = 0.5 * (a + b) * t
keliling_trapesium = a + b + c + d

print("Luas Trapesium =", luas_trapesium)
print("Keliling Trapesium =", keliling_trapesium)