from Animal import Animal

class Burung(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.paruh = paruh
    self.warna_bulu = warna_bulu

  def info_burung(self):
    super().info_animal()
    print("Paruh \t\t : ", self.paruh,
          "\nWarna Bulu \t : ", self.warna_bulu)
    

burung_beo = Burung("Beo", "Jagung", "Darat", "Berterlur", "Melengkung", "Warna warni")
burung_beo.info_burung()
print("==============================================================")
burung_merpati = Burung("Merpati", "Jagung", "Darat", "Bertelur", "Lurus", "Putih")
burung_merpati.info_burung()
print("==============================================================")
burung_elang = Burung("Elang", "Tikus", "Darat", "Bertelur", "Melengkung", "Hitam Putih")
burung_elang.info_burung()
print("==============================================================")