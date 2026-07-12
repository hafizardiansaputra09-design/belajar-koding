import os
import time

os.system('clear')

print("====SELAMAT DATANG DI TOKO PALING GOKIL====")

while True:
    try:
        nama = input("Masukkan nama anda: ")
        barang = input("Masukkan nama barang yang ingin dibeli: ")
        harga = int(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        break
    except ValueError:
        print("Ngetik yg bener dong, jangan asal ngetik ege. Harga dan jumlah harus angka! masa iya mo diingetin mulu, emang lu bocah tk??")


if jumlah <= 0 or harga <= 0:
    print("Unexpected condition: Kelakuan lu kayak anjing, kalo mo ngerampok bukan disini ege. lu mau gua doxxing?")
    exit()

else:
    print("====NOTA PEMBELIAN====")
    print(f"Nama pembeli: {nama}")
    print(f"Barang yang dibeli: {barang}")
    print(f"Harga barang: {harga}")
    print(f"Jumlah barang: {jumlah}")
    print(f"Total harga: {harga * jumlah}")

    total_harga = harga * jumlah
    waktu_sekarang = time.ctime()

    if total_harga > 500000:
        print("==LU DAPET DISKON POTONGAN 50000, JANLUP MAKASIH AMA GUA==")
        total_harga -= 50000
    elif total_harga > 250000:
        print("==LU DAPET DISKON POTONGAN 25000, JANLUP MAKASIH AMA GUA==")
        total_harga -= 25000
    else:
        print("==LU GA DAPET DISKON, BELANJA LU KURANG BANYAK NGAB==")

    print(f"Total harga setelah diskon: {total_harga}")

with open(f"nota_{nama}.txt", "w") as file:
    file.write("==================================\n")
    file.write("          NOTA PEMBELIAN          \n")
    file.write("==================================\n")
    file.write(f"Waktu cetak: {waktu_sekarang}\n")
    file.write(f"Nama pembeli: {nama}\n")
    file.write(f"Barang: {barang}\n")
    file.write(f"Harga barang: Rp{harga}\n")
    file.write(f"Jumlah barang: {jumlah}pcs\n")
    file.write(f"---------------------------------\n")
    file.write(f"Total harga: Rp{harga * jumlah}\n")
    file.write(f"Setelah diskon: Rp{total_harga}\n")
    file.write("==================================\n")
    file.write("      JANLUP BELI DISINI LAGI     \n")
    file.write("==================================\n")

with open("laporan_toko.txt", "a") as laporan:
    laporan.write(f"Nama pembeli: {nama}, Barang: {barang}, Harga: Rp{harga}, Jumlah: {jumlah}pcs, Total: Rp{total_harga}\n")

print(f"\n [INFO] Nota pembelian telah disimpan ke 'nota_{nama}.txt'")

print("====GUA GA AKAN BILANG MAKASIH KARENA MEMBELI DI TOKO GUA HUKUMNYA WAJIB AWOK-AWOK====")