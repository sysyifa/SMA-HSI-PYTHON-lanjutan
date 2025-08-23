"""

"""
def pembersih_data():
    try:
        with open(r"C:\Users\santri_jimm\latihan\lanjutan\pertemuan lanjutan\project pekan 3\transaksi_kotor.txt", "r" , encoding="utf-8") as file_input:
            with open("laporan_bersih_txt","w",encoding="utf-8")as file_output:

                file_output.write("LAPORAN TRANSAKSI BERSIH\n")
                file_output.write("========================\n")

                grand_total = 0

                for baris in file_input:
                    if not baris.strip():
                        continue

                    baris = baris.strip()

                    data_potongan= baris.split(",")

                    if len (data_potongan) != 4:
                        continue

                    id_transaksi = data_potongan[0].strip().upper()
                    nama_produk = data_potongan[1].strip().title()
                    jumlah = int(data_potongan[2].strip())
                    harga_satuan = float(data_potongan[3].strip())


                    total_harga = jumlah * harga_satuan
                    grand_total += total_harga

                    if total_harga <= 500000:
                        continue

                    string_output = (
                        f"ID: {id_transaksi} | Produk: {nama_produk} |"
                        f"jumlah: {jumlah} | Total harga : Rp {total_harga} |"
                    )

                    file_output.write(string_output +"\n")

                file_output.write("---ANALISIS SELESAI---\n")
                file_output.write(f"TOTAL KESELURUHAN : Rp {grand_total}\n")

            print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

    except FileNotFoundError:
        print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")

if __name__=="__main__":
    pembersih_data()

                