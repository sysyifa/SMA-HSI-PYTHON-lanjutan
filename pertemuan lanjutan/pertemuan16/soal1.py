"""
Latihan 1: Iterasi dan Kalkulasi
Diberikan dictionary harga buah: harga_buah = {"apel": 5000, "jeruk": 8500, "mangga":
7800, "pisang": 3000}.
Gunakan for loop dan .items() untuk mencetak setiap buah dan harganya dalam format "Harga 1 kg
[nama buah] adalah Rp [harga]". Di akhir, hitung dan cetak total harga semua buah

"""

harga_buah = {
    "apel": 5000,
    "jeruk": 8500,
    "mangga": 7800,
    "pisang": 3000
}

total_harga = 0 #variabel untuk  menapung total harga / wadah awal untuk harga 

# Iterasi menggunakan .items()
for buah,harga in  harga_buah.items(): # setiap putaran loop ,buah akan berisi nama buah, dan harga berisi harganya.
    print(f"harga 1 kg {buah} adalah Rp {harga}")  # dan gunanya for loop untuk mengulang setiap pasangan (harga dan buah)
    total_harga += harga #nambahin harga buah ke total

print(f"total semua harga adalah Rp {total_harga}")#cetak semua total harga buah