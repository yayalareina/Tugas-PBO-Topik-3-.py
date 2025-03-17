# Tugas-PBO-Topik-3-.py
Berdasarkan hasil program pada tugas class dan object

class sepeda:
    def __init__ (self, merk, warna, harga):
        self.merk = merk
        self.warna = warna
        self.harga = harga
        self.kecepatan = 0

    def kayuh(self, kecepatan):
        self.kecepatan += kecepatan
        print("sepeda melaju dengan kecepatan", self.kecepatan, "km/jam")

    def rem(self):
        self.kecepatan = 0
        print("sepeda berhenti")

    def belok(self, arah):
        print("sepeda belok ke", arah)

#Contoh penggunaan kelas Sepeda
sepeda_saya = sepeda("Polygon", "Merah", 5000000)

sepeda_saya.kayuh(20)
sepeda_saya.belok("kiri")
sepeda_saya.kayuh(10)
sepeda_saya.rem()

Buatlah :

1. Ubah 2 properties menjadi private

2. Buat method getter dan setter

3. Buat objek baru dan akses variabel private tersebut menggunakan method getter dan setter

4. Kumpulkan link github/replit
