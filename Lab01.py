# COLOR FORMATTING
col_input = "\033[1;0m{}:\033[1;31m ".format
col_output = "\033[1;34m{}\033[1;0m".format
col_warning = "\033[1;33m{}\033[1;0m".format

print("Welcome to Dek Depe's Name Tag Store!\n" + "\033[1;0m-" * 45)

# INPUT
nama = input(col_input("Nama\t".expandtabs(25)))
tanggal_lahir = input(col_input("Tanggal lahir\t".expandtabs(25)))
jurusan = input(col_input("Jurusan\t".expandtabs(25)))
motto_hidup = input(col_input("Motto hidup\t".expandtabs(25)))

# INPUT PANJANG & LEBAR
while True:
    try:
        panjang = float(input(col_input("Masukan panjang (cm)\t".expandtabs(25))))
        if panjang <= 0:
            print(col_warning("Nilai panjang harus lebih dari nol!"))
        else:
            break
    except ValueError:
        print(col_warning("Masukkan nilai panjang dengan tepat!"))

while True:
    try:
        lebar = float(input(col_input("Masukan lebar (cm)\t".expandtabs(25))))
        if lebar <= 0:
            print("Nilai lebar harus lebih dari nol!")
        else:
            break
    except ValueError:
        print("Masukkan nilai lebar dengan tepat!")

# PERHITUNGAN LUAS & HARGA
luas = panjang * lebar
harga = luas * 100

print("\033[1;0m-" * 45)

# OUTPUT
print(
    f"Halo {col_output(nama)} dari {col_output(jurusan)}."
    + f'\nLahir pada {col_output(tanggal_lahir)} dengan motto "{col_output(motto_hidup)}."'
    + f"\nLuas name tag {col_output(nama)}: {col_output(luas)} cm^2\nHarga name tag {col_output(nama)}: Rp{col_output(harga)}"
)

print(
    "\033[1;0m-" * 45 + "\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!"
)
