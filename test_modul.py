
print("TEST")

from login import loginFunction

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

   
