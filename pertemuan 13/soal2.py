"""
(2) Modifikasi List
. Gunakan list jadwal_senin dari latihan sebelumnya.
. Ternyata jam pelajaran "Olahraga" dipindah ke hari Selasa. Ubah elemen "Olahraga" menjadi
"Kimia".
. Cetak list jadwal_senin yang sudah diperbarui.

"""
"""
 # Membuat list jadwal Senin
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print("jadwal senin:",jadwal_senin)

# Cetak hanya mata pelajaran pertama
print("mata pelajaran ke siji:",jadwal_senin[0])

# Cetak mata pelajaran terakhir (indeks negatif)
print("mata pelajaran ke loro:",jadwal_senin[-1])
"""

#(2) Mengganti "Olahraga" menjadi "Kimia"
jadwal_senin[2] = "Kimia"

# Cetak list yang sudah diperbarui
print(jadwal_senin)
