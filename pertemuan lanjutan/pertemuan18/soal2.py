"""
Latihan 2: Class RekeningBank
Buatlah sebuah class bernama RekeningBank untuk mensimulasikan rekening bank sederhana.
. Buat constructor __init__() yang menerima dua parameter: nomor_rekening dan
nama_pemilik. Ia juga harus menginisialisasi atribut self.saldo dengan nilai awal 0.
. Buat method lihat_saldo() yang mencetak saldo saat ini.
. Buat method setor(jumlah) yang menambahkan jumlah ke self.saldo dan mencetak pesan
konfirmasi.
. Buat method tarik(jumlah) yang mengurangi jumlah dari self.saldo. Tambahkan logika if di
dalamnya: jika jumlah yang ditarik lebih besar dari saldo, cetak pesan "Saldo tidak mencukupi" dan
jangan ubah saldo. Jika tidak, kurangi saldo dan cetak pesan konfirmasi.
. Buat sebuah objek rekening_budi, lalu coba panggil semua method-nya: setor beberapa kali, tarik,
dan lihat saldo.

"""

class RekeningBank :
    def __init__(self,nomer_rekening,nama_pemilik):
        self.nomer_rekening = nomer_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def lihat_saldo(self):
        print(f"saldo anda saat ini Rp {self.saldo}")

    def setor(self,jumlah):
        self.saldo += jumlah
        print(f"berhasil setor Rp{jumlah}. saldo baru: Rp {self.saldo}")
    
    def tarik(self, jumlah) :
        if jumlah > self.saldo:
            print("saldo tidak mencukupi!")

        else :
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp {jumlah},saldo baru: Rp {self.saldo}")


RekeningBank = RekeningBank("28083928292","sumanto")

RekeningBank.lihat_saldo()
RekeningBank.setor(500000)
RekeningBank.setor(200000)
RekeningBank.tarik(150000)
RekeningBank.tarik(800000)
RekeningBank.lihat_saldo()





            

    

