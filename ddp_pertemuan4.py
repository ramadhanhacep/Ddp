bilangan = int(input('masukan bilangan anda: '))

if bilangan % 2 == 0:
  print(bilangan, 'merupakan bilangan genap')
else:
  print(bilangan, 'merupakan bilangan ganjil')

#program menentukan nilai ujian
print('## 2, program menentukan nilai ujian ##')
print()
#input nilai
nilai_ujian = int(input('masukkan nilai ujian: '))
#proses input nilai
if nilai_ujian >= 75:
  print('kamu dinyatakan lulus')
else:
  print('kamu dinyatakan tidak lulus')

#input usia
usia = int(input('masukkan usia anda: '))

if usia >= 18:
  print('anda sudah dewasa')
elif usia >= 13 and usia <= 17:
  print('anda masih bocil')
else:
  print('anda masih anak-anak')
print()

#program menentukan ke anggotaan
print('## 3, program status menentukan keanggotaan')
print()

#proses status
status_anggota = input("""Daftar anggota dibawah ini
1.syadad
2.rifai
3.nauval
masukkan pilihan kamu: """)

#proses dan output
if status_anggota == 'syadad' or status_anggota == 'rifai':
  print('selamat anda telah bergabung')
elif status_anggota == 'nauval':
  print('selamat anda telah join dengan diskon')
else:
  print('masukan kata dengan benar')

#Pembelian Diskon
# Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. 
# Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
#example : minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000

#input
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))

#proses
diskon = 0.1 if jumlah_pembelian > 100 else 0
total_harga = jumlah_pembelian - (jumlah_pembelian * diskon)

#output
if diskon > 0:
    print(f"Total harga setelah diskon: (total_harga:.2f)")
else:
    print(f"Total harga tanpa diskon: (total_harga:.2f)")