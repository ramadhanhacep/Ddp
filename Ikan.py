from Animal import Animal

class Ikan(Animal):
  def __init__(self, nama, makanan, hidup, berkembang_biak, kecepatan_berenang, warna_ikan):
    super().__init__(nama, makanan, hidup, berkembang_biak)
    self.kecepatan_berenang = kecepatan_berenang
    self.warna_ikan = warna_ikan

  def info_ikan(self):
    super().info_animal()
    print("Kecepatan Berenang : ", self.kecepatan_berenang,
          "\nWarna Ikan \t : ", self.warna_ikan)
    

ikan_hiu = Ikan("Hiu", "Daging/Ikan kecil", "Laut", "Ber-anak", "Cepat" ,"Abu abu")
ikan_hiu.info_ikan()
print("==============================================================")
ikan_lele = Ikan("Lele", "Kotoran", "Sungai/Danau", "Ber-anak", "Lambat", "Hitam")
ikan_lele.info_ikan()
print("==============================================================")