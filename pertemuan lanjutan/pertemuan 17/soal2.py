"""
Latihan 2: Immutability
Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
langsung.

"""

kordinat_awal = (10,20)

kordinat_baru = (kordinat_awal[0],25)          
#kordinat_baru = kordinat_awal[0:1] + (25,)

print("kordinat awal :",kordinat_awal)
print("kordinat baru :",kordinat_baru)