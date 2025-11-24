print("Program Inventaris Gudang CRUD dengan Validasi")

inventaris = {}   

def tampilkan_semua():
    print("\n=== DAFTAR INVENTARIS ===")
    if not inventaris:
        print("Belom ada data barang.")
    else:
        for Id_barang, data in inventaris.items():
            print(f"ID Barang : {Id_barang}")
            print(f"Nama      : {data[0]}")
            print(f"Harga     : {data[1]}")
            print(f"Stok      : {data[2]}")
            print("----------------------------")

def cari_barang():
    print("\n=== CARI BARANG ===")
    if not inventaris:
        print("belom ada data barang")
        return
    Id_barang = input("Masukkan ID barang: ")
    if Id_barang =="":
        print("id tidak bole kosong")
        return

    if Id_barang in inventaris:
        data = inventaris[Id_barang]
        print("Barang ditemukan!")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")

def tambah_barang():
    print("\n=== TAMBAH BARANG ===")
    while True:
      Id_barang = input("Masukkan ID: ")
      if not Id_barang.isdigit():
        print("id harus berupa angka lohhh!")
      else:
        break

    if Id_barang in inventaris:
        print("ID sudah terpakai! Gunakan ID lain.")
        return

    while True:
       nama = input("Nama barang: ")
       if not nama.isalpha():
           print("namanya berupa huruf !!")
       else:
           break

    while True:
        try:
            harga = float(input("Harga barang: "))
            break
        except:
            print("masukinnya angka bukan yang lain")


    while True:
        try:
            stok = int(input("Stok barang: "))
            break
        except:
            print("masukin angka bukan yang lain")

    inventaris[Id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    print("\n=== UPDATE STOK BARANG ===")
    Id_barang = input("Masukkan ID barang: ")

    if Id_barang not in inventaris:
        print("Barang tidak dapat ditemukan.")
        return

    while True:
        try:
            stok_baru = int(input("Masukkan stok baru (boleh tambah/kurang): "))
            break
        except:
            print("Masukkan angka yang benar!")

    stok_sekarang = inventaris[Id_barang][2]
    stok_final = stok_sekarang + stok_baru

    if stok_final < 0:
        print("Gagal! Stok tidak boleh negatif.")
        return

    inventaris[Id_barang][2] = stok_final
    print("Stok berhasil diperbarui!")


def hapus_barang():
    print("\n=== HAPUS BARANG ===")
    Id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if Id_barang in inventaris:
        del inventaris[Id_barang]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan.")


while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang (read)")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru(create)")
    print("4. Update Stok Barang(update)")
    print("5. Hapus Barang (delete)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")