print("SELAMAT DATANG DI DATABASE MAHASISWA !!")
print("-"*60)

x = "iya"
listdata = []

while x == "iya":
     print()
     kode = input("Kode : ")
     nama = input("Nama : ")
     fakultas = input("Fakultas : ")
     prodi = input("Prodi : ")

     data_mahasiswa = {
         'kode' : kode,
         'nama' : nama,
         'fakultas' : fakultas,
         'prodi' : prodi
     }
     listdata.append(data_mahasiswa)
     print()
     x = input(f"Bersediakah anda mengisi data lagi (iya/tidak) ? : \n")
     if x == "iya":
         continue
     else:
         break
print(f"{'Kode' : <10} {'Nama' : <10} {'Fakultas' : <10} {'Prodi' : <10}")
print("-"*60)

for database in listdata:
     KODE = database['kode']
     NAMA = database['nama']
     FAKULTAS = database['fakultas']
     PRODI = database['prodi']
     print(f"{KODE:<10} {NAMA:<10} {FAKULTAS:<10} {PRODI:<10} \n")


print("Terimakasih atas waktunya !!")


