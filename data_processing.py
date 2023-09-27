import math
import json
from database import query_database_for_rider_by_id
from database2 import get_sorted_data,query_database_for_rider_by_id2

string1 = 'QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL'

def tao_mang_leader(mang):
    mang_moi = [None] * len(mang)
    mang_moi[0] = ""
    for i in range(1, len(mang)):
        mang_moi[i] = mang[0] - mang[i]
    return mang_moi

def tao_mang_Previous(mang):
    mang_moi = [None] * len(mang)
    mang_moi[0] = ""
    for i in range(1, len(mang)):
        mang_moi[i] = mang[i-1] - mang[i]
    return mang_moi

def tinh_tong_mang(mang):
    tong = 0
    for phan_tu in mang:
        if phan_tu != "-":
            tong += int(phan_tu)
    return tong
arr_test = []


def get_data(number):
    arr_data = []
    for i in range(number):
        data1 = query_database_for_rider_by_id(i+1)
        data2 = list(data1)
        arr_data.append(data2)
    return arr_data

def create_3_arr_data(arr_data):
    arr_3_arr = []
    arr_point = []
    arr_leader = []
    arr_Previous = []
    for j in arr_data:
        arr_only_number = j[3:]
        sum = tinh_tong_mang(arr_only_number)
        arr_point.append(sum)
    arr_leader = tao_mang_leader(arr_point)
    arr_Previous = tao_mang_Previous(arr_point)
    arr_3_arr.append(arr_point)
    arr_3_arr.append(arr_leader)
    arr_3_arr.append(arr_Previous)
    return arr_3_arr

# test = create_3_arr_data(get_data(11))
# print(test)
# print(type(test))

# print(get_data(5))

def data_processing(number):
    arr_tong = get_data(number=number)
    three_arr = create_3_arr_data(arr_data=arr_tong)
    arr_finish_all = []
    # print(three_arr[1][1])
    # for i in three_arr:
        # print(i)

    for i in range(number):
        arr_finish = list(arr_tong[i])
        
        arr_finish.insert(2,three_arr[0][i])
        arr_finish.insert(3,three_arr[1][i])
        arr_finish.insert(4,three_arr[2][i])
        # print(arr_finish)
        arr_finish_all.append(arr_finish)
    # print(arr_finish_all)
    arr_json = json.dumps(arr_finish_all)
    # print(arr_json)
    # print(type(arr_json))
    return arr_json
    
# data_processing()

# a = data_processing(8)
# print(a)
# print(type(a))



# a = ['-', '1', '11', '11', '8', '25', '-', '25', '-', '-', '25', '25', '25', '25', '20', '-', '16', '16', '25', '7']

# b = tinh_tong_mang(a)
# print(b)



# Ví dụ sử dụng:
# mang_cu = [265, 248, 219, 212, 189]
# # mang_moi = tao_mang_leader(mang_cu)
# mang_moi2 = tao_mang_Previous(mang_cu)
# print(mang_moi2)


#để check với thầy vụ ko phải là database trả lại tất mà còn có các bước xử lý nữa 
# a = get_data(8)
# for i in a:
#     print(i)


#database2
def get_poit_arr(data):
    poit_arr = []
    for d in data:
        poit = d[3]
        poit_arr.append(poit)
    return poit_arr
    # poit_arr = [poit_arr for d in data d[3]]

def get_Leader_arr(data_poit_arr):
    leader_arr = []
    for i in range(len(data_poit_arr)):
        if i == 0:
            leader = None
        else:
            leader = data_poit_arr[0] - data_poit_arr[i]
        leader_arr.append(leader)
    return leader_arr

def get_Previous_arr(data_poit_arr):
    Previous_arr = []
    for i in range(len(data_poit_arr)):
        if i == 0:
           Previous = None
        else:   
            Previous = data_poit_arr[i-1] - data_poit_arr[i]
        Previous_arr.append(Previous)
    return Previous_arr    

def data_processing2(data_arr,Leader_arr,Previous_arr):
    finally_data = []
    for i in range(len(data_arr)):
        data_add_2_element = list(data_arr[i])
        data_add_2_element.insert(4,Leader_arr[i])
        data_add_2_element.insert(5,Previous_arr[i])
        data_add_2_element = data_add_2_element[1::]
        data_add_2_element.insert(0,i+1)
        finally_data.append(data_add_2_element)
    # return finally_data
    arr_json = json.dumps(finally_data)
    return arr_json



# data_poit_arr = get_poit_arr(data=get_sorted_data())
# print(f"poit :{data_poit_arr}")
# print(f"leader :{get_Leader_arr(data_poit_arr=data_poit_arr)}")
# print(f"previous :{get_Previous_arr(data_poit_arr=data_poit_arr)}")


# data_arr = get_sorted_data()
# poit_arr = get_poit_arr(data=data_arr)
# leader_arr = get_Leader_arr(data_poit_arr=poit_arr)
# previous_arr = get_Previous_arr(data_poit_arr=poit_arr)
# finall_data = data_processing2(data_arr=data_arr,Leader_arr=leader_arr,Previous_arr=previous_arr)
# # print(finall_data)
# for i in finall_data:
#     print(i)