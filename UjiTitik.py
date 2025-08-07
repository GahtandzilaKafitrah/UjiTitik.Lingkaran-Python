# Mulai LOOP UTAMA
p = "iya"
while p == "iya":

    # DATA LINGKARAN
    print("Masukkan data lingkaran di bawah !")
    a = float(input("Jari-jari lingkaran : "))
    b = float(input("Pusat lingkaran (titik x) : "))
    c = float(input("Pusat lingkaran (titik y) : "))
    print(f"Rumus lingkaran : (x-{b})^2 + (y-{c})^2 = {a**2}\n")

    print("Uji titik pada lingkaran")
    tanya = "iya"

    # LOOP UJI TITIK
    while tanya == "iya":

       # UJI TITIK
       x = float(input("Nilai x : "))
       y = float(input("Nilai y : "))
       print(f"Titik yang kamu input : ({x},{y})")
       hasil = (b-x)**2 + (c-y)**2
       if hasil == a**2:
           print(f"Titik ({x},{y}) terletak pada lingkaran")
       elif hasil < a**2:
           print(f"Titik ({x},{y}) terletak di dalam lingkaran")
       else:
           print(f"Titik ({x},{y}) terletak di luar lingkaran")

       # LOOP PERINGATAN UJI TITIK LAIN
       while True :
          tanya = input("Mau uji titik lain (iya/tidak) ? : \n")
          if tanya == "iya":
              break
          elif tanya == "tidak":
              break
          else:
              print("Harap masukkan sesuai perintah !\n")
              continue
    p = input("Mau ubah data lingkaran (iya/tidak) ? : ")

    # LOOP PERINGATAN UBAH DATA LINGKARAN
    while True:
       if p == "iya":
           break
       elif p == "tidak":
           break
       else:
           print("Harap masukkan sesuai perintah !")
           continue

# PENUTUP SISTEM
print("Terimakasih dan sampai jumpa kembali !")