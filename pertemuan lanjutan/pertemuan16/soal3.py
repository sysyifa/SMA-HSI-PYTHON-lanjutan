


# Nested Dictionary
produk = {
    "PROD001": {
        "nama": "Keyboard Mechanical",
        "harga": 550000,
        "stok": 10
    },
    "PROD002": {
        "nama": "Mouse Gaming",
        "harga": 250000,
        "stok": 15
    }
}

# Cetak nama dan harga produk dengan ID "PROD002"
print("Nama Produk:", produk["PROD002"]["nama"])
print("Harga Produk:", produk["PROD002"]["harga"])
