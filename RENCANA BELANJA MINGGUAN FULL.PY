

belanja = []



def tambah_data():
    print("\n=== Tambah Data Belanja ===")
    nama = input("Nama barang   : ").strip()
    
    try:
        harga = int(input("Harga barang  : "))
    except:
        print("\033[91mHarga harus angka!\033[0m")
        return
    
    kategori = input("Kategori (makanan/kebersihan/dapur/lainnya): ").strip().lower()

    item = {"nama": nama, "harga": harga, "kategori": kategori}
    belanja.append(item)

    print("\033[92mData berhasil ditambahkan!\033[0m")


def tampilkan_data():
    print("\n=== Daftar Belanja Mingguan ===")
    if not belanja:
        print("Belum ada data.")
        return
    
    total = 0
    for i, item in enumerate(belanja):
        print(f"{i+1}. {item['nama']} - Rp{item['harga']} ({item['kategori']})")
        total += item["harga"]

    print("\nTotal Belanja Mingguan :", total)
    print("Estimasi Belanja Bulanan :", total * 4)


def edit_data():
    tampilkan_data()
    if not belanja:
        return

    try:
        idx = int(input("\nPilih nomor data yg ingin diedit: ")) - 1
        if idx < 0 or idx >= len(belanja):
            print("Nomor tidak valid!")
            return
    except:
        print("Input harus angka!")
        return

    print("Kosongkan input jika tidak ingin mengubah.")
    nama = input("Nama baru    : ")
    harga = input("Harga baru   : ")
    kategori = input("Kategori baru: ")

    if nama.strip():
        belanja[idx]["nama"] = nama
    if harga.strip():
        try:
            belanja[idx]["harga"] = int(harga)
        except:
            print("Harga harus angka!")
    if kategori.strip():
        belanja[idx]["kategori"] = kategori.lower()

    print("\033[92mData berhasil diubah!\033[0m")


def hapus_data():
    tampilkan_data()
    if not belanja:
        return

    try:
        idx = int(input("\nHapus nomor berapa? ")) - 1
        if idx < 0 or idx >= len(belanja):
            print("Nomor tidak valid!")
            return
    except:
        print("Input harus angka!")
        return
    
    terhapus = belanja.pop(idx)
    print(f"\033[91mMenghapus {terhapus['nama']}\033[0m")


def cari_barang():
    print("\n=== Cari Barang ===")
    keyword = input("Masukkan nama barang: ").lower()

    ditemukan = False
    for item in belanja:
        if keyword in item["nama"].lower():
            print(f"- {item['nama']} (Rp{item['harga']}, {item['kategori']})")
            ditemukan = True
    
    if not ditemukan:
        print("Barang tidak ditemukan!")


def analisis():
    print("\n=== Analisis Mingguan ===")
    if not belanja:
        print("Tidak ada data.")
        return

    # Cari termahal dan termurah
    termahal = belanja[0]
    termurah = belanja[0]

    total = 0
    kategori_total = {}

    for item in belanja:
        # total
        total += item["harga"]

        # kategori
        kategori = item["kategori"]
        kategori_total[kat] = kategori_total.get(kat, 0) + item["harga"]

        # termahal & termurah
        if item["harga"] > termahal["harga"]:
            termahal = item
        if item["harga"] < termurah["harga"]:
            termurah = item

    print(f"Barang Termahal: {termahal['nama']} - Rp{termahal['harga']}")
    print(f"Barang Termurah: {termurah['nama']} - Rp{termurah['harga']}")
    print("\nPengeluaran Per Kategori:")
    
    for kategori, t in kategori_total.items():
        print(f"- {kat}: Rp{t}")

    print("\nTotal Belanja Mingguan :", total)
    print("Estimasi Bulanan :", total * 4)

    if total > 300000:
        print("\033[93m⚠️ Anda melebihi 300.000/minggu, pertimbangkan untuk mengurangi belanja.\033[0m")


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


# --------------------- Program Utama ------------------------

muat_file()

while True:
    print("""
===============================
   APLIKASI BELANJA MINGGUAN
===============================
1. Tambah data
2. Tampilkan data
3. Edit data
4. Hapus data
5. Cari barang
6. Analisis mingguan
7. Simpan data
8. Keluar
""")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        edit_data()
    elif pilih == "4":
        hapus_data()
    elif pilih == "5":
        cari_barang()
    elif pilih == "6":
        analisis()
    elif pilih == "7":
        simpan_file()
    elif pilih == "8":
        simpan_file()
        print("Keluar...")
        break
    else:

        print("Menu tidak valid!")
