import math
import random

# COLOR FORMATTINGS
col_input = "\033[1;0m{}\033[1;31m ".format # MERAH
col_output = "\033[1;34m{}\033[1;0m".format # BIRU
col_warning = "\033[1;33m{}\033[1;0m".format # KUNING

# FUNCTION UNTUK INPUT SEMUA VALUE
def type_in(type):
    return input(col_input(f"Masukkan {type}: "))

# FUNCTION UNTUK VALIDASI VALUE, KARENA HARUS BERBENTUK ANGKA DAN LEBIH DARI NOL
def validation_in(value):
    while True:
        try:
            x = float(type_in(value))
            if x <= 0:
                print(col_warning(f"Nilai {value} harus lebih dari nol!"))
            else:
                return x
        except ValueError: # MENANGKAP VALUEEROR
            print(col_warning(f"Masukkan nilai {value} yang valid!"))

# FUNCTION UNTUK PRINT MENU UTAMA
def menu_utama():
    print("\033[1;0mWelcome to Dek Depe's Name Tag Store!\n" +
        "-"*40 +
        "\n(1) Buat name tag" +
        "\n(2) Lihat pesanan name tag" +
        "\n(3) Exit\n")

# FUNCTION UNTUK MENAMPILKAN BAHAN KERTAS NAME TAG, MEMILIH, MENGHITUNG, DAN MENYIMPAN KE DICT
def bahan():
    print("\033[1;0mBahan kertas name tag yang tersedia:" +
        "\n> HVS: Rp100/cm^2" +
        "\n> Karton: Rp150/cm^2" +
        "\n> Buffalo: Rp170/cm^2" +
        "\n> Art Paper: Rp190/cm^2")
    global bahan_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    bahan_nametag = type_in("jenis kertas yang ingin digunakan")
    # VALIDASI BAHAN NAME TAG
    while bahan_nametag != "HVS" and bahan_nametag != "Karton" and bahan_nametag != "Buffalo" and bahan_nametag != "Art Paper":
        print(col_warning("Pilih salah satu dari bahan kertas yang tersedia!"))
        bahan_nametag = type_in("jenis kertas yang ingin digunakan")
    global harga_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    if bahan_nametag == "HVS":
        harga_nametag = luas_nametag*100
    elif bahan_nametag == "Karton":
        harga_nametag = luas_nametag*150
    elif bahan_nametag == "Buffalo":
        harga_nametag = luas_nametag*170
    else:
        harga_nametag = luas_nametag*190
    print(f"\033[1;0mSukses membuat pesanan name tag! Nomor antrian name tag ini adalah: {col_output(urutan_nametag)}")

# FUNCTIONS UNTUK HITUNG LUAS & HARGA
def luas_segiempat():
    """'p' ADALAH PANJANG & 'l' ADALAH LEBAR"""
    p = validation_in("panjang (cm)")
    l = validation_in("lebar (cm)")
    global luas_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    luas_nametag = p*l
    bahan()

def luas_segitiga():
    """'a' ADALAH PANJANG ALAS & 't' ADALAH TINGGI"""
    a = validation_in("panjang alas (cm)")
    t = validation_in("tinggi (cm)")
    global luas_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    luas_nametag = a*t/2
    bahan()

def luas_lingkaran():
    """'d' ADALAH DIAMETER"""
    d = validation_in("diameter (cm)")
    global luas_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    luas_nametag = 1/4*math.pi*d**2
    bahan()

def luas_random():
    """luas_random() AKAN MEMILIH SALAH SATU DARI KETIGA BENTUK SECARA ACAK"""
    chosen_shape = random.choice(["segiempat", "segitiga", "lingkaran"])
    print(col_output(f"Bentuk yang terpilih adalah {chosen_shape}"))
    global bentuk_nametag # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
    if chosen_shape == "segiempat":
        bentuk_nametag = "segiempat" # MENENTUKAN BENTUK NAMETAG SESUAI RANDOM YANG TERPILIH
        return luas_segiempat()
    elif chosen_shape == "segitiga":
        bentuk_nametag = "segitiga" # MENENTUKAN BENTUK NAMETAG SESUAI RANDOM YANG TERPILIH
        return luas_segitiga()
    else:
        bentuk_nametag = "lingkaran" # MENENTUKAN BENTUK NAMETAG SESUAI RANDOM YANG TERPILIH
        return luas_lingkaran()

# ============= RANGKA UTAMA PROGRAM =============

"""ASSIGN DICTIONARY SUMMARY UNTUK SEMUA JENIS INFORMASI, 
DENGAN KEY-NYA ADALAH NOMOR URUT NAMETAG, 
DAN VALUE-NYA ADALAH LIST BERISI NAMA, BENTUK, BAHAN, LUAS, HARGA"""
summary = {}

# DEFINE URUTAN = 0 UNTUK DITAMBAHKAN 1 SETIAP FOR LOOP JUMLAH NAMETAG
urutan_nametag = 0 

