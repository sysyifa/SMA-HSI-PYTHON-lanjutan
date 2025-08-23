"""
Latihan 3: Penggunaan .get()
. Masih dengan dictionary biodata.
. Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
pada baris ini agar tidak error).
. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
. Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan nilai default "Pelajar".
Cetak hasilnya.

"""

#dictionary latihan 1
biodata = {
    "nama" : "sysyifa",
    "umur" : 16,
    "hobi" : ["azan","sepak bola","ngayal"],#list /string
    "sudah_menikah" : False
}

# print(biodata["pekerjaan"])   Error: KeyError karena "pekerjaan" tidak ada di dictionary

print(biodata.get("pekerjaan"))

print("pekerjaan :",biodata.get("pekerjaan","santri nih boss"))


