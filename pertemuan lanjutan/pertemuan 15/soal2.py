""" 
Latihan 2: Modifikasi Dictionary
. Gunakan dictionary biodata dari Latihan 1.
. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
. Ubah value dari key "umur" menjadi umurmu tahun depan.
. Cetak dictionary yang sudah diperbarui.

"""

#dictionary latihan 1
biodata = {
    "nama" : "sysyifa",
    "umur" : 16,
    "hobi" : ["azan","sepak bola","ngayal"],#list /string
    "sudah_menikah" : False
}

biodata["kota"] = "bandung"
biodata["nama kota"] = "cilehe"

biodata["umur"] = 17 # ganti umur

print("biodata setelah di rubah :",biodata)