# 'while True' AGAR PROGRAM TETAP BERJALAN HINGGA USER INPUT PILIHAN 3 (KELUAR)
while True:
    menu_utama()
    try:
        pilihan = int(input(col_input("Pilih fitur yang ingin Anda gunakan: ")))
        
        # PILIHAN PERTAMA, MEMBUAT NAMETAG
        if pilihan == 1:
            print("\033[1;0m-"*40)
            pelanggan = int(validation_in("jumlah pelanggan"))

            # LOOP JUMLAH PELANGGAN
            for i in range(1, pelanggan+1):
                print("\n" + "\033[1;0m="*7 + f" PELANGGAN {i}")
                nama = input(col_input(f"Nama pelanggan ke-{i}: "))
                # INPUT JUMLAH NAMETAG (n)
                n = int(validation_in("jumlah name tag yang ingin dibuat"))
                global harga_pelanggan # MENGGUNAKAN GLOBAL AGAR VARIABLE MUDAH DIAKSES DIMANA SAJA
                harga_pelanggan = 0 # AGAR HARGA TER-RESET SETIAP BERGANTI PELANGGAN
                
                # LOOP JUMLAH NAME TAG
                for j in range(1, n+1):
                    urutan_nametag += 1 
                    bentuk_nametag = input(col_input(f"\nBentuk nametag ke-{j} (segiempat/segitiga/lingkaran/random): "))
                    # VALIDASI BENTUK NAMETAG
                    while bentuk_nametag != "segiempat" and bentuk_nametag != "segitiga" and bentuk_nametag != "lingkaran" and bentuk_nametag != "random":
                        bentuk_nametag = input("\033[1;34mBentuk tidak valid! Masukkan ulang bentuk yang diinginkan (segiempat/segitiga/lingkaran/random):\033[1;31m " + "\033[1;0m")
                    if bentuk_nametag == "segiempat":
                        luas_segiempat()
                    elif bentuk_nametag == "segitiga":
                        luas_segitiga()
                    elif bentuk_nametag == "lingkaran":
                        luas_lingkaran()
                    else:
                        luas_random()
                    
                    # MEMASUKKAN SEMUA DATA KE DICTIONARY summary, SESUAI FORMAT KEY & VALUE YANG SUDAH DIJELASKAN DI ATAS
                    summary[urutan_nametag] = [nama, bentuk_nametag, bahan_nametag, luas_nametag, harga_nametag]

                    # PENAMBAHAN HARGA PELANGGAN SETIAP PENGULANGAN NAMETAG
                    harga_pelanggan += harga_nametag

                # OUTPUT NAMA, JUMLAH NAMETAG, DAN HARGA TOTAL UNTUK SETIAP PELANGGAN
                print(f"\n\033[1;0mTotal harga kertas yang diperlukan untuk membuat {col_output(n)} name tag untuk pelanggan atas nama {col_output(nama)} adalah Rp{col_output(f'{harga_pelanggan:.2f}')}")

            print("\n" + "-"*40)

        # PILIHAN KEDUA, MELIHAT PESANAN NAME TAG, TAPI BELUM ADA YANG DIPESAN, AGAR KEMBALI KE SISTEM while True
        elif pilihan == 2 and urutan_nametag == 0:
            print("\033[1;0m-"*40 + col_warning("\nBelum ada name tag yang terdaftar!") + "\n\n" + "-"*40)

        # PILIHAN KEDUA, MELIHAT PESANAN NAME TAG
        elif pilihan == 2:
            print("\033[1;0m-"*40)
            nomor = int(type_in("nomor antrian pesanan yang ingin dilihat"))
            # OUTPUT DATA, DENGAN CARA MENGAKSES KEY, KEMUDIAN MENGAKSES INDEX VALUE-NYA YANG DALAM BENTUK LIST
            print(f"\n\033[1;0m======= PESANAN NAME TAG NO. {col_output(nomor)}" +
                f"\n\033[1;34mNama: {summary[nomor][0]}" +
                f"\nBentuk name tag: {summary[nomor][1]}" +
                f"\nBahan kertas: {summary[nomor][2]}" +
                f"\nLuas name tag: {f'{summary[nomor][3]:.2f}'} cm^2" +
                f"\nHarga: {f'{summary[nomor][4]:.2f}'}\033[1;0m\n" +
                "\n" + "-"*40)

        # PILIHAN KETIGA, KELUAR PROGRAM
        elif pilihan == 3:
            print("\033[1;0m-"*40 + 
                "\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!")
            break

        # VALIDASI INPUT, HARUS 1, 2, ATAU 3
        else:
            print(col_warning("Pilihan tidak valid. Silakan pilih 1, 2, atau 3."))
            print("\n" + "-"*40)

    # VALIDASI DI PILIHAN KE-2 LEBIH TEPATNYA, UNTUK MENANGKAP ERROR INPUT PILIHAN KE-2
    except:
        print(col_warning("Nomor antrian tidak valid!"))
        print("\n" + "-"*40)

# ================ END OF PROGRAM ================