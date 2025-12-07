# module_belanja.py

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