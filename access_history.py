import sqlite3

def create_database_for_history():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/history.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE access_history_time
                  (id INTEGER PRIMARY KEY,
                   time TEXT
                   
                   )''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_history()

def query_database_for_history_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/history.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM access_history_time WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

# lưu dữ liệu 
def save_data_for_history_in_table( time ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/history.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO access_history_time ( time) VALUES (?)",
               (time,))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# for i in range(20):
#     b = query_database_for_history_by_id(i+1)
#     print(b)

def query_database_for_history_3_time_lastest():
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/history.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute("SELECT * FROM access_history_time ORDER BY id DESC LIMIT 3")
    data = cursor.fetchall()

    # Đóng kết nối
    conn.close()
    time_values = list(map(lambda x: x[1], data))# cover data trả về thành dạng list time

    return time_values

# print(query_database_for_history_3_time_lastest())
# print(type(query_database_for_history_3_time_lastest()))