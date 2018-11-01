qty = int(input("banyak barang :"))
hrgbrg = float(input("harga satuan :"))
jmlbyr = qty * hrgbrg
if jmlbyr > 100000:
    if hrgbrg > 50000:
        keterangan = "dapat karto diskon"
    else:
        keterangan = "tidak dapat kaktu diskon"
else:
    keterangan = "tidak dapat kartu diskon"
if qty > 100:
    diskon = jmlbyr * 0.3
else:
    diskon = 0
byrakh = jmlbyr - diskon
print("banyak barang :", qty)
print("harga satuan :",hrgbrg)
print("keterangan :",keterangan)
print("total bayar akhir : Rp.",byrakh)
