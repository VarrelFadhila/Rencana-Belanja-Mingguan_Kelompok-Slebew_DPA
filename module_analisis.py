# module_analisis.py

from module_belanja import belanja

def analisis():
    print("\n=== Analisis Mingguan ===")
    if not belanja:
        print("Tidak ada data.")
        return

    termahal = belanja[0]
    termurah = belanja[0]
    total = 0
    kategori_total = {}

    for barang in belanja:
        total += barang["harga"]

        kategori = barang["kategori"]
        if kategori not in kategori_total:
            kategori_total[kategori] = 0
        kategori_total[kategori] += barang["harga"]
        
        if barang["harga"] > termahal["harga"]:
            termahal = barang
            
        if barang["harga"] < termurah["harga"]:
            termurah = barang

    print(f"Barang Termahal: {termahal['nama']} - Rp{termahal['harga']}")
    print(f"Barang Termurah: {termurah['nama']} - Rp{termurah['harga']}")
    print("\nPengeluaran Per Kategori:")
    
    for kategori, t in kategori_total.items():
        print(f"- {kategori}: Rp{t}")

    print("\nTotal Belanja Mingguan :", total)
    print("Estimasi Bulanan :", total * 4)

    if total > 300000:
        print("\033[93m Anda melebihi 300.000/minggu!\033[0m")