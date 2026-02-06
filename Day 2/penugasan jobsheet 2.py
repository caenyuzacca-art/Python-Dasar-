class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def info(self):
        print(self.nama, "kelas", self.kelas)

s1 = Siswa("Andi", "X RPL")
s1.info()
