"""
(4)Slicing dan Penggabungan
. Buat dua buah list: awal_minggu = ["Senin", "Selasa", "Rabu"] dan akhir_minggu =
["Kamis", "Jumat", "Sabtu", "Minggu"].
. Gunakan operator + untuk menggabungkan keduanya menjadi list baru bernama seminggu.
. Dari list seminggu, gunakan slicing untuk membuat list baru bernama hari_kerja yang hanya
berisi hari Senin sampai Jumat.
. Cetak list hari_kerja.

"""
# Dua list awal
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Gabungkan list
seminggu = awal_minggu + akhir_minggu

# Ambil hanya hari kerja (Senin sampai Jumat)
hari_kerja = seminggu[0:5]

# Cetak hari kerja
print(hari_kerja)
