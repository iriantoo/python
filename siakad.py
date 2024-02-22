nama = input ("Nama Mahasiswa  : ")
nim = input ("NIM             : ")
prodi = input ("Program Studi   : ")
angkatan = input ("Angkatan       : ")

total_sks = 0
total_nilai = 0
total_tugas = 0
nama_matkul = [] 
nilai_matkul = []  

jumlah_matkul = int (input ("Jumlah mata kuliah yang ditempuh         : "))
print ("============================================")

for i in range (jumlah_matkul):
    matkul = input (f"\nNama Matakuliah ke-{i+1}: ")
    absen = int (input ("Jumlah kehadiran dari 16x pertemuan : "))
    kuis = float (input ("Nilai Kuis : "))
    tugas = int (input ("Jumlah tugas yang diberi : "))
    for i in range (tugas):
        nilai_tugas = float (input (f"Nilai Tugas ke-{i+1}: "))
        total_tugas =+ nilai_tugas
    uts = float (input ("Nilai UTS : "))
    uas = float (input ("Nilai UAS : "))
    
    total_nilai_matakuliah = ((absen/16) * 0.1) + (kuis * 0.1) + (total_tugas * 0.15) + (uts * 0.25) + (uas * 0.4)
    
    if (total_nilai_matakuliah >= 80):
        grade = 'A'
        ips = 4
    elif (total_nilai_matakuliah >= 70):
        grade = 'B'
        ips = 3
    elif (total_nilai_matakuliah >= 60):
        grade = 'C'
        ips = 2
    elif (total_nilai_matakuliah >= 50):
        grade = 'D'
        ips = 1
    else:
        grade = 'E'
        ips = 0
    
    total_sks += ips
    total_nilai += total_nilai_matakuliah

    print(f"\nNilai mata kuliah {matkul}: {total_nilai_matakuliah} ({grade})")
    
    nama_matkul.append(matkul)
    nilai_matkul.append(total_nilai_matakuliah)