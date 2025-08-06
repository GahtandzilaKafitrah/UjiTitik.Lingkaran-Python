a = int(input("Masukkan angka ke-1 : "))
b = int(input("Masukkan angka ke-2 : "))

def tambah(angka1,angka2):
    jumlah = angka1 + angka2
    print(f"Anda memasukan {angka1} dan {angka2} maka jika dijumlahkan akan menghasilkan {jumlah}")

tambah(a,b)

x = input("Masukkan nama ayah kamu : ")
y = input("Masukkan nama ibu kamu : ")
z = input("Masukkan nama kamu : ")
keluarga = [x,y,z]

def family(familymu):
    keluargamu = familymu.copy()
    for nama in keluargamu:
        print(nama)


family(keluarga)



