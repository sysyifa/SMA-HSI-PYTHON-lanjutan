"""
Latihan 1: Membuat dan Mengakses
. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
"sudah_menikah" (berisi boolean).
. Cetak seluruh dictionary.
. Cetak hanya value dari key "nama".
. Cetak hobi pertamamu dari list hobi.

"""

biodata = {
    "nama" : "sysyifa",
    "umur" : 16,
    "hobi" : ["azan","sepak bola","ngayal"],#list /string
    "sudah_menikah" : False
}

print(f"biodata :",biodata)

print("nama :",biodata["nama"])

print("hobi pertama :",biodata["hobi"][0])
