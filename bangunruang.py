import math

def luas_balok(p, l, t):
  hitung = 2 * (p*l)+(p*t)+(l*t)
  print(f'Luas Balok Adalah {hitung}')

def luas_kubus(sisi):
  hitung = 6 * (sisi * sisi)
  print(f'Luas kubus adalah {hitung}')

def luas_tabung(r2, t):
  hitung = 6 * (r2 + t)
  print(f'Luas Tabung adalah {hitung}')

def luas_limas(a, st):
  hitung = math.sqrt(3) * a * st
  print(f'Luas Limas adalah {hitung}')

def luas_prisma(alas, tinggi):
  hitung = 1/2 * alas * tinggi
  print(f'Luas prisma adalah {hitung}')