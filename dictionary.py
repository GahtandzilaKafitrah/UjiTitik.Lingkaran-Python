data_pertama = {
    "G":"Gahtan",
    "C":"Chico",
    "M":"Maria"
}

print(data_pertama)

data_pertama.update({"k":"Kevin"})
print(data_pertama)

del data_pertama["M"]
print(data_pertama)

CHECK = "G"
VALID = CHECK in data_pertama
print(f"Apakah {CHECK} ada pada dictionary : {VALID}")

for key in data_pertama.keys():
    print(key)

for value in data_pertama.values():
    print(value)

item = data_pertama.items()
print(item)

value = data_pertama.values()
print(value)

key = data_pertama.keys()
print(key)

for key,value in data_pertama.items():
    print(f"Ini adalah key = {key} sedangkan ini adalah value = {value} ")


data_baru = data_pertama.copy()
print(data_baru)

transferdata_1 = data_pertama.pop("k")
print(f"Tranfer data k adalah = {transferdata_1} \n")
print(f"menyebabkan data awal nya hilang 1 item ")
print(data_pertama)


