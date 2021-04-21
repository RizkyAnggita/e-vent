# E-Vent
> Aplikasi Booking Online Event berbasis Desktop
> Menggunakan Python3, Pyqt5, mariadb

## General Info
Aplikasi berbasis desktop untuk melakukan pemesanan tiket event-event yang diadakan secara online bagi member. Pihak penyelenggara event dapat menawarkan event yang diselenggarakannya melalui aplikasi ini, meliputi detail event seperti deskripsi event, tanggal pelaksanaan, biaya pendaftaran, kontak, dll. Calon pengunjung dapat melihat event-event apa saja yang ditawarkan oleh penyelenggara, termasuk melihat detail acara, informasi penyelenggara, biaya pendaftaran, kontak penyelenggara, dll.

## Cara Menjalankan aplikasi
Terdapat beberapa dependencies yang harus dimiliki sebelum menjalankan aplikasi ini : <br>
- Python 3.x <br>
- mariadb  Ver 15.1<br>
- PyQt5 5.15.4 (pip install pyqt5)<br>
- Pyqt5-tools 5.15.2 (pip3 install pyqt5-tools)<br>
- mysql-connector-python 8.0.23 (pip install mysql-connector-python) atau <br>
- mysql-connector-2.2.9 (pip install mysql-connector)<br>
- pytest 6.2.3 (pip install pytest)<br>

Jika semua dependensi sudah terpenuhi, jalankan urutan di bawah ini
1. Clone repo ini ke direktori lokal, dan masuk ke dalam direktori tersebut
```
$ git clone https://gitlab.informatika.org/RizkyAnggita/if2250-2021-k03-13-e-vent.git
$ cd if2250-2021-k03-13-e-vent/
```
2. Jalakan mariadb server, kemudian jalankan MariaDB kemudian ketik script di bawah ini
```
mysql> USE mysql;
mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> CREATE DATABASE e_vent;
mysql> use e_vent;
mysql> exit;
```
3. Kemudian lakukan import database sql (e_vent.sql). Pada terminal, ketikkan
```
$ mysql -u {username} -p e_vent < e_vent.sql
```
4. Kemudian, masuk ke direktori src dan jalankan `main.py`.
```
$ cd src/
$ python3 main.py
atau
$ python main.py
```
5. Aplikasi sudah berjalan
6. Jika ingin menjalankan testing modul, jalankan test_modul.py pada direktori src.
```
$ cd src/
$ pytest -v
```

## Daftar Modul yang diimplementasi
1. Modul Utama (Tampilan Awal)  - 13519132 Rizky Anggita S Siregar <br>
foto here
2. Modul Login  - 13519132 Rizky Anggita S Siregar <br>
foto here
3. Modul Signup (Signup Member dan Penyelenggara)   - 13519132 Rizky Anggita S Siregar <br>
foto here
4. Modul Feed Event dan Search Event    - 13519117 Rehagana Kevin C. Sembiring <br>
foto here
5. Modul Detail Event dan Registrasi    - 13519127 Giant Andreas Tambunan <br>
foto here
6. Modul Add Event (termasuk Validasi dan Konfirmasi Event) - 13519150 Imam Nurul Hukmi <br>
foto here


## Daftar Tabel Basis Data
```
Tabel Member
+-----------+--------------+------+-----+---------+----------------+ 
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| member_id | int(11)      | NO   | PRI | NULL    | auto_increment |
| nama      | varchar(255) | NO   |     | NULL    |                |
| email     | varchar(255) | NO   |     | NULL    |                |
| tgl_lahir | date         | NO   |     | NULL    |                |
| password  | varchar(16)  | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

Tabel Penyelenggara
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| penyelenggara_id | int(11)      | NO   | PRI | NULL    | auto_increment |
| nama             | varchar(255) | NO   |     | NULL    |                |
| email            | varchar(255) | NO   |     | NULL    |                |
| no_telp          | varchar(20)  | NO   |     | NULL    |                |
| password         | varchar(16)  | NO   |     | NULL    |                |
| deskripsi        | varchar(255) | NO   |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+

Tabel Event
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| event_id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| namaEvent        | varchar(255) | NO   |     | NULL    |                |
| deskripsi        | varchar(255) | NO   |     | NULL    |                |
| tanggal          | date         | NO   |     | NULL    |                |
| biaya            | int(11)      | NO   |     | NULL    |                |
| penyelenggara_id | int(11)      | NO   | MUL | 1       |                |
+------------------+--------------+------+-----+---------+----------------+

Tabel member_event
+-----------+---------+------+-----+---------+-------+
| Field     | Type    | Null | Key | Default | Extra |
+-----------+---------+------+-----+---------+-------+
| member_id | int(11) | NO   | PRI | NULL    |       |
| event_id  | int(11) | NO   | PRI | NULL    |       |
+-----------+---------+------+-----+---------+-------+
```

## Author
- 13519117 Rehagana Kevin C. Sembiring
- 13519127 Giant Andreas Tambunan
- 13519132 Rizky Anggita S Siregar
- 13519150 Imam Nurul Hukmi
