import random
import math

# COLOR FORMATTINGS
col_input = "\033[1;0m{}\033[1;31m ".format
col_output = "\033[1;34m{}\033[1;0m".format
col_warning = "\033[1;33m{}\033[1;0m".format

# FUNCTION UNTUK INPUT SEMUA VALUE
def type_in(type):
    return float(input(col_input(f"Masukkan {type}\t: ".expandtabs(45))))

# FUNCTION UNTUK VALIDASI VALUE
def validation_in(value):
    while True:
        try:
            sym = type_in(value)
            if sym <= 0:
                print(f"Nilai {value} harus lebih dari nol!")
            else:
                return sym
        except ValueError:
            print(col_warning(f"Masukkan nilai {value} dengan tepat!"))

# FUNCTIONS UNTUK HITUNG LUAS & HARGA
def luas_segiempat(): # 'p' ADALAH PANJANG & 'l' FOR LEBAR
    p = validation_in("panjang (cm)")
    l = validation_in("lebar (cm)")
    harga_segiempat = p*l*100
    return harga_segiempat

def luas_segitiga(): # 'a' ADALAH PANJANG ALAS & 't' ADALAH TINGGI
    a = validation_in("panjang alas (cm)")
    t = validation_in("tinggi (cm)")
    harga_segitiga = a*t*100/2
    return harga_segitiga

def luas_lingkaran(): # 'd' ADALAH DIAMETER
    d = validation_in("diameter (cm)")
    harga_lingkaran = 1/4*math.pi*d**2*100
    return harga_lingkaran

def luas_random(): # luas_random() AKAN MEMILIH SALAH SATU DARI KETIGA BENTUK SECARA ACAK
    chosen_shape = random.choice(["segiempat", "segitiga", "lingkaran"])
    print(col_output(f"Bentuk yang terpilih adalah {chosen_shape}"))
    if chosen_shape == "segiempat":
        return luas_segiempat()
    elif chosen_shape == "segitiga":
        return luas_segitiga()
    else:
        return luas_lingkaran()

# ================== P R O G R A M ==================

# INTRO & INPUT JUMLAH PELANGGAN (num)
print("\033[1;0mWelcome to Dek Depe's Name Tag Store!")
num = int(validation_in("jumlah pelanggan"))
print("\033[1;0m-"*40)

# LOOP JUMLAH PELANGGAN (num)
for i in range(1, num+1):
    print("\033[1;0m="*7 + f" PELANGGAN {i}")
    # INPUT NAMA PELANGGAN & INPUT JUMLAH ORDER (n)
    nama = input(col_input(f"Masukkan nama pelanggan ke-{i}\t: ".expandtabs(45)))
    n = int(validation_in("jumlah name tag yang ingin dibuat"))
    harga = 0 # UNTUK ASSIGN VARIABEL HARGA DAN UNTUK MERESET HARGA SETIAP ITERASI
    # LOOP JUMLAH ORDER (n)
    for j in range(1, n+1):
        bentuk = input(col_input(f"\nBentuk nametag ke-{j} (segiempat/segitiga/lingkaran/random)  : ")).upper()
        while bentuk != "SEGIEMPAT" and bentuk != "SEGITIGA" and bentuk != "LINGKARAN" and bentuk != "RANDOM":
            print("Pilih salah satu dari bentuk-bentuk yang tersedia!")
            bentuk = input(col_input(f"Bentuk nametag ke-{j} (segiempat/segitiga/lingkaran/random)  : ")).upper()
        if bentuk == "SEGIEMPAT":
            harga +=luas_segiempat()
        elif bentuk == "SEGITIGA":
            harga += luas_segitiga()
        elif bentuk == "LINGKARAN":
            harga += luas_lingkaran()
        else:
            harga += luas_random()
    # OUTPUT HARGA TOTAL TIAP PELANGGAN
    print(f"\n\033[1;0mTotal harga kertas yang diperlukan untuk membuat {col_output(n)} name tag untuk pelanggan atas nama {col_output(nama)} adalah Rp{col_output(harga)}\n")

# OUTRO
print("\033[1;0m-"*40 + "\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!")

# ============ E N D  O F  P R O G R A M ============