import os
from datetime import datetime
import pandas as pd

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_transaction():
    now = datetime.now()
    time = now.strftime("%B %d, %Y | %H:%M:%S")

    header = """ 
    \t------------------------------------
    \t|              HOTEL               |
    \t|            ~SYARIAH~             | 
    \t------------------------------------
    """

    print(header)
    print()
    input("\t~~TEKAN ENTER UNTUK MELANJUTKAN~~")

    print()
    
    nama_saya = str(input("\tMasukkan Nama lengkap: "))

    print("\t\t-----------------")
    print("\t\t| Laki-laki (L) |")
    print("\t\t| Perempuan (P) |")
    print("\t\t-----------------")

    opsi_gender = input("\tJenis kelamin (Pilih L/P): ")
    jenis_kel = ""
    
    if opsi_gender.lower() == "l":
        jenis_kel = "Laki-laki"
        print(f"\t({jenis_kel})")
    elif opsi_gender.lower() == "p":
        jenis_kel = "Perempuan"
        print(f"\t({jenis_kel})")
    else:
        print("\tProgram berhenti")
        return None

    usia = int(input("\tMasukkan usia anda: "))
    if usia < 18:
        print("\tMaaf anda belum cukup umur")
        return None
    elif usia >= 18:
        print("\tLanjut")
    alamat = input("\tMasukkan Alamat anda: ")

    print("\t~~~~~~~~~PILIH JENIS KAMAR~~~~~~~~~")
    print("\t1. Classic Room = Rp.200.000 / hari")
    print("\t2. Elite Room   = Rp.400.000 / hari")
    print("\t3. Premium Room = Rp.600.000 / hari")
    print("\t4. VIP Room     = Rp.800.000 / hari")
    print("\t-----------------------------------")

    while True:
        jenis_kamar = int(input("Pilih jenis kamar dengan memilih angka 1-4.: "))
        if 1 <= jenis_kamar <= 4:
            break
        else:
            print('Kamar Tidak Tersedia, Silahkan Input Kembali 1 hingga 4.')

    jenis_kamar_list = ["Classic Room", "Elite Room", "Premium Room", "VIP Room"]
    jenis = jenis_kamar_list[jenis_kamar - 1]
    harga_list = [200000, 400000, 600000, 800000]
    harga = harga_list[jenis_kamar - 1]

    print()

    hari = int(input("\tUntuk berapa hari: "))
    hasil = hari * harga
    
    total = f"""
    \t{header}
    \t{time}
    \tNama          : {nama_saya}
    \tJenis Kelamin : {jenis_kel}
    \tUmur          : {usia} Tahun
    \tAlamat        : {alamat}
    \tJenis Kamar   : {jenis}
    \tSelama        : {hari} Hari
    \tTotal Harga   : RP.{hasil}

    \t~~~~~~~~~PEMBAYARAN~~~~~~~~~
    """

    print(total)
    uang_pembayaran = int(input("\tMasukkan jumlah uang pembayaran: RP. "))

    if uang_pembayaran < hasil:
        print("\tUang pembayaran kurang. Silahkan masukkan uang yang cukup.")
        return None

    uang_kembalian = uang_pembayaran - hasil

    total += f"""
    \tUang Pembayaran: RP.{uang_pembayaran}
    \tUang Kembalian: RP.{uang_kembalian}
    
    \t~~TERIMA KASIH TELAH MEMESAN ~~
    """
    print(total)

    return total

def main():
    transactions = []

    while True:
        clear_screen()
        transaction_result = input_transaction()

        if transaction_result is not None:
            transactions.append(transaction_result)

        status = input("\tApakah ingin memesan lagi? (y = ya, n = tidak): ")
        print()

        if status.lower() == "n":
            break
        elif status.lower() != "y":
            print("\tMaaf, inputan tidak diketahui, Program akan berhenti")
            break

    # Simpan transaksi ke pandas DataFrame
    df = pd.DataFrame(transactions, columns=["Transaction"])
    df.to_csv("transactions.csv", index=False)

if __name__ == "__main__":
    main()
