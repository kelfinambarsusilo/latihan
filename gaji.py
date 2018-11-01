
namapgw = input("Nama Pegawai :")
gapok = float(input("Gaji Pegawai :"))
jmlkrj = float(input("Jam Kerja :"))

gator = gapok * jmlkrj

if gator > 5000000:
    pajak = gator * 0.05
    keterangan = "Pajak"
else:
    pajak = 0
    keterangan = "Tidak Kena Pajak"
gajibersih = gator - pajak
print("Nama Pegawai",namapgw)
print("Gaji Kotor =",gator)
print("Pajak =",pajak)
print("Gaji Bersih=",gajibersih)
print("Keterangan=",keterangan)

