
print("TEST")

from login import loginFunction
from signup_member import signupMember
from signup_penyelenggara import signupPenyelenggara
from pageEvent import searchEvent

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
    member, penyelenggara, member_id, penyelenggara_id = loginFunction(email, password, cur)
    assert member == True
    assert penyelenggara == False
    # assert member_id == something beda" tiap database
    assert penyelenggara_id == -1 #karena yang login member, maka penyelenggara_id default = -1

    # Login salah


def test_login_penyelenggara():
    # Login penyelenggara benar
    email = "test1@yahoo.com"
    password = "test1"
    member, penyelenggara, member_id, penyelenggara_id = loginFunction(email, password, cur)
    assert member == False
    assert penyelenggara == True
    assert member_id == -1
    # assert penyelenggara_id == something beda" tiap database

def test_login_gagal():
    # Login salah (tidak terdaftar)
    email = "notexist@yahoo.com"
    password = "notexist"
    member, penyelenggara, member_id, penyelenggara_id = loginFunction(email, password, cur)
    assert member == False
    assert penyelenggara == False
    assert member_id == -1
    assert penyelenggara_id == -1

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

