import math
import json

from database4 import query_database_for_rider_by_id5

# def get_sum_of_poit():
def get_poit_arr(data):
    poit_arr = []
    for d in data:
        poit = d[2]
        poit_arr.append(poit)
    return poit_arr
    # poit_arr = [poit_arr for d in data d[3]]

def get_Leader_arr(data_poit_arr):
    leader_arr = []
    for i in range(len(data_poit_arr)):
        if i == 0:
            leader = None
        else:
            leader = int(data_poit_arr[0]) - int(data_poit_arr[i])
        leader_arr.append(leader)
    return leader_arr

def get_Previous_arr(data_poit_arr):
    Previous_arr = []
    for i in range(len(data_poit_arr)):
        if i == 0:
           Previous = None
        else:   
            Previous = int(data_poit_arr[i-1]) - int(data_poit_arr[i])
        Previous_arr.append(Previous)
    return Previous_arr    


def get_poit_for_rider5_table_by_id(id):
    data_list = query_database_for_rider_by_id5(id=id)
    
    data_list1 = data_list[1:]
    data_list1 = list(data_list1)
    data_list_name_and_country = data_list1[0:2]
    data_list_poits = data_list1[2:]
    total = 0
    for num in data_list_poits:
        if num != "-" and num is not None:
            total += int(num)
    data_list1.insert(2,total)
    # print(data_list1)
    # print(type(data_list1))
    # print(data_list_name_and_country)
    # print(data_list_poits)
    # print(f"poit = {total}")
    return data_list1

def data_processing3(data_arr,Leader_arr,Previous_arr):
    finally_data = []
    for i in range(len(data_arr)):
        data_add_2_element = list(data_arr[i])
        data_add_2_element.insert(3,Leader_arr[i])
        data_add_2_element.insert(4,Previous_arr[i])
        # data_add_2_element = data_add_2_element[1::]
        data_add_2_element.insert(0,i+1)
        finally_data.append(data_add_2_element)
    # return finally_data
    arr_json = json.dumps(finally_data)
    return arr_json
    # return finally_data

def get_all_data():
    all_data = []
    for i in range(11):
        a = get_poit_for_rider5_table_by_id(i+1)
        all_data.append(a)
    # sorted_arrays = sorted(all_data, key=lambda x: x[2], reverse=False)
    sorted_arrays = sorted(all_data, key=lambda x: x[2], reverse=True)
    return sorted_arrays

def get_finall_data():
    all_data = get_all_data()
    # print(all_data)

    poit_arr = get_poit_arr(data=all_data)
    leader_arr = get_Leader_arr(data_poit_arr=poit_arr)
    Previous_arr = get_Previous_arr(data_poit_arr=poit_arr)
    b = data_processing3(data_arr=all_data,Leader_arr=leader_arr,Previous_arr=Previous_arr)
    # print(b)
    return b



# for i in range(11):
#     a = get_poit_for_rider5_table_by_id(id=i+1)
#     print(a)

