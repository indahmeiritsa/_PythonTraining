# -*- coding: utf-8 -*-
"""

Created on Sat Jun  4 15:09:56 2022

@author: 007660 indahm
"""

hargabuku = 2000
jumlahbeli = 5
uang =100000
if uang > (hargabuku * jumlahbeli):
    print('beli buku')
elif uang > (hargabuku * jumlahbeli*2):
    print('beli bagibagi')
else:
    print ('pulang ambil uang')
   
#Latihan 2
#nilai_akhir > 80 <100		--> A
#nilai_akhir > 70 <79		--> B
#nilai_akhir > 60 <69		--> C
#nilai_akhir > 50 <59		--> D
#0 < 49		--> E

#nilai_absen * 10%
#nilai_tugas * 20%
#nilai_uts * 30%
#nilai_uas * 40%

#nilai_total = akumulasi semua nilai

absen = int(input("masukan nilai absen = "))
tugas = int(input("masukan nilai absen = "))
uts = int(input("masukan nilai absen = "))
uas = int(input("masukan nilai absen = "))

akhir = int((absen*0.1))+ int((tugas*0.2)) + int((uts*0.3)) + int((uas*0.4))
print("nilai akhir adalah = ", akhir)

if akhir >= 80 <=100 :
    print("anda mendapat A")
elif akhir >= 70 <= 79:
    print("anda mendapat B")
elif akhir >= 60 <= 69:
    print("anda mendapat C")
elif akhir >= 50 <= 59:
    print("anda mendapat D")
else:
    print("anda TIDAK LULUS")

