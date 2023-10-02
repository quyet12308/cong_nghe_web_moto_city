# import sqlite3

# # Kết nối đến cơ sở dữ liệu SQLite
# conn = sqlite3.connect('database/rider.db')

# # Tạo đối tượng cursor
# cursor = conn.cursor()

# # Tên của bảng bạn muốn xóa
# table_name_to_delete = 'rider5'

# # Sử dụng lệnh SQL để xóa bảng
# cursor.execute(f"DROP TABLE IF EXISTS {table_name_to_delete}")

# # Lưu các thay đổi vào cơ sở dữ liệu
# conn.commit()

# # Đóng kết nối
# conn.close()