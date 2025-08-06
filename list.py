# Belajar list

list_data = []
x = "iya"
while x == "iya":
    print()
    nama = input("Nama : ")
    print()
    makanan = input("Makanan Kesukaan : ")
    print()
    hobby = input("Hobby  : ")
    data_user = [nama, makanan, hobby]
    list_data.append(data_user)
    print()
    print("Data Update !!")
    for index,data in enumerate(list_data):
        print(str(index+1) + " // " + str(data[0]) + " // " + str(data[1]) + " // " + str(data[2]) )
    while True:
        x = input("Bersediakah anda memasukkan informasi lagi? \n(iya/tidak) ")
        if x == "iya":
            break
        elif x == "tidak":
            print("Terimakasih atas waktunya !")
            break
        else:
            print()
            print("Harap masukkan data sesuai perintah !")
            continue



