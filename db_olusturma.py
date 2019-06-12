import sqlite3 as sql
vt = sql.connect('ornekdb.sqlite')
imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz

imlec.execute("CREATE TABLE IF NOT EXISTS ornek_tablo (kitap_adi,kitap_yazari,okunma_durumu,begeni)")

giris = "INSERT INTO ornek_tablo VALUES ('k1_kayit1', 'k2_kayit1', 'k3_kayit1','k4_kayit1')"

imlec.execute(giris)


vt.commit() # veri tabanına hafızadaki bilgiyi kaydetmek için
vt.close() # veri tabanını kapatmak için