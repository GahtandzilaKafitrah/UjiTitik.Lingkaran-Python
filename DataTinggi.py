# HEADER
print()
print("SELAMAT DATANG DI PERHITUNGAN DATA TINGGI BADAN !\n by Gahtandzila Kafitrah")
print("-"*60)

# LOOP SISTEM UTAMA
p = "iya"
while p == "iya":
   # USER INPUT TINGGI BADAN
   a = float(input("Tinggi badan ke-1 (cm) : "))
   b = float(input("Tinggi badan ke-2 (cm): "))
   c = float(input("Tinggi badan ke-3 (cm): "))
   d = float(input("Tinggi badan ke-4 (cm): "))
   e = float(input("Tinggi badan ke-5 (cm): "))

   print()

   data_tinggi = [a,b,c,d,e]

   # TABEL
   print(f"{'Tertinggi (max) //' : <10} {'Terendah (min) //' : <10} {'Rata-rata(mean) //' : <10} {'Standar Deviasi' :<10}")
   print("-"*80)

   # PERHITUNGAN STATISTIKA DESKRIPTIF (MIN, MAX, MEAN, STANDAR DEVIASI)
   minimal = min(data_tinggi)
   maksimal = max(data_tinggi)
   rata = (a+b+c+d+e)/5
   std = (((a-rata)**2 + (b-rata)**2 + (c-rata)**2 + (d-rata)**2 + (e-rata)**2)/4 )**0.5

   # OUTPUT PERHITUNGAN
   print(f"{maksimal : <20}{minimal : <18}{rata : <20}{std : <20}")
   print()

   # PERINGATAN PENGULANGAN PERINTAH
   while True :
      p = input("Ingin input data lagi (iya/tidak) ? : \n")

      if p == "iya":
          break
      elif p == "tidak":
          break
      else:
          print("Mohon masukkan sesuai perintah !\n")
          continue

# PENUTUP SISTEM
print("Terimakasih dan sampai jumpa kembali !")


