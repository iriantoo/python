# Mendefinisikan variabel atau menyiapkan sebuah variabel kosong
nama_biaya_tambahan = []
biaya_nama_tambahan = []
total_biaya_tambahan = 0

# Membuat sebuah tampilan
print ("-" * 55)
print ("-" * 10 + " Program Perencanaan Biaya Liburan "  + "-" * 10)
print ("-" * 55)

# Memasukkan nilai / Menginput data
tujuan_liburan = str (input ("Tujuan berlibur             : "))
jumlah_orang = int (input ("Jumlah orang yang berlibur  : "))
lama_liburan = int (input ("Lama berlibur (dalam hari)  : "))
print ("\n")

# Menampilkan opsi transportasi untuk ke tempat tujuan liburan
print (f"Berikut adalah beberapa opsi transportasi yang dapat digunakan untuk ke {tujuan_liburan}:")
print ("1. Pesawat")
print ("2. Kereta")
print ("3. Rental mobil")
print ("Selain 1/2/3. Kendaraan pribadi")
print ("\n")

# Memilih transportasi ke tempat tujuan liburan dengan menginput angka yang sesuai
transportasi_tujuan_liburan = input ("Menggunakan transportasi no: ")

# Penyeleksian kondisi transportasi untuk ke tempat tujuan liburan
if (transportasi_tujuan_liburan == "1"):
    # Jika memilih 1 (pesawat) atau Ya, maka program akan meminta menginput biaya pp pesawat
    pp_pesawat = int (input ("Biaya PP ke " + str (tujuan_liburan) + " menggunakan pesawat: Rp "))
    transportasi_tujuan_liburan = "pesawat"
    # Melakukan perhitungan biaya transportasi ke tempat tujuan liburan
    biaya_transportasi_tujuan_liburan = pp_pesawat * jumlah_orang

# Jika tidak, maka akan terjadi penyeleksian kondisi lagi
elif (transportasi_tujuan_liburan == "2"):
    # Jika memilih 2 (kereta) atau Ya, maka program akan meminta menginput biaya pp kereta
    pp_kereta = int (input ("Biaya PP ke " + str (tujuan_liburan) + " menggunakan kereta: Rp "))
    transportasi_tujuan_liburan = "kereta"
    # Melakukan perhitungan biaya transportasi ke tempat tujuan liburan
    biaya_transportasi_tujuan_liburan = pp_kereta * jumlah_orang

# Jika tidak, maka akan terjadi penyeleksian kondisi lagi
elif (transportasi_tujuan_liburan == "3"):
    # Jika memilih 3 (rental mobil) atau Ya, maka program akan meminta menginput biaya rental mobil perhari dan jumlah mobil yang dirental
    rental_mobil = int (input ("Biaya rental mobil per hari : Rp "))
    jumlah_rental_mobil = int (input ("Jumlah mobil yang dirental  : "))
    transportasi_tujuan_liburan = "rental mobil"
    # Melakukan perhitungan biaya transportasi ke tempat tujuan liburan
    biaya_transportasi_tujuan_liburan = rental_mobil * jumlah_rental_mobil * lama_liburan

# Jika tidak (else), maka program akan otomatis memilih selain 1/2/3 atau kendaraan pribadi
else:
    # Maka program akan meminta menginput jumlah kendaraan pribadi yang dipakai dan perkiraan biaya bensin PP dari tempat tujuan liburan
    jumlah_kendaraan = int (input ("Jumlah kendaraan yang dipakai   : "))
    bensin_pp_pribadi = int (input ("Biaya bensin PP                 : Rp "))
    transportasi_tujuan_liburan = "kendaraan pribadi"
    # Melakukan perhitungan biaya transportasi ke tempat tujuan liburan
    biaya_transportasi_tujuan_liburan = jumlah_kendaraan * bensin_pp_pribadi
print ("\n")

# Menginput beberapa data yang akan menjadi total biaya sementara
biaya_penginapan = int (input ("Biaya penginapan per malam   : Rp "))
lama_menginap = int (input ("Lama menginap (dalam malam)  : "))
biaya_makan = int (input ("Biaya makan per hari         : Rp "))
biaya_jajan = int (input ("Biaya jajan                  : Rp "))
biaya_belanja = int (input ("Biaya belanja                : Rp "))
dana_darurat = int (input ("Dana darurat yang disiapkan  : Rp "))
print ("\n")

# Menghitung total biaya sementara
total_biaya_sementara = (biaya_penginapan * lama_menginap * jumlah_orang) + (biaya_makan * jumlah_orang * lama_liburan) + (biaya_jajan * jumlah_orang) + (biaya_belanja * jumlah_orang) + (dana_darurat * jumlah_orang)

# Menampilkan opsi transportasi yang digunakan saat di tempat tujuan liburan
print (f"Berikut adalah beberapa opsi transportasi yang dapat digunakan saat di {tujuan_liburan}:")
print ("1. Rental mobil")
print ("2. Rental motor")
print ("3. Kendaraan pribadi")
print ("Selain 1/2/3. Jalan kaki")
print ("\n")

# Memilih transportasi ke tempat tujuan liburan dengan menginput angka yang sesuai
transportasi_liburan = input ("Menggunakan transportasi no: ")

