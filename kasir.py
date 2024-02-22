barang = {
    1 : {"nama" : 'Tas Kuromi', "harga" : 400000},
    2 : {"nama" : 'Lampu Tidur', "harga" : 200000},
    3 : {"nama" : 'Kipas Kuromi', "harga" : 150000},
    4 : {"nama" : 'Gantungan Kunci Kuromi', "harga" : 50000},
    5 : {"nama" : 'Bantal Kuromi', "harga" : 250000}
}

list_barang = []
list_jumlah_barang = []
list_harga = []
total_harga = 0
pesan_lagi= "y"

print ("Daftar Barang dan Harganya:")
for i in range(len(barang)):
    i = i+1
    print (f"{i}. {barang[i]['nama']} - Rp {barang[i]['harga']}")

while (pesan_lagi == "y" or pesan_lagi == "Y"):
    pilihan = input ("\nMasukkan nomor barang yang ingin dibeli [1-5]: ")
    if pilihan.isdigit():
        no_pilihan = int(pilihan)
        if (1 <= no_pilihan <= 5):
            list_barang.append (barang[no_pilihan]['nama'])
            jumlah_barang = int (input (f"Jumlah {barang[no_pilihan]['nama']} yang ingin dibeli: "))
            list_jumlah_barang.append (jumlah_barang)
            total_harga = total_harga + (barang[no_pilihan]['harga'] * jumlah_barang)
            print (f"{barang[no_pilihan]['nama']} sebanyak {jumlah_barang} pcs adalah Rp {barang[no_pilihan]['harga'] * jumlah_barang}")
            list_harga.append (barang[no_pilihan]['harga'] * jumlah_barang)
        else:
            print ("Pilihan anda tidak valid!")
            continue
    else:
        print ("Pilihan anda tidak valid!")
        continue

    while True:
        pesan_lagi = input ("\nIngin memesan lagi? [Y/N]: ")
        if (pesan_lagi == "y" or pesan_lagi == "Y"):
            break
        elif (pesan_lagi == "n" or pesan_lagi == "N"):
            break
        else:
            print ("Pilihan anda tidak valid!")
            continue

total_harga_dapat_diskon = 500000
if (total_harga >= total_harga_dapat_diskon):
    print ("\nAnda mendapatkan diskon sebesar 10%")
    harga_diskon = total_harga * (10/100)
    print (f"Diskon sebesar Rp {harga_diskon:.0f}")
    print (f"Total harga sebelum diskon: Rp {total_harga}")
    print (f"Total harga setelah diskon: Rp {(total_harga - harga_diskon):.0f}")
else:
    print ("\nAnda tidak mendapatkan diskon")
    harga_diskon = 0

print (f"\nTotal harga pembelian: Rp {(total_harga - harga_diskon):.0f}")
while True:
    uang = int(input("\nMasukkan nominal pembayaran : Rp "))
    if (uang < (total_harga - harga_diskon)):
        print ("Uang anda tidak mencukupi! Mohon masukkan nominal pembayaran yang sesuai!")
        continue
    else:
        break

print ("\n=================================")
no = 1
index = 0
for i in list_jumlah_barang:
    print (f"{no}. {list_barang[index]} {i} pcs Rp {list_harga[index]}")
    no += 1
    index += 1
print (f"Total harga pembelian: Rp {(total_harga - harga_diskon):.0f}")
print (f"Nominal pembayaran: Rp {uang}")
print (f"Kembalian {uang - (total_harga - harga_diskon):.0f}")
print ("---------------------------------")

