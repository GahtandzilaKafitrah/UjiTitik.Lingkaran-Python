# Header Kalkulator
print()
print("KALKULATOR SEDERHANA\n oleh Gahtandzila Kafitrah")
print("-"*60)
print()

# Input User
x = "iya"
while x == "iya":
    while True:
     a = float(input("Masukkan angka ke-1 : "))
     b = input("Masukkan operator(+/-/x/:) : ")
     c = float(input("Masukkan angka ke-2 : "))

     # OPERASI KALKULATOR
     if b == "+":
         tambah = a+c
         print(f"Maka hasil dari {a} {b} {c} = {tambah}\n")
         break
     elif b == "-":
         kurang = a-c
         print(f"Maka hasil dari {a}{b}{c} = {kurang}\n")
         break
     elif b == "x" or b == "*":
         kali = a*c
         print(f"Maka hasil dari {a}{b}{c} = {kali}\n")
         break
     elif b == "/" or b == ":":
         bagi = a/c
         print(f"Maka hasil dari {a}{b}{c} = {bagi}\n")
         break
     else:
         print("Masukkan sesuai perintah !\n")
         continue

    # LOOP PERINGATAN
    while True :
       x = input("Apakah mau menghitung lagi (iya/tidak) : \n")
       if x == "iya":
           break
       elif x == "tidak":
           break
       else:
           print("Harap Masukkan Sesuai Perintah !")
           continue

# PENUTUP SISTEM
print("Baiklah, sampai jumpa kembali !")