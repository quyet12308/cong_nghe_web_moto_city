from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

import uvicorn
from data_processing import data_processing,data_processing2, get_Leader_arr, get_Previous_arr, get_poit_arr
from access_history import save_data_for_history_in_table,query_database_for_history_3_time_lastest
from database3 import query_database_for_admin_by_name

import datetime
import json
import pytz

from database2 import get_sorted_data
from database4 import get_empty_column2,update_column_values
from data_processing2 import data_processing3,get_finall_data
from test4 import replace_empty_with_dash

# lấy time
def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


app = FastAPI()

# cors để ko chặn trang web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sửa đổi danh sách này để chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




#get database 
@app.get("/api/get_data")
async def get_data_for_table_html():
    data_arr = get_sorted_data()# get pre-processing data
    poit_arr = get_poit_arr(data=data_arr)# get poit data
    leader_arr = get_Leader_arr(data_poit_arr=poit_arr) # make leader arr
    previous_arr = get_Previous_arr(data_poit_arr=poit_arr) # make previous arr
    time = gettime2() # get time for history
    # data = data_processing(11)
    data = data_processing2(data_arr=data_arr,Leader_arr=leader_arr,Previous_arr=previous_arr) # sort data
    # print(data)
    # print(type(data))
    save_data_for_history_in_table(time=time) # save history
    return data 

@app.get("/api/get_data2")
async def get_data_for_table_html2():
    
    time = gettime2() # get time for history
    data = get_finall_data()
    save_data_for_history_in_table(time=time) # save history
    return data 

# Testing not completed with time history
# phần test đang phát triển thêm để làm thêm phần lịch sử 
@app.get("/api/get_lastest_time")
async def get_3_lastest_time():
    data = query_database_for_history_3_time_lastest()
    data_json = json.dumps(data)
    return data_json

# hàm test
@app.post("/api/add_rider")
async def add_rider(request_data: dict):
    if request_data:
        pass

# phần lấy tên vòng đua cho phần admin page
@app.get("/api/get_the_name_of_the_race")
async def get_the_name_of_the_race():
    empty_column = get_empty_column2("rider5")
    return {"response":empty_column}


# cập nhật điểm vào database
@app.post("/api/update_the_point_of_the_race")
async def update_the_point_of_the_race(request_data: dict):
    if request_data:
        arr_data = request_data["arr_data"]
        empty_column = request_data["empty_column"]
        # print(arr_data)
        # print(empty_column)
        empty_column_ = get_empty_column2("rider5")
        if empty_column == empty_column_:
            new_arr = replace_empty_with_dash(arr=arr_data)
            update_column_values(column_name=empty_column,values=new_arr)
            
            return {"response":"updated successfully"}
        else:
            return {"response":"update failed"}
            



# @app.post("/api/is_admin")
# async def is_admin(request_data: dict):
#     if request_data:
#         data = query_database_for_admin_by_name()
#         id_ , name_ , pass_ , time = data
#         if request_data["pass"] == :
#             return {"response":{
#                 "status":True
#             }}
#         else:
#             return {"response":{
#                 "status":False
#             }}





if __name__ == "__main__":
    
    uvicorn.run("app:app",port=8001,workers=5,reload=True)






    