# Penyeleksian kondisi transportasi yang digunakan saat di tempat tujuan liburan
if (transportasi_liburan == "1"):
    # Jika memilih 1 (rental mobil) atau Ya, maka program akan meminta menginput biaya rental mobil perhari, jumlah mobil yang dirental, dan biaya bensin rental mobil per hari
    rental_mobil = int (input ("Biaya rental mobil per hari : Rp "))
    jumlah_rental_mobil = int (input ("Jumlah mobil yang dirental  : "))
    bensin_rental_mobil = int (input ("Biaya bensin rental mobil per hari: Rp "))
    transportasi_liburan = "rental mobil"
    # Melakukan perhitungan biaya transportasi yang digunakan saat di tempat tujuan liburan
    biaya_transportasi_liburan = (rental_mobil * jumlah_rental_mobil * lama_liburan) + (bensin_rental_mobil * jumlah_rental_mobil * lama_liburan)

# Jika tidak, maka akan terjadi penyeleksian kondisi lagi
elif (transportasi_liburan == "2"):
    # Jika memilih 2 (rental motor) atau Ya, maka program akan meminta menginput biaya biaya rental motor perhari, jumlah motor yang dirental, dan biaya bensin rental motor per hari
    rental_motor = int (input ("Biaya rental motor per hari        : Rp "))
    jumlah_rental_motor = int (input ("Jumlah motor yang dirental         : "))
    bensin_rental_motor = int (input ("Biaya bensin rental motor per hari : Rp "))
    transportasi_liburan = "rental motor"
    # Melakukan perhitungan biaya transportasi yang digunakan saat di tempat tujuan liburan
    biaya_transportasi_liburan = (rental_motor * jumlah_rental_motor * lama_liburan) + (bensin_rental_motor * jumlah_rental_motor * lama_liburan)

# Jika tidak, maka akan terjadi penyeleksian kondisi lagi
elif (transportasi_liburan == "3"):
    # Jika memilih 2 (kendaraan pribadi) atau Ya, maka program akan meminta menginput biaya bensin kendaraan pribadi per hari
    bensin_pribadi= int (input ("Biaya bensin kendaraan per hari : Rp "))
    transportasi_liburan = "kendaraan pribadi"
    # Melakukan perhitungan biaya transportasi yang digunakan saat di tempat tujuan liburan
    biaya_transportasi_liburan = jumlah_kendaraan * bensin_pribadi * lama_liburan

# Jika tidak (else), maka program akan otomatis memilih selain 1/2/3 atau jalan kaki
else:
    # Maka tidak ada biaya transportasi yang digunakan saat di tempat tujuan liburan
    transportasi_liburan = "jalan kaki"
    biaya_transportasi_liburan = 0

# Memberi pertanyaan apakah ada biaya tambahan yang ingin ditambahkan saat sedang berliburan
biaya_tambahan = input ("Apakah ada biaya tambahan yang ingin ditambahkan? [Y]: ")

# Looping dan penyeleksian kondisi apakah ada biaya tambahan
# While atau ketika memilih Y atau Yes/Ya dalam biaya tambahan, maka program akan melakukan perulangan dan meminta inputan
# Jika memilih selain Y dari awal, maka program akan melewatinya
while (biaya_tambahan == "Y"):
    nama_biaya = str (input ("Nama biaya tambahan : "))
    biaya_tambahan = int (input (f"Biaya {nama_biaya}: Rp "))
    # Memasukkan nama biaya ke variabel nama biaya tambahan yang kosong yang telah disiapkan
    nama_biaya_tambahan.append (nama_biaya) 
    # Memasukkan biaya tambahan ke variabel biaya nama tambahan yang kosong yang telah disiapkan
    biaya_nama_tambahan.append (biaya_tambahan)
    # Menghitung total biaya tambahan
    total_biaya_tambahan = total_biaya_tambahan + biaya_tambahan
    # Menanyakan kembali apakah ada aktivitas tambahan
    # Jika memilih N atau No/Tidak, maka perulangan akan berhenti dan akan meneruskan program
    biaya_tambahan = input ("Apakah ada biaya tambahan lagi yang ingin ditambahkan? [Y]: ")

# Menghitung total biaya keseluruhan
total_biaya_keseluruhan = biaya_transportasi_tujuan_liburan + total_biaya_sementara + biaya_transportasi_liburan + total_biaya_tambahan

# Menampilkan output
print ("\n")
print (f"Perencaan biaya liburan dengan tujuan liburan adalah {tujuan_liburan} berjumlah {jumlah_orang} orang. Yang akan dilakukan selama {lama_liburan} hari. Dengan moda transportasi ke tempat tujuan liburan menggunakan {transportasi_tujuan_liburan}. Adapun perkiraan biaya-biaya selama liburan sebagai berikut.")
print (f"• Biaya transportasi ke tempat tujuan liburan adalah Rp {biaya_transportasi_tujuan_liburan}, dengan menggunakan transportasi ke tempat tujuan yaitu {transportasi_tujuan_liburan}.")
print (f"• Transportasi selama liburan adalah {transportasi_liburan} dengan biaya sebesar Rp {biaya_transportasi_liburan}.")
print (f"• Total biaya sementara mencakup biaya penginapan, biaya makan, biaya jajan, biaya belanja, dan dana darurat yaitu Rp {total_biaya_sementara}.")
print (f"• Total biaya tambahan dari aktivitas tambahan adalah Rp {total_biaya_tambahan}.")
print (f"• Total biaya keseluruhan yang diperkirakan adalah Rp {total_biaya_keseluruhan}.")
