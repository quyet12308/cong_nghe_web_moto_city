import sqlite3

def create_database_for_rider5():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/rider.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE rider5
                  (id INTEGER PRIMARY KEY,
                   rider_name TEXT,
                   country TEXT,
                    QAT TEXT,
                    INA TEXT,
                    ARG TEXT,
                    AME TEXT,
                    POR TEXT,
                    SPA TEXT,
                    FRA TEXT,
                    ITA TEXT,
                    CAT TEXT,
                    GER TEXT,
                    NED TEXT,
                    GBR TEXT,
                    AUT TEXT,
                    RSM TEXT,
                    ARA TEXT,
                    JPN TEXT,
                    THA TEXT,
                    AUS TEXT,
                    MAL TEXT,
                    VAL TEXT
                   )''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_rider5()

def query_database_for_rider_by_id5( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM rider5 WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def save_data_for_rider_in_table5(rider_name, country):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()
    # Thêm dữ liệu vào bảng rider
    cursor.execute(f"INSERT INTO rider5 (rider_name, country) VALUES (?, ?)",
                   (rider_name, country))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

import sqlite3

def update_column_values(column_name, values):
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Lặp qua từng giá trị trong danh sách và cập nhật vào cột cụ thể
    for i in range(len(values)):
        cursor.execute(f"UPDATE rider5 SET {column_name} = ? WHERE id = ?", (values[i], i + 1))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def get_empty_columns(table_name):
    conn = sqlite3.connect('database/rider.db')  # Thay thế bằng đường dẫn tới cơ sở dữ liệu SQLite của bạn
    cursor = conn.cursor()

    # Lấy tên cột trong bảng
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]

    # Kiểm tra các cột không có giá trị
    empty_columns = []
    for column in column_names:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column} IS NULL")
        count = cursor.fetchone()[0]
        if count == 0:
            empty_columns.append(column)

    conn.close()
    return empty_columns

def get_empty_column2(table_name):
    conn = sqlite3.connect('database/rider.db')  # Thay đổi đường dẫn tới cơ sở dữ liệu của bạn
    cursor = conn.cursor()

    # Lấy danh sách tên cột trong bảng
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    # Kiểm tra từng cột trong danh sách
    for column in columns:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column} IS NOT NULL")
        result = cursor.fetchone()[0]
        if result == 0:
            # Trả về tên cột chưa có giá trị
            return column

    # Đóng kết nối và cursor
    cursor.close()
    conn.close()

    # Trường hợp không tìm thấy cột nào chưa có giá trị
    return None

# d = get_empty_columns("rider5")
# e = get_empty_column2("rider5")
# print(e)

vong_dua = ['QAT', 'INA', 'ARG', 'AME', 'POR', 'SPA', 'FRA', 'ITA', 'CAT', 'GER', 'NED', 'GBR', 'AUT', 'RSM', 'ARA', 'JPN', 'THA', 'AUS', 'MAL', 'VAL']
QATs = ['-', '7', '25', '13', '-', '20', '9', '8', '-', '-', '4']
INAs = ['1', '20', '5', '7', '13', '8', '11', '16', '-', '25', '0']
ARGs = ['11', '8', '6', '25', '2', '10', '16', '-', '20', '3', '9']
AMEs = ['11', '9', '25', '5', '16', '4', '20', '7', '8', '0', '6']
PORs = ['8', '25', '-', '16', '-', '-', '13', '20', '-', '11', '6']
SPAs = ['25', '20', '8', '16', '11', '6', '0', '-', '0', '4', '2']
FRAs = ['-', '13', '25', '16', '20', '8', '-', '11', '-', '-', '6']
ITAs = ['25', '20', '-', '16', '1', '9', '-', '13', '3', '7', '4']
CATs = ['-', '25', '-', '11', '2', '8', '-', '16', '20', '7', '9']
GERs = ['-', '25', '6', '13', '16', '9', '-', '20', '10', '7', '-']
NEDs = ['25', '-', '5', '13', '10', '11', '6', '3', '9', '7', '16']
GBRs = ['25', '8', '13', '7', '16', '5', '9', '-', '11', '10', '20']
AUTs = ['25', '20', '-', '10', '16', '9', '8', '11', '6', '4', '3']
RSMs = ['25', '11', '20', '10', '0', '8', '9', '-', '7', '5', '16']
ARAs = ['20', '-', '25', '16', '11', '13', '7', '8', '10', '5', '3']
JPNs = ['-', '8', '7', '0', '25', '20', '-', '5', '16', '11', '9']
THAs = ['16', '0', '10', '5', '20', '6', '4', '13', '7', '25', '9']
AUSs = ['16', '-', '11', '7', '-', '6', '25', '8', '9', '4', '0']
MALs = ['25', '16', '20', '6', '10', '8', '11', '7', '-', '3', '0']
VALs = ['7', '13', '8', '-', '-', '20', '25', '-', '16', '11', '-']
# for i in QATs:
#     update_column_values(column_name="QAT",values=QATs)

name = [
    "BAGNAIA Francesco",
    "QUARTARARO Fabio",
    "BASTIANINI Enea",
    "ESPARGARO Aleix",
    "MILLER Jack",
    "BINDER Brad",
    "RINS Alex",
    "ZARCO Johann",
    "MARTIN Jorge",
    "OLIVEIRA Miguel",
    "VINALES Maverick"
]



countrys = [
"ITA","FRA","ITA","SPA","AUS","RSA","SPA","FRA","SPA","POR","SPA"
]

# for i in range(11):
#     print(f'<tr><td class="center">{name[i]}</td><td class="center">{countrys[i]}</td><td><input type="number" name="point{i}"></td></tr>')


# for i in range(11):
#     # print(i)
#     save_data_for_rider_in_table5(rider_name=name[i],country=countrys[i])

# for i in range(15):
#     data = query_database_for_rider_by_id5(i)
#     print(data)