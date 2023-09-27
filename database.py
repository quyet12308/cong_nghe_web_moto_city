import sqlite3
from test import name,data,countrys

def create_database_for_rider():
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/rider.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE rider
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

# create_database_for_rider()

def query_database_for_rider_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM rider WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data

# lưu dữ liệu 
def save_data_for_rider_in_table( rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/rider.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO rider (rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL))

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
#     save_data_for_rider_in_table(
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