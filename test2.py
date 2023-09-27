import sqlite3

def find_max_id(database_path, table_name, id_column):
    try:
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Sử dụng câu lệnh SQL để truy vấn giá trị id lớn nhất trong bảng
        query = f"SELECT MAX({id_column}) FROM {table_name};"
        cursor.execute(query)

        # Lấy kết quả
        max_id = cursor.fetchone()[0]

        return max_id

    except sqlite3.Error as e:
        print("Lỗi SQLite:", e)
        return None

    finally:
        if conn:
            conn.close()

# Thay đổi đường dẫn đến cơ sở dữ liệu, tên bảng và tên cột id theo bảng của bạn
database_path = "database/history.db"
table_name = "access_history_time"
id_column = "id"

max_id = find_max_id(database_path, table_name, id_column)
if max_id is not None:
    print(f"ID lớn nhất trong bảng {table_name} là: {max_id}")
else:
    print("Không thể tìm thấy giá trị ID lớn nhất.")
