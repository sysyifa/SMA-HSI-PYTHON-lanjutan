"""
Oke, aku ringkas jadi poin-poin biar lebih gampang dipahami 👇

---

## **Ringkasan Materi Regex (Regular Expression)**

### 1. **Kenapa Perlu Regex**

* Pencarian biasa dengan `in` atau `.find()` terbatas.
* Regex digunakan untuk pencarian teks kompleks: angka, email, pola khusus, validasi format, dll.

### 2. **Apa itu Regex**

* Regex = "bahasa mini" untuk mendeskripsikan pola teks.
* Bisa digunakan untuk mencari, memvalidasi, atau mengekstrak data.

### 3. **Modul `re` di Python**

* `import re` untuk mengaktifkan Regex.

**Fungsi dasar:**

* `re.findall(pola, teks)` → cari semua kecocokan, hasil berupa list.
* `re.search(pola, teks)` → cari kecocokan pertama, hasil berupa **Match object** (pakai `.group()` untuk ambil hasil).

### 4. **Metakarakter Penting**

* `.` → satu karakter apa saja (kecuali newline).
* `\d` → digit (0–9), `\D` → selain digit.
* `\w` → huruf/angka/underscore, `\W` → selain itu.
* `\s` → spasi/tab/newline, `\S` → selain spasi.
* **Jangkar (anchors):** `^` (awal string), `$` (akhir string), `\b` (batas kata).

### 5. **Quantifiers (Jumlah Kemunculan)**

* `*` → 0 kali atau lebih.
* `+` → 1 kali atau lebih.
* `?` → 0 atau 1 kali.
* `{n}` atau `{m,n}` → jumlah spesifik.

### 6. **Contoh Kasus**

* Cari angka: `re.findall(r'\d+', teks)`.
* Cari kata: `re.findall(r'\w+', teks)`.
* Cari email: `re.findall(r'\S+@\S+', teks)`.

### 7. **Latihan**

1. **Temukan semua angka** → gunakan `re.findall(r'\d+', data)`.
2. **Validasi nomor telepon (10–13 digit)** → pakai `^\d+$` + cek panjang dengan `len()`.
3. **Bedakan `re.search` dan `re.findall`**:

   * `search` → hanya hasil pertama.
   * `findall` → semua hasil dalam list.
4. **Cari kata berakhiran 'g'** → `re.findall(r'\w+g', kalimat)`.

---

👉 Intinya: **Regex adalah alat super untuk pencarian teks rumit**.
`findall` = ambil semua, `search` = ambil pertama, dan pola Regex + metakarakter = rumus pencarian.

Mau aku bikinkan **contoh kode lengkap untuk semua latihan 1–4** biar langsung bisa dicoba?

"""