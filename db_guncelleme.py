import os
import sqlite3 as sql
veritabani = 'ornekdb.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()


imlec.execute("UPDATE SORGUSU")
imlec.execute("UPDATE SORGUSU")
vt.commit()

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("SELECT * FROM ornek_tablo")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")

vt.close()