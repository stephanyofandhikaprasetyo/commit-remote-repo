user_data = {
"arsene lupin": {"nik": 1234, "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
"sherlock holmes": {"nik": 4321, "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
"irene adler": {"nik": 6789, "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}
}
nama = input("Masukkan nama: ")
nik = int(input("Masukkan NIK: "))
jenis_kelamin = input("Masukkan jenis kelamin: ")
tanggal_lahir = input("Masukkan tanggal lahir (format YYYY-MM-DD): ")

user_data[nama] = {"nik": nik, "jenis_kelamin": jenis_kelamin, "tanggal_lahir": tanggal_lahir}
