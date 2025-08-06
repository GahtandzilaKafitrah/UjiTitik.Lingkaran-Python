# Fungsi Perhitungan Jarak
def hitung_jarak():
    kecepatan = int(input("Masukkan kecepatan rata-rata anda (m/s) : "))
    waktu = int(input("Masukkan waktu tempuh anda (s): "))
    hitungjarak = kecepatan*waktu
    print(f"Jarakmu terhadap tujuan adalah {hitungjarak} m\n")
    return hitungjarak

# Fungsi Perhitungan Kecepatan
def hitung_kecepatan():
    jarak = int(input("Masukkan jarak tempuh anda (m): "))
    waktu = int(input("Masukkan waktu tempuh anda (s): "))
    hitungkecepatan = jarak/waktu
    print(f"Kecepatanmu kamu bergerak adalah : {hitungkecepatan} m/s\n")
    return hitungkecepatan

# Fungsi Perhitungan Waktu
def hitung_waktu():
    jarak = int(input("Masukkan jarak tempuh anda (m): "))
    kecepatan = int(input("Masukkan kecepatan rata-rata anda (m/s): "))
    hitungwaktu = jarak/kecepatan
    print(f"Waktu tempuh mu adalah : {hitungwaktu} s\n")
    return hitungwaktu


# Program Utama
print(f"Perhitungan Fisika Gerak Lurus Beraturan")
print(f"Karya Gahtandzila Kafitrah")
print("-"*60)
y = "iya"
while y == "iya":
    y = "iya"
    while y == "iya":
       x = input("Anda ingin mencari apa? (Jarak/kecepatan/waktu)? : \n")
       if x == "jarak":
           hitung_jarak()
       elif x == "kecepatan":
           hitung_kecepatan()
       elif x == "waktu":
           hitung_waktu()
       else:
           print("Anda tidak sesuai dengan perintah !\n")
           continue
       while True:
          y = input("Ingin mencari yang lain (iya/tidak) ? : \n")
          if y == "iya":
              break
          elif y == "tidak":
              break
          else:
              print("Harap masukkan sesuai perintah !\n")
              continue

print("Program telah selesai, sampai bertemu kembali !")





