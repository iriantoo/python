import datetime as dt

hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

studio = {
    1 : {"nama" : 'Reguler', "harga" : [35000, 35000, 35000, 35000, 40000, 50000, 50000]},
    2 : {"nama" : 'Premiere', "harga" : [100000, 100000, 100000, 100000, 150000, 200000, 200000]}
}

harga_tiket = 0
pilihan_studio = 0
tanggal_menonton = 0
hari_menonton = " "
list_studio = []
list_tanggal = []
list_hari = []

def input_studio():
    global harga_tiket
    global pilihan_studio
    global tanggal_menonton
    global hari_menonton
    global list_studio
    global list_tanggal
    global list_hari
    print ("\nBerikut adalah jenis studio yang tersedia: ")
    for i in range (len(studio)):
        i += 1
        print (f"{i}. {studio[i]['nama']}")
    while True:
        pilihan_studio = int (input ("Silahkan memilih jenis studio [Masukkan nomor yang sesuai]: "))
        if (pilihan_studio in studio):
            list_studio.append (studio[pilihan_studio]['nama'])
            print ("\nSilahkan masukkan tanggal, bulan, dan tahun ingin menonton.")
            tanggal = int (input ("Tanggal [ex: 01]     : "))
            bulan = int (input ("Bulan   [01-12]      : "))
            tahun = int (input ("Tahun   [ex: 2024]   : "))

            tanggal_menonton = dt.date (tahun, bulan, tanggal)
            list_tanggal.append (tanggal_menonton)
            indeks_hari = tanggal_menonton.weekday()
            hari_menonton = hari[indeks_hari]
            list_hari.append (hari_menonton)
            harga_tiket = studio[pilihan_studio]['harga'][indeks_hari]

            print (f"\nJenis studio yang anda pilih adalah {studio[pilihan_studio]['nama']}")
            print (f"Anda memilih menonton pada tanggal {tanggal_menonton} hari {hari_menonton} dengan tiket seharga Rp {harga_tiket} per orang")
            break
        else:
            print ("\nPilihan tidak valid! Mohon memilih yang sesuai.")
            continue
    return harga_tiket, pilihan_studio, tanggal_menonton, hari_menonton, list_studio, list_tanggal, list_hari

film = {
    1 : {"nama" : 'Man In Love', "jam" : ['12:00', '14.50', '15:10', '19:30']},
    2 : {"nama" : 'A Man Called Otto', "jam" : ['12.15', '13:00', '17:20', '18:00']},
    3 : {"nama" : 'Monster', "jam" : ['13:45', '16:00', '18:10', '19:45']},
    4 : {"nama" : 'The Last 10 Years', "jam" : ['14:00', '15.25', '16:35', '20:05']},
    5 : {"nama" : 'Miracle in Cell No. 7', "jam" : ['12.50', '14:35', '17:00', '20:10']}
}

pilihan_film = 0
pilihan_jam = 0
list_film = []
list_jam = []

def input_film():
    global pilihan_film
    global pilihan_jam
    global list_film
    print ("\nBerikut adalah daftar film yang tersedia: ")
    for i in range (len(film)):
        i += 1
        print (f"{i}. {film[i]['nama']}")
    while True:
        pilihan_film = int (input ("Silahkan memilih film [Masukkan nomor yang sesuai]: "))
        if (pilihan_film in film):
            list_film.append (film[pilihan_film]['nama'])
            print (f"\nBerikut adalah jam tayang film {film[pilihan_film]['nama']} yang tersedia: ")
            for i in range (len(film[pilihan_film]['jam'])):
                i += 1
                print (f"{i}. {film[pilihan_film]['jam'][i-1]}")
            while True:
                pilihan_jam = int (input (f"Silahkan memilih jam film {film[pilihan_film]['nama']} yang tersedia [Masukkan nomor yang sesuai]: ")) - 1
                if (0 <= pilihan_jam < len(film[pilihan_film]['jam'])):
                    list_jam.append (film[pilihan_film]['jam'][pilihan_jam])
                    print (f"\nAnda memilih jam tayang film {film[pilihan_film]['nama']} pada pukul {film[pilihan_film]['jam'][pilihan_jam]}")
                    break
                else:
                    print ("\nPilihan tidak valid! Mohon memilih yang sesuai.")
                    continue
            break
        else:
            print ("\nPilihan tidak valid! Mohon memilih yang sesuai.")
            continue
    return pilihan_film, pilihan_jam, list_film, list_jam

list_jumlah_seat = []
list_seat = []
list_main_seat = []
list_harga = []
total_harga = 0

pesan_lagi = "Y"
while (pesan_lagi == "y" or pesan_lagi == "Y"):
    input_studio()
    input_film()


    jumlah_seat = int (input ("\nUntuk berapa seat: "))
    list_jumlah_seat.append (jumlah_seat)
    for i in range (jumlah_seat):
        seat = input (f"Seat ke-{i+1}: ")
        list_seat.append (seat)

    list_main_seat.append (list_seat)
    harga = jumlah_seat * harga_tiket
    list_harga.append (harga)
    total_harga = total_harga + harga

    print (f"\n{jumlah_seat} seat {list_seat} film {film[pilihan_film]['nama']} pada pukul {film[pilihan_film]['jam'][pilihan_jam]} seharga Rp {harga}")
    print (f"\nTotal harga sebesar Rp {total_harga}")

    while True:
        pesan_lagi = input ("\nIngin memesan lagi? [Y/N]: ")
        if (pesan_lagi == "y" or pesan_lagi == "Y"):
            break
        elif (pesan_lagi == "n" or pesan_lagi == "N"):
            break
        else:
            print ("\nPilihan anda tidak valid!")
            continue

print (f"\nTotal harga sebesar Rp {total_harga}")
while True:
    uang = int(input("\nMasukkan nominal pembayaran : Rp "))
    if (uang < total_harga):
        print ("Uang anda tidak mencukupi! Mohon masukkan nominal pembayaran yang sesuai!")
        continue
    else:
        break

print ("\n")
print ("=" * 150)
no = 1
index = 0
for i in list_harga:
    print (f"{no}. {list_tanggal[index]} hari {list_hari[index]} studio {list_studio[index]} film {list_film[index]} pukul {list_jam[index]} {list_jumlah_seat[index]} seat {list_main_seat[index]} Rp {list_harga[index]}")
    no += 1
    index += 1
print (f"\nTotal harga         : Rp {total_harga}")
print (f"Nominal pembayaran   : Rp {uang}")
print (f"Kembalian            : Rp {uang - total_harga}")
print ("=" * 150)