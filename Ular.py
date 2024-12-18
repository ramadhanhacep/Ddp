from Animal import Animal

class Ular(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, Bisa, warna_ular):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.Bisa = Bisa
    self.warna_ular = warna_ular

  def info_ular(self):
    super().info_animal()
    print("Bisa \t\t : ", self.Bisa,
          "\nWarna Ular \t : ", self.warna_ular)
    
Ular_Cobra = Ular("Cobra", "Tikus", "Tanah/Semak semak", "Bertelur", "Mematikan", "Coklat,Kuning,Hijau,Dengan Bintik Hitam")
Ular_Cobra.info_ular()
print("==============================================================")
Ular_Weling = Ular("Weling", "Tikus", "Lubang Tikus/Sumber air", "Bertelur", "Menyebabkan Kejang kejang", "Hitam Putih")
Ular_Weling.info_ular()