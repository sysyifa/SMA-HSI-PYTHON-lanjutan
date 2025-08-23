"""
Latihan 3: Analisis Kata
Buat program yang:
. Meminta pengguna memasukkan sebuah kalimat.
. Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
. Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
. Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
list yang sudah terurut

"""

kalimat = input("Masukkan sebuah kalimat: ")

kata_kata = kalimat.split() #misahin kalimat menjadi list kata

jumlah_kata = len(kata_kata)
print("Jumlah kata:", jumlah_kata)  #ngitung jumlah kata

kata_kata.sort() # ngurutin kata kata
print("Kata-kata terurut:", kata_kata)

