import os
import sqlite3 as sql
veritabani = 'ornekdb.sqlite'
dosya_mevcut = os.path.exists(veritabani)
#dosya varlık durumuna göre True ve ya False değeri dönderir
if dosya_mevcut:
    vt = sql.connect(veritabani)
    imlec = vt.cursor()
else:
    print("veri tabanı yoktur")

imlec.execute("SELECT * FROM ornek_tablo")
kitaplar = imlec.fetchall()
print(kitaplar)
#print(kitaplar[0]) #print(kitaplar[9])
a=1
for i in kitaplar:
    #print(i)
    print(a," ",end="")
    for k in i:
        print(k,end=" ")
    print("")
    a=a+1
vt.close()