# soal no 1
def celcius_ke_fahrenheit(celcius):
  fahrenheit = (celcius * 9/5) + 32
  return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# soal no 2
def is_genap(bilangan):
  return bilangan % 2 == 0

print(is_genap(4))
print(is_genap(7))

# soal no 3
def nilai(n):
  if n >= 70:
    return "lulus"
  else:
    return "gagal"
  
print(nilai(80))
print(nilai(60))

# soal no 4
def bilangan(n):
  for i in range(1, n, 2):
    print(i, end=" ")

bilangan(20)