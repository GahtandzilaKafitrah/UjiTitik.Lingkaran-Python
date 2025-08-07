# dengan fungsi biasa
def pangkat6(angka):
    hasil = angka**6
    return hasil

pangkat_6 = pangkat6(2)
print(f"Menggunakan fungsi biasa = {pangkat_6}")

# dengan lambda
pangkat6 = lambda angka:angka**6
print(f"Menggunakan lambda = {pangkat6(2)}")

# dengan fungsi biasa
def pangkatbaru(a,b):
    hasilnya = a**b
    return hasilnya

coba1 = pangkatbaru(21,22)
print(f"Ini menggunakan fungsi biasa = {coba1}")

# dengan lambda
coba2 = lambda angka1,angka2:angka1**angka2
print(f"Menggunakan lambda = {coba2(21,22)}")