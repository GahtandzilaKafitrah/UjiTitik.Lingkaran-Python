
p = "iya"
# LOOP SISTEM UTAMA
while p == "iya":

    # LOOP SISTEM JIKA TIDAK MEMENUHI SYARAT
    while True:
     x = input("Anda mau cari segitiga apa (siku-siku/sama sisi) ? : \n")
     if x == "siku-siku":
          a = int(input("Masukkan Tinggi Segitiga : "))

          for i in range(1,a+1):
              print("*" * i)

          print(f"Maka alas segitiga siku-siku nya adalah {a}")
          luas_siku = 0.5*a*a
          print(f"Karena itu, luasnya adalah {luas_siku}\n")
          break
     elif x == "sama sisi":
          b =int(input("Masukkan Tinggi Segitiga : "))
          for i in range(0,b):
              spasi = " "*(b-i)
              tinggi = "*"* ((2*i)+1)
              print(spasi + tinggi)

          alas = 1 + ((b-1)*2)
          print(f"Maka alas segitiganya adalah = {alas}")
          luas = 0.5*b*alas
          print(f"Karena itu, luasnya adalah = {luas}")
          break
     else:
         print("Pilihan kami hanya (siku-siku/sama sisi) !!\n")
         continue

    # PERTANYAAN UNTUK KE SISTEM UTAMA ATAU TIDAK
    p = input("Apakah ingin mencari nilai yang lain ? (iya/tidak)\n")


# LUAR LOOP SISTEM UTAMA BERUPA PENUTUP
print("Terimakasih telah mencoba !")