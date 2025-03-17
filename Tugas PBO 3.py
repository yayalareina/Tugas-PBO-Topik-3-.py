class Sepeda:
    def __init__ (self, merk, warna, harga):
        self.__merk = merk       # Private property
        self.warna = warna       # Public property
        self.__harga = harga     # Private property
        self.kecepatan = 0       # Public property

    # Getter untuk merk
    def get_merk(self):
        return self.__merk

    # Setter untuk merk
    def set_merk(self, merk_baru):
        self.__merk = merk_baru

    # Getter untuk harga
    def get_harga(self):
        return self.__harga

    # Setter untuk harga
    def set_harga(self, harga_baru):
        self.__harga = harga_baru

    # Method untuk mengayuh sepeda
    def kayuh(self, kecepatan):
        self.kecepatan += kecepatan
        print("Sepeda melaju dengan kecepatan", self.kecepatan, "km/jam")

    # Method untuk mengerem
    def rem(self):
        self.kecepatan = 0
        print("Sepeda berhenti")

    # Method untuk membelokkan sepeda
    def belok(self, arah):
        print("Sepeda belok ke", arah)

# Membuat objek Sepeda
sepeda_baru = Sepeda("Wimcycle", "Biru", 3000000)

# Mengakses atribut private menggunakan getter
print("Sebelum perubahan:")
print("Merk:", sepeda_baru.get_merk())
print("Harga: Rp", sepeda_baru.get_harga())

# Mengubah atribut private menggunakan setter
sepeda_baru.set_merk("United")
sepeda_baru.set_harga(3500000)

# Menampilkan informasi setelah perubahan
print("\nSetelah perubahan:")
print("Merk:", sepeda_baru.get_merk())
print("Harga: Rp", sepeda_baru.get_harga())

# Menggunakan method sepeda
sepeda_baru.kayuh(15)
sepeda_baru.belok("kanan")
sepeda_baru.kayuh(10)
sepeda_baru.rem()
