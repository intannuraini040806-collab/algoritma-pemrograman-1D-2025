print("=== PROGRAM VALIDASI KUPON PADA SISTEM KASIR ===")

keranjang = []

kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}
def input_harga():
    while True:
        harga = input("Masukkan harga barang: ")

        if harga == "":
            print("Harga tidak boleh kosong!")
            continue
        if not harga.isdigit():
            print("Harga harus angka!")
            continue
        if int(harga) <= 0:
            print("Harga harus lebih dari 0!")
            continue

        return int(harga)


def input_kode_kupon():
    while True:
        kode = input("Masukkan kode kupon : ")

        if kode == "":
            return ""  

        if " " in kode:
            print("Kupon tidak boleh ada spasi!")
            continue

        return kode
    
def input_nama_barang():
    while True:
        nama = input("masukkan nama barang :")
        if nama == "":
            print("nama barang tidak boleh kosong")
            continue
        if not nama.replace(" ","").isalpha():
            print("nama barang hanya boleh huruf")
            continue
        return nama

def tambah_barang():
    print("\n=== INPUT BARANG ===")
    nama_barang = input_nama_barang()
    harga = input_harga()

    keranjang.append([nama_barang, harga])
    print("Barang berhasil ditambahkan!\n")


def tampilkan_keranjang():
    if len(keranjang) == 0:
        print("\nKeranjang masih kosong.\n")
        return

    print("\n=== DAFTAR BARANG ===")
    total = 0
    for barang,harga in keranjang:
        print(f"{barang} - Rp{harga}")
        total += harga

    print(f"\nTOTAL BELANJA : Rp{total}\n")


def tampilkan_kupon():
    if len(kupon) == 0:
        print("\nTidak ada kupon yang tersedia.\n")
    else:
        print("\n===== KUPON TERSEDIA =====")
        for kode in kupon:
            print(f"Kode : {kode} | Diskon : {kupon[kode]}%")
        print()

def proses_pembayaran():
    if len(keranjang) == 0:
        print("\nKeranjang masih kosong, tambahkan barang dulu!\n")
        return
    
    total_belanja = sum(harga for _, harga in keranjang)
    print(f"\nTotal belanja: Rp{total_belanja}")

    tampilkan_kupon()

    kode = input_kode_kupon()

    if kode == "":
        print("\nTidak menggunakan kupon.")
        print("Total Bayar:", total_belanja)
        print("Terima kasih!\n")
        keranjang.clear()
        return

    if kode not in kupon:
        print("\nKupon tidak valid!\n")
        return

    diskon = kupon[kode]
    potongan = total_belanja * (diskon / 100)
    total_bayar = total_belanja - potongan

    del kupon[kode]   

    print("\n====== STRUK PEMBAYARAN ======")
    print(f"Total Belanja      : Rp {total_belanja}")
    print(f"Diskon ({diskon}%) : Rp {potongan}")
    print(f"Total Bayar        : Rp {total_bayar}")
    print("Kupon berhasil digunakan!\n")

    keranjang.clear()  

while True:
    print("\n====== MENU PROGRAM ======")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Tampilkan Kupon")
    print("4. Bayar / Gunakan Kupon")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_keranjang()
    elif pilihan == "3":
        tampilkan_kupon()
    elif pilihan == "4":
        proses_pembayaran()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid! Pilih 1-5.\n")