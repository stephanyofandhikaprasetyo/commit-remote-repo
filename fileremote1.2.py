user_data = {
    "arsene lupin": {"nik": 1234, "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
    "sherlock holmes": {"nik": 4321, "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
    "irene adler": {"nik": 6789, "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}
}

while True:
    print("Pilih aksi yang diinginkan:")
    print("1. Input data")
    print("2. Cari data")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        nama = input("Masukkan nama: ")
        nik = int(input("Masukkan NIK: "))
        jenis_kelamin = input("Masukkan jenis kelamin: ")
        tanggal_lahir = input("Masukkan tanggal lahir (format YYYY-MM-DD): ")

        user_data[nama] = {"nik": nik, "jenis_kelamin": jenis_kelamin, "tanggal_lahir": tanggal_lahir}
        print("Data telah ditambahkan")

    elif choice == "2":
        nama_cari = input("Masukkan nama yang ingin dicari: ")
        if nama_cari in user_data:
            data_user = user_data[nama_cari]
            print("Data lengkap {}:".format(nama_cari))
            print("NIK: {}".format(data_user["nik"]))
            print("Jenis Kelamin: {}".format(data_user["jenis_kelamin"]))
            print("Tanggal Lahir: {}".format(data_user["tanggal_lahir"]))
        else:
            print("Data tidak ada")

    elif choice == "3":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")

