import sqlite3
import datetime
import json
import pytz

# def gettime2():
#     utc_time = datetime.datetime.now(pytz.utc)
#     local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
#     t = local_time.strftime("%Y-%m-%d %H:%M:%S")
#     return t

def create_database_for_admin():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/admin.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE admin_info
                  (id INTEGER PRIMARY KEY,
                   admin_name TEXT,
                   password TEXT,
                   createdTime TEXT
                   
                   )''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_admin()

def query_database_for_admin_by_name( name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/admin.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM admin_info WHERE name=?", (name,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def save_data_for_admin_in_table(name, password , time):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/admin.db')
    cursor = conn.cursor()


    # Thêm dữ liệu vào bảng rider
    cursor.execute(f"INSERT INTO admin_info (admin_name, password,createdTime) VALUES (?, ?, ?)",
                   (name, password , time))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# save_data_for_admin_in_table(name="admin", password="111111",time=gettime2())