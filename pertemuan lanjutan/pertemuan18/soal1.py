"""
Latihan 1: Class Kucing
. Buatlah sebuah class bernama Kucing.
. Buat constructor __init__() yang menerima dua parameter: nama dan warna. Constructor ini
harus menyimpan nilai-nilai tersebut ke dalam atribut self.nama dan self.warna.
. Buat sebuah method bernama bersuara() yang tidak memiliki parameter (selain self). Ketika
dipanggil, method ini harus mencetak "Meow!".
. Buat sebuah method bernama perkenalkan_diri() yang mencetak kalimat seperti "Halo, saya
kucing bernama [nama] dan warna saya [warna].".
. Buat dua object (instance) dari class Kucing dengan nama dan warna yang berbeda (misal, "Oren"
berwarna "Oranye" dan "Milo" berwarna "Coklat").
. Panggil method perkenalkan_diri() dan bersuara() dari kedua objek tersebut.


"""


class Kucing : 
    def __init__(self,nama,warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("Meow!!")

    def perkenalkan_diri(self):
        print(f"halo,saya kucing bernama {self.nama} dan warna saya {self.warna}.")

#ini membuat objek nya
Kucing1 = Kucing("Oren","Oranye")
kucing2 = Kucing("Milo","Coklat")

#buat manggil methodnya 
Kucing1.perkenalkan_diri()
Kucing1.bersuara()

kucing2.perkenalkan_diri()
kucing2.bersuara()
