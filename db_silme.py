import os
import sqlite3 as sql
veritabani = 'ornekdb.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect(veritabani)
imlec = vt.cursor()
imlec.execute("DELETE FROM ornek_tablo WHERE kolon1='deger'")
vt.commit()
imlec.execute("SELECT * FROM ornek_tablo")
kitaplar = imlec.fetchall()
print(kitaplar)
for i in kitaplar:
    for k in i:
        print(k,end=" ")
    print("")
vt.commit()
vt.close()