
print("TEST")

from login import loginFunction
from signup_member import signupMember
from signup_penyelenggara import signupPenyelenggara
from pageEvent import searchEvent
from add_event import checkDataEvent
from showDetailEvent import showDetail
from showDetailEvent import cekKeterdaftaran

from PyQt5.QtCore import QDate
import mysql.connector as database

conn = database.connect(
    user="admin",
    password="admin",
    host="localhost",
    database="e_vent")

cur = conn.cursor()

def test_login_member():
    #  Login member benar
    email = "13519132@std.stei.itb.ac.id"
    password = "admin"
    member, penyelenggara, member_id, penyelenggara_id, data_lengkap = loginFunction(email, password, cur)
    assert member == True
    assert penyelenggara == False
    # assert member_id == something beda" tiap database
    assert penyelenggara_id == -1 #karena yang login member, maka penyelenggara_id default = -1
    assert data_lengkap == True

    # Login salah


def test_login_penyelenggara():
    # Login penyelenggara benar
    email = "test1@yahoo.com"
    password = "test1"
    member, penyelenggara, member_id, penyelenggara_id, data_lengkap = loginFunction(email, password, cur)
    assert member == False
    assert penyelenggara == True
    assert member_id == -1
    assert data_lengkap == True
    # assert penyelenggara_id == something beda" tiap database

def test_login_gagal():
    # Login salah (tidak terdaftar)
    email = "notexist@yahoo.com"
    password = "notexist"
    member, penyelenggara, member_id, penyelenggara_id, data_lengkap = loginFunction(email, password, cur)
    assert member == False
    assert penyelenggara == False
    assert member_id == -1
    assert penyelenggara_id == -1
    assert data_lengkap == True

def test_signupMember():
    data_lengkap, sukses = signupMember("Rizky", "rizky@rizky.com", "2001-11-29", "rizky", cur, conn)
    assert data_lengkap == True
    assert sukses == False

    data_lengkap, sukses = signupMember("", "rizky@rizky.com", "2001-11-29", "rizky", cur, conn)
    assert data_lengkap == False
    assert sukses == False

def test_signupPenyelenggara():
    data_lengkap, sukses = signupPenyelenggara("joni", "joni@joni.id", "082211223344",  "joni", "joni", cur, conn)
    assert data_lengkap == True
    assert sukses == False #data sudah ada, signup gagal

    data_lengkap, sukses = signupPenyelenggara("", "joni@joni.id", "082211223344",  "joni", "joni", cur, conn)
    assert data_lengkap == False
    assert sukses == False

def test_search():
    sql = "SELECT namaEvent FROM event"
    cur.execute(sql)
    result = cur.fetchall()
    found, res = searchEvent(result,"test1")
    assert found == True

def test_nama_event_kosong():
    nama = ""
    deskripsi = "ini deskripsi"
    tanggal = QDate()
    tanggal.setDate(2030,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 0
    assert deskripsiStatus == 1
    assert tanggalStatus == True

def test_nama_event_kebanyakan():
    nama = "a"*300
    deskripsi = "ini deskripsi"
    tanggal = QDate()
    tanggal.setDate(2030,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 2
    assert deskripsiStatus == 1
    assert tanggalStatus == True

def test_deskripsi_event_kosong():
    nama = "ini nama"
    deskripsi = ""
    tanggal = QDate()
    tanggal.setDate(2030,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 1
    assert deskripsiStatus == 0
    assert tanggalStatus == True

def test_deskripsi_event_kebanyakan():
    nama = "ini nama"
    deskripsi = "a"*300
    tanggal = QDate()
    tanggal.setDate(2030,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 1
    assert deskripsiStatus == 2
    assert tanggalStatus == True

def test_tanggal_event_lampau():
    nama = "ini nama"
    deskripsi = "ini deskripsi"
    tanggal = QDate()
    tanggal.setDate(1999,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 1
    assert deskripsiStatus == 1
    assert tanggalStatus == False

def test_data_event_valid():
    nama = "ini nama"
    deskripsi = "ini deskripsi"
    tanggal = QDate()
    tanggal.setDate(2030,1,1)
    namaStatus, deskripsiStatus, tanggalStatus = checkDataEvent(nama, deskripsi, tanggal)
    assert namaStatus == 1
    assert deskripsiStatus == 1
    assert tanggalStatus == True

def test_show_detail():
    event_id = 1
    sukses, result = showDetail(event_id, cur)
    assert result[0]== event_id
    assert sukses == True

def test_show_detail_notfound():
    event_id = -1
    sukses, result = showDetail(event_id,cur)
    assert result == None
    assert sukses == False

def test_cekKeterdaftaran():
    event_id = 1
    member_id = 2
    result = cekKeterdaftaran(event_id, member_id, cur)
    assert result == True

def test_cekKeterdaftaran_belum_terdaftar():
    event_id = -1
    member_id = 2
    result = cekKeterdaftaran(event_id, member_id, cur)
    assert result == False