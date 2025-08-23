"""
Latihan 2: Manajemen Kontak
Buat program manajemen kontak sederhana:
. Buat dictionary kosong bernama kontak.
. Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
. Ubah nomor telepon "Ibu".
. Gunakan .pop() untuk menghapus "Teman".
. Cetak dictionary kontak akhir.

"""

kontak = {}

kontak["ibu"] = "0856437114456 "
kontak["ayah"] ="0246437139026 "
kontak["bolo"] ="04920242949240 "

kontak["ibu"] = "1111111222222"

kontak.pop("bolo")

print("kontak terakhir =",kontak)