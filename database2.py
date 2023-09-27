import sqlite3
from test3 import name,data,countrys

def create_database_for_rider4():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/rider.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE rider4
                  (id INTEGER PRIMARY KEY,
                   rider_name TEXT,
                   country TEXT,
                   poit INTEGER,
                    QAT INTEGER,
                    INA INTEGER,
                    ARG INTEGER,
                    AME INTEGER,
                    POR INTEGER,
                    SPA INTEGER,
                    FRA INTEGER,
                    ITA INTEGER,
                    CAT INTEGER,
                    GER INTEGER,
                    NED INTEGER,
                    GBR INTEGER,
                    AUT INTEGER,
                    RSM INTEGER,
                    ARA INTEGER,
                    JPN INTEGER,
                    THA INTEGER,
                    AUS INTEGER,
                    MAL INTEGER,
                    VAL INTEGER
                   )''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_rider4()

def query_all_database_and_sort_rider_by_poit():
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('database/rider.db')

    # Tạo đối tượng cursor để thực hiện câu truy vấn
    cursor = conn.cursor()

    # Sử dụng câu truy vấn SQL SELECT để lấy tất cả dữ liệu và sắp xếp theo cột 'point'
    cursor.execute('SELECT * FROM rider4 ORDER BY point')

    # Lấy tất cả các hàng kết quả
    rows = cursor.fetchall()

    # Đóng kết nối đến cơ sở dữ liệu
    conn.close()

    return data

def query_database_for_rider_by_id2( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM rider4 WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

def get_sorted_data():
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Truy vấn dữ liệu từ bảng và sắp xếp theo thứ tự giảm dần của thuộc tính "point"
    query = "SELECT * FROM rider4 ORDER BY poit DESC"
    cursor.execute(query)

    # Lấy tất cả dữ liệu từ kết quả truy vấn
    data = cursor.fetchall()

    # Đóng kết nối và trả về dữ liệu
    cursor.close()
    conn.close()
    return data

# lưu dữ liệu 
def save_data_for_rider_in_table4(rider_name, country, QAT, INA, ARG, AME, POR, SPA, FRA, ITA, CAT, GER, NED, GBR, AUT, RSM, ARA, JPN, THA, AUS, MAL, VAL):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Tính tổng giá trị các cột, đảm bảo không có giá trị None
    column_values = [QAT, INA, ARG, AME, POR, SPA, FRA, ITA, CAT, GER, NED, GBR, AUT, RSM, ARA, JPN, THA, AUS, MAL, VAL]
    # poit = sum(0 if value == "None" else value for value in column_values)
    # poit = sum(value or 0 for value in column_values)
    poit = 0
    for value in column_values:
        if value is not None:
            poit = poit + int(value)
        else:
            poit = poit + 0
    print(f"{poit}")


    # Thêm dữ liệu vào bảng rider
    cursor.execute(f"INSERT INTO rider4 (rider_name, country, poit, QAT, INA, ARG, AME, POR, SPA, FRA, ITA, CAT, GER, NED, GBR, AUT, RSM, ARA, JPN, THA, AUS, MAL, VAL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
                   (rider_name, country, poit, QAT, INA, ARG, AME, POR, SPA, FRA, ITA, CAT, GER, NED, GBR, AUT, RSM, ARA, JPN, THA, AUS, MAL, VAL))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()



# a = query_database_for_rider_by_id(1)
# id ,rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL = a
# print(a)
# print(type(a))
# print(rider_name)
# print(id)

# for i in range(11):
#     save_data_for_rider_in_table4(
#         rider_name=name[i],
#         country=countrys[i],
#         QAT=data[i][0],
#          INA=data[i][1], ARG=data[i][2], AME=data[i][3], POR=data[i][4], 
#          SPA=data[i][5] ,FRA=data[i][6] ,ITA=data[i][7] ,CAT=data[i][8],
#         GER=data[i][9], NED=data[i][10], GBR=data[i][11], AUT=data[i][12], 
#         RSM=data[i][13], ARA=data[i][14], JPN=data[i][15] ,THA=data[i][16] ,
#         AUS=data[i][17], MAL=data[i][18], VAL=data[i][19]
#         )

# print([a for a in range(10)])

def structure_of_the_table(path_to_database,table_name):
    # Kết nối đến CSDL SQLite
    conn = sqlite3.connect(path_to_database)

    # Tạo con trỏ
    cursor = conn.cursor()

    # Tên bảng cần in cấu trúc
    # table_name = 'your_table_name'

    # Thực thi câu truy vấn để lấy thông tin cấu trúc của bảng
    cursor.execute(f"PRAGMA table_info({table_name})")

    # Lấy kết quả từ câu truy vấn
    table_structure = cursor.fetchall()

    # In cấu trúc của bảng
    # print("Cấu trúc của bảng", table_name)
    # for column in table_structure:
    #     print(column)

    # Đóng kết nối và con trỏ
    cursor.close()
    conn.close()

    return table_structure

def delete_table(path_database,table_name):
    conn = sqlite3.connect(path_database)

    # Tạo đối tượng cursor
    cursor = conn.cursor()

    

    # Sử dụng lệnh SQL để xóa bảng
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Lưu các thay đổi vào cơ sở dữ liệu
    conn.commit()

    # Đóng kết nối
    conn.close()


# structure_table = structure_of_the_table(path_to_database="database/rider.db",table_name="rider4")
# print(structure_table)

# delete_table(path_database="database/rider.db",table_name="rider4")

# for i in range(15):
#     data = query_database_for_rider_by_id2(i)
#     # if data:
#     print(data)
#     # print(type(data))

# print("=================================================================")

def show_database_rider():
    data = get_sorted_data()
    # print(data)
    for d in data:
        print(d)

