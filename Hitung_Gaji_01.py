# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:20:41 2021

@author: Dell
"""

print("")
print("======================================================")
print("==========PERHITUNGAN GAJI KARYAWAN CV. LOGOS=========")
print("======================================================")
print("===========Daftar Gaji Pokok Setiap Golongan==========")
print("======================================================")
print("a = Golongan 1 Rp 2.500.000")
print("b = Golongan 2 Rp 4.500.000")
print("c = Golongan 3 Rp 6.500.000")
print("")
print("")

#1. Siapkan Variable
import datetime
list_nmapeg =[] #simpan seluruh nama pegawai
list_jnsgol =[] #simpan jenis golongan
list_nilgol =[] #nilai golongan (rupiah) rpgol (nilai gaji pokok)
list_jnskel =[] #simpan jenis kelamin
list_stskwn =[] #simpan status kawin
list_gjipok =[] #simpan gaji pokok
list_tjistr =[] #simpan tunjangan istri
list_tjanak =[] #simpan tunjangan anak
list_gjibrt =[] #simpan gaji brutto (G.Bruto = G.Pokok + Tj.Istri + Tj.Anak)
list_byjbtn =[] #simpan biaya jabatan
list_iupens =[] #simpan iuran pensiunan
list_iuorgs =[] #simpan iuran organisasi
list_gjnett =[] #simpan Gaji Netto 
list_gjbrut =[] #simpan Gaji Brutto

kdgol = ['a','b','c']
nmgol = ['Golongan 1','Golongan 2','Golongan 3']
rpgol = [2500000,4500000,6500000] #gaji pokok


#2. Input 
nmapeg = input("Ketikkan Nama Pegawai = ")

#3. Input Pilihan
pilgol = input(">>> Masukkan Kode Golongan = ")

 
#4. Input Jenis Kelamin dan Status Kawin
jnskel = input(" Ketikan Jenis Kelamin = ")
stskwn = input(" Ketikkan Status Kawin = ")

#5.Ambil pil Gol
##cek nama golongan dan ambil rupiah
i = 0
while i<len(nmgol):
    #jika value pada list kdgol(a) == pilgol
    if kdgol[i] == pilgol:
        #ambil golongan ke berapa
        nm_gol = nmgol[i]
        #ambil nilai golongan (rupiah)
        #nilgol = rpgol[i]
    #jika tidak cocok, lanjut ke nilai a berikutnya
    i+=1

#while i<len(nmgol):
#    if kdgol[i] == pilgol:
#        nm_gol = nmgol[i]
#    i+=1    

    #6. Hitung Gaji Bruto
    #gji_brut = nilgol + nilgol #coba coba 
    
    #7. Simpan Pada Item Pada List Perhitungan Gaji
    list_nmapeg.append(nmapeg)
#    list_jnsgol.append(nm_gol)
    list_jnskel.append(jnskel) #simpan jenis kelamin
    list_stskwn.append(stskwn) #simpan status kawin
    #list_gjbrut.append(gji_brut)
    
    #cnt = cnt + 1
    
    #8. Tampilkan output
print(datetime.datetime.now())
print(">>> NAMA           : " + nmapeg + "\r" )
print(">>> GOLONGAN       : " + str(nm_gol) + "\r")
print(">>> JENIS KELAMIN  : " + jnskel + "\r")
print(">>> STATUS KAWIN   : " + stskwn + "\r")
#print(">>> GAJI BRUTTO    : " + str(gji_brut) + "\r")
print("========================================")    


