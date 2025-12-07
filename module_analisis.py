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

    for item in belanja:
        total += item["harga"]

        kat = item["kategori"]
        kategori_total[kat] = kategori_total.get(kat, 0) + item["harga"]

        if item["harga"] > termahal["harga"]:
            termahal = item
        if item["harga"] < termurah["harga"]:
            termurah = item

    print(f"Barang Termahal: {termahal['nama']} - Rp{termahal['harga']}")
    print(f"Barang Termurah: {termurah['nama']} - Rp{termurah['harga']}")
    print("\nPengeluaran Per Kategori:")
    
    for kat, t in kategori_total.items():
        print(f"- {kat}: Rp{t}")

    print("\nTotal Belanja Mingguan :", total)
    print("Estimasi Bulanan :", total * 4)

    if total > 300000:
        print("Anda melebihi 300.000/minggu!")
