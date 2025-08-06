x = int(input("Masukkan angka ke-1 : "))
y = int(input("Masukkan angka ke-2 : "))


def operasi(a,b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah,kurang,kali,bagi

p,q,r,z = operasi(x,y)

print(f"Hasil tambah nya adalah {p}")
print(f"Hasil kurang nya adalah {q}")
print(f"Hasil kali nya adalah {r}")
print(f"Hasil bagi nya adalah {z}")


