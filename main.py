# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
z = int(input("Masukkan bilangan ketiga: "))

average = (x + y + z) / 3
print('Rata-rata bilangan adalah {0}, {1}, dan {2} adalah {3}'.format(
    x, y, z, average))

# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
angka = 5

while angka <= 25:
    print("Kelipatan angka 5 adalah")
    print(angka, sep="---", end="---")
    angka = angka + 5
