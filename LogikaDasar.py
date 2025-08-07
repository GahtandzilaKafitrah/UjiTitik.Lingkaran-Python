# Header
print("SELAMAT DATANG DI LOGIKA DASAR MATEMATIKA")
print("oleh Gahtandzila Kafitrah")
print("-" * 60)
print()

# Peringatan
while True:
    print("MOHON DIBACA INFORMASI DI BAWAH INI !")
    print("Gunakan opsi jawaban sesuai perintah pada setiap kalimat yang ada\n jika MENGGUNAKAN HURUF TERTENTU MAKA HARUS DIIKUTI \n jika tidak diikuti maka akan ada peringatan !")
    p = input("Apakah anda sudah membaca peringatan tadi ?\n (sudah/belum)\n")
    if p == "sudah":
        break
    else: continue
print()

# User Input
def userinput():
    a = input("Pernyataan P (B/S) : ")
    b = input("Operator logika (^/v/->/<->) : ")
    c = input("Pernyataan Q (B/S) : ")
    print(f"{'P' : <10} {'Q' : <10} {'Operator' : <10} {'Nilai' : <10}")
    print("-" * 60)
    if a == "B" and b == "^"and c == "B":
        print(f"{'B' : <10} {'B' : <10} {'^' :<10} {'Benar' : <10}")
    elif a == "B" and b == "^" and c == "S":
        print(f"{'B' : <10} {'S' : <10} {'^' : <10} {'Salah' : <10}")
    elif a == "S" and b == "^" and c == "B":
        print(f"{'S' : <10} {'B' : <10} {'^' : <10} {'Salah' : <10}")
    elif a == "S" and b == "^" and c == "S":
        print(f"{'S' : <10} {'S' : <10} {'^' : <10} {'Salah'}")
    elif a == "B" and b == "v" and c == "B":
        print(f"{'B' : <10} {'B' : <10} {'v' : <10} {'Benar' : <10}")
    elif a == "B" and b == "v" and c == "S":
        print(f"{'B' : <10} {'S' : <10} {'v' : <10} {'Benar' : <10}")
    elif a == "S" and b == "v" and c == "B":
        print(f"{'S' : <10} {'B' : <10} {'v' : <10} {'Benar' : <10}")
    elif a == "S" and b == "v" and c == "S":
        print(f"{'S' : <10} {'S' : <10} {'v' : <10} {'Salah' : <10}")
    elif a == "B" and b == "->" and c == "B":
        print(f"{'B' : <10} {'B' : <10} {'->' : <10} {'Benar' : <10}")
    elif a == "B" and b == "->" and c =="S":
        print(f"{'B' : <10} {'S' : <10} {'->' : <10} {'Salah' : <10}")
    elif a == "S" and b == "->" and c == "B":
        print(f"{'S' : <10} {'B' : <10} {'->' : <10} {'Benar' : <10}")
    elif a == "S" and b == "->" and c == "S":
        print(f"{'S' : <10} {'S' : <10} {'->' : <10} {'Benar' : <10}")
    elif a == "B" and b == "-->" and c == "B":
        print(f"{'B' : <10} {'B' : <10} {'<->' : <10} {'Benar' : <10}")
    elif a == "B" and b =="-->" and c == "S":
        print(f"{'B' : <10} {'S' : <10} {'<->' : <10} {'Salah' : <10}")
    elif a == "S" and b == "-->" and c == "B":
        print(f"{'S' : <10} {'B' : <10} {'<->' : <10} {'Salah' : <10}")
    elif a == "S" and b == "-->" and c == "S":
        print(f"{'S' : <10} {'S' : <10} {'<->' : <10} {'Benar' : <10}")
    else:
        print("Mohon Masukkan sesuai perintah !!!\n")



# Loop Sistem
x = "iya"
while x == "iya" :
    userinput()
    while True:
       x = input("Ingin mencari tabel kebenaran lagi (iya/tidak) ? : \n")

       if x == "iya":
           break
       elif x == "tidak":
           break
       else:
           print("Mohon Masukkan sesuai perintah !!\n")
           continue


#Penutup Program
print("Baiklah, sampai bertemu kembali !!")






