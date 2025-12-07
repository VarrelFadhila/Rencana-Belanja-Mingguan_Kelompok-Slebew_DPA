# main.py
from module_belanja import tambah_data, tampilkan_data, edit_data, hapus_data, cari_barang
from module_analisis import analisis
from module_file import simpan_file, muat_file

# Muat data bila ada
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