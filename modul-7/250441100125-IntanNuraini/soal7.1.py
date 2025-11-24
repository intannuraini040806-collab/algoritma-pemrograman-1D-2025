print("=== CONTACT BOOK  ===")

contacts = {}
def input_nama(name):
    while True:
        nama = input(name).strip()

        if nama == "":
            print("Nama tidak boleh kosong!")
            continue

        if not nama.replace(" ", "").isalpha():
            print("Error: Nama hanya boleh huruf!")
            continue

        if nama in contacts:
            print("Error: Nama sudah ada, gunakan nama lain!")
            continue

        return nama

def input_telepon():
    while True:
        telepon = input("Masukkan nomor telepon: ").strip()

        if telepon == "":
            print("Error: Nomor telepon tidak boleh kosong!")
            continue

        if not telepon.isdigit():
            print("Error: Nomor telepon harus angka!")
            continue

        if len(telepon) < 12:
            print("Nomor terlalu pendek, minimal 12 digit!")
            continue
        
        if len(telepon) > 13:
            print("Nomor terlalu panjang, maksimal 13 digit!")
            continue

        for data in contacts.values():
            if telepon == data[0]:
                print("Error: Nomor telepon sudah terdaftar!")
                break
        else:
            return telepon

def input_email():
    while True:
        email = input("Masukkan email: ").strip()

        if email == "":
            print("Error: Email tidak boleh kosong!")
            continue

        if "@" not in email or "." not in email:
            print("Error: Email harus mengandung '@' dan '.'")
            continue

        if not email.endswith("@gmail.com"):
            print("Error: Email harus menggunakan @gmail.com!")
            continue

        for data in contacts.values():
            if email == data[1]:
                print("Error: Email sudah digunakan!")
                break
        else:
            return email

def tampilkan():
    if len(contacts) == 0:
        print("\nBelum ada kontak.\n")
    else:
        print("\n--- Daftar Kontak ---")
        for nama in contacts:
            print("Nama   :", nama)
            print("Telp   :", contacts[nama][0])
            print("Email  :", contacts[nama][1])
            print("---------------------")
        print()


def cari():
    if len(contacts) == 0:
        print("Belum ada kontak, tambahkan kontak terlebih dahulu.")
        return

    nama = input("Masukkan nama yang dicari: ").strip()

    if nama in contacts:
        print("\nKontak ditemukan!")
        print("Nama   :", nama)
        print("Telp   :", contacts[nama][0])
        print("Email  :", contacts[nama][1])
    else:
        print("\nKontak tidak ada.")


def tambah():
    nama = input_nama("Masukkan nama: ")
    telepon = input_telepon()
    email = input_email()

    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!\n")


def update():
    nama = input("Masukkan nama yang ingin diupdate emailnya: ").strip()
    if nama in contacts:
        email_baru = input_email()
        contacts[nama][1] = email_baru
        print("Email berhasil diupdate!\n")
    else:
        print("Kontak tidak ditemukan.\n")


def hapus():
    nama = input("Masukkan nama yang ingin dihapus: ").strip()
    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus!\n")
    else:
        print("Kontak tidak ditemukan.\n")

while True:
    print("\n=== MENU CONTACT BOOK ===")
    print("1. Tampilkan kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        cari()
    elif pilihan == "3":
        tambah()
    elif pilihan == "4":
        update()
    elif pilihan == "5":
        hapus()
    elif pilihan == "6":
        print("Program selesai, terima kasih!")
        break
    else:
        print("Menu harus 1-6!")