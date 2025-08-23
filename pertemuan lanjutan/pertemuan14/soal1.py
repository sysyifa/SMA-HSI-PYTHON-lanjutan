"""
Latihan 1: Manajemen Daftar Belanja
. Buat sebuah list kosong bernama belanjaan.
. Gunakan .append() untuk menambahkan "Telur", "Susu", dan "Roti".
. Gunakan .insert() untuk menambahkan "Apel" di posisi paling awal.
. Gunakan .remove() untuk menghapus "Susu".
. Cetak list akhir.

"""

daftar_belanjaan = []
print("List awal:",daftar_belanjaan)

daftar_belanjaan.append("Telur")
daftar_belanjaan.append("Susu")
daftar_belanjaan.append("Roti")
print("list setelah di append :",daftar_belanjaan)

daftar_belanjaan.insert(0,"apel")
print("list setelah di insert:",daftar_belanjaan)

daftar_belanjaan.remove("Susu")
print("setelah di remove:",daftar_belanjaan)

