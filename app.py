from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

import uvicorn
from data_processing import data_processing,data_processing2, get_Leader_arr, get_Previous_arr, get_poit_arr
from access_history import save_data_for_history_in_table,query_database_for_history_3_time_lastest


import datetime
import json
import pytz

from database2 import get_sorted_data


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


app = FastAPI()

# cors
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

# Testing not completed with time history
@app.get("/api/get_lastest_time")
async def get_3_lastest_time():
    data = query_database_for_history_3_time_lastest()
    data_json = json.dumps(data)
    return data_json


if __name__ == "__main__":
    
    uvicorn.run("app:app",port=8001,workers=5,reload=True)






    
