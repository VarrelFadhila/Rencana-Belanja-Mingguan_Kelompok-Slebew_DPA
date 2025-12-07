# module_file.py

from module_belanja import belanja

def simpan_file():
    f = open("belanja.txt", "w")
    for item in belanja:
        f.write(f"{item['nama']}|{item['harga']}|{item['kategori']}\n")
    f.close()
    print("\033[92mData disimpan ke belanja.txt\033[0m")


def muat_file():
    try:
        f = open("belanja.txt", "r")
        for line in f:
            nama, harga, kategori = line.strip().split("|")
            belanja.append({"nama": nama, "harga": int(harga), "kategori": kategori})
        f.close()
        print("\033[92mData sebelumnya berhasil dimuat.\033[0m")
    except:
        print("Belum ada file data, mulai baru.")
