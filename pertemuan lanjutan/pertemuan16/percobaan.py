"""
kontak = {'Andi': '08123', 'Budi': '08234', 'Citra': '08345'}
nomor_budi = kontak.pop('Budi')
print(f"Menghapus Budi, nomornya adalah: {nomor_budi}")
print("Kontak sekarang:", kontak)
# Tidak akan error, akan mengembalikan 'Tidak ditemukan'
nomor_dian = kontak.pop('Dian', 'Tidak ditemukan')
print(f"Mencoba menghapus Dian: {nomor_dian}")
kontak.popitem()
print("Setelah popitem:", kontak) # Akan menghapus Citra

del kontak['Andi']
print("Setelah del Andi:", kontak)

kontak.clear()
print("Setelah clear:", kontak)

"""
database_siswa = {
 "siswa_001": {
 "nama": "Budi Santoso",
 "umur": 17,
 "nilai": {
 "matematika": 90,
 "fisika": 88,
 "bahasa": 85
 }
 },
 "siswa_002": {
 "nama": "Ani Lestari",
 "umur": 16,
 "nilai": {
 "matematika": 95,
 "fisika": 91,
 "bahasa": 89
 }
 }
}
# Mengakses data nested
# Mengambil seluruh data siswa_002
data_ani = database_siswa["siswa_002"]
print("Data Ani:", data_ani)
# Mengakses nama Ani
nama_ani = database_siswa["siswa_002"]["nama"]
print("Nama Siswa 002:", nama_ani)
# Mengakses nilai fisika Budi
nilai_fisika_budi = database_siswa["siswa_001"]["nilai"]["fisika"]
print("Nilai Fisika Budi:", nilai_fisika_budi)
# Menambahkan data baru
database_siswa["siswa_001"]["nilai"]["kimia"] = 82
print("Nilai Budi setelah ditambah Kimia:", database_siswa["siswa_001"]
["nilai"])


