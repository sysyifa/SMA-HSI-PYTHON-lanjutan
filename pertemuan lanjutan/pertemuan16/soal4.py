# soal4.py

fname = r"c:\Users\santri_jimm\latihan\lanjutan\pertemuan lanjutan\pertemuan16\mbox-short.txt"
fh = open(fname)

hari_count = dict()

for line in fh:
    if line.startswith("From "):   # hanya baris yang mulai dengan "From "
        kata = line.split()
        hari = kata[2]             # kata ketiga = hari
        hari_count[hari] = hari_count.get(hari, 0) + 1

print(hari_count)
