a = ['QAT', 'INA', 'ARG', 'AME', 'POR', 'SPA', 'FRA', 'ITA', 'CAT', 'GER', 'NED', 'GBR', 'AUT', 'RSM', 'ARA', 'JPN', 'THA', 'AUS', 'MAL', 'VAL']
# print(len(countries))

# for i in countries:
#     print(f"{i} TEXT,")

# a = [rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL]

# for i in range(20):
#     print(f"?",end=",")

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

# dữ liệu ban đầu 
# data = [
#     [None, '1', '11', '11', '8', '25', None, '25', None, None, '25', '25', '25', '25', '20', None, '16', '16', '25', '7'],
#     ['7', '20', '8', '9', '25', '20', '13', '20', '25', '25', None, '8', '20', '11', None, '8', '0', None, '16', '13'],
#     ['25', '5', '6', '25', None, '8', '25', None, None, '6', '5', '13', None, '20', '25', '7', '10', '11', '20', '8'],
#     ['13', '7', '25', '5', '16', '16', '16', '16', '11', '13', '13', '7', '10', '10', '16', '0', '5', '7', '6', None],
#     [None, '13', '2', '16', None, '11', '20', '1', '2', '16', '10', '16', '16', '0', '11', '25', '20', None, '10', None],
#     ['20', '8', '10', '4', None, '6', '8', '9', '8', '9', '11', '5', '9', '8', '13', '20', '6', '6', '8', '20'],
#     ['9', '11', '16', '20', '13', '0', None, None, None, None, '6', '9', '8', '9', '7', None, '4', '25', '11', '25'],
#     ['8', '16', None, '7', '20', None, '11', '13', '16', '20', '3', None, '11', None, '8', '5', '13', '8', '7', None],
#     [None, None, '20', '8', None, '0', None, '3', '20', '10', '9', '11', '6', '7', '10', '16', '7', '9', None, '16'],
#     [None, '25', '3', '0', '11', '4', None, '7', '7', '7', '7', '10', '4', '5', '5', '11', '25', '4', '3', '11'],
#     ['4', '0', '9', '6', '6', '2', '6', '4', '9', None, '16', '20', '3', '16', '3', '9', '9', '0', '0', None]

# ]

# dữ liệu khi trộn
data = [
    ['9', '11', '16', '20', '13', '0', None, None, None, None, '6', '9', '8', '9', '7', None, '4', '25', '11', '25'],
    ['25', '5', '6', '25', None, '8', '25', None, None, '6', '5', '13', None, '20', '25', '7', '10', '11', '20', '8'],
    ['13', '7', '25', '5', '16', '16', '16', '16', '11', '13', '13', '7', '10', '10', '16', '0', '5', '7', '6', None],
    [None, '1', '11', '11', '8', '25', None, '25', None, None, '25', '25', '25', '25', '20', None, '16', '16', '25', '7'],
    ['7', '20', '8', '9', '25', '20', '13', '20', '25', '25', None, '8', '20', '11', None, '8', '0', None, '16', '13'],
    
    [None, '13', '2', '16', None, '11', '20', '1', '2', '16', '10', '16', '16', '0', '11', '25', '20', None, '10', None],
    ['20', '8', '10', '4', None, '6', '8', '9', '8', '9', '11', '5', '9', '8', '13', '20', '6', '6', '8', '20'],
    
    [None, '25', '3', '0', '11', '4', None, '7', '7', '7', '7', '10', '4', '5', '5', '11', '25', '4', '3', '11'],
    ['4', '0', '9', '6', '6', '2', '6', '4', '9', None, '16', '20', '3', '16', '3', '9', '9', '0', '0', None],
    
    ['8', '16', None, '7', '20', None, '11', '13', '16', '20', '3', None, '11', None, '8', '5', '13', '8', '7', None],
    [None, None, '20', '8', None, '0', None, '3', '20', '10', '9', '11', '6', '7', '10', '16', '7', '9', None, '16']

]

# poit = 0
# for value in data[0]:
#         if value is not None:
#             poit = poit + int(value)
#         else:
#             poit = poit + 0

# print(poit)

# print(data[1][2])
# for i in range(11):
#     print(i)

def chuyen_chuoi_sang_mang(chuoi):
    mang = chuoi.split(" ")
    return mang

text1 = "- 1 11 11 8 25 - 25 - - 25 25 25 25 20 - 16 16 25 7"
text2 = "7 20 8 9 25 20 13 20 25 25 - 8 20 11 - 8 0 - 16 13"
text3 = "25 5 6 25 - 8 25 - - 6 5 13 - 20 25 7 10 11 20 8"
text4 = "13 7 25 5 16 16 16 16 11 13 13 7 10 10 16 0 5 7 6 -"
text5 = "- 13 2 16 - 11 20 1 2 16 10 16 16 0 11 25 20 - 10 -"
text6 = "20 8 10 4 - 6 8 9 8 9 11 5 9 8 13 20 6 6 8 20"
text7 = "9 11 16 20 13 0 - - - - 6 9 8 9 7 - 4 25 11 25"
text8 = "8 16 - 7 20 - 11 13 16 20 3 - 11 - 8 5 13 8 7 -"
text9 = "- - 20 8 - 0 - 3 20 10 9 11 6 7 10 16 7 9 - 16"
text10 = "- 25 3 0 11 4 - 7 7 7 7 10 4 5 5 11 25 4 3 11"
text11 = "4 0 9 6 6 2 6 4 9 - 16 20 3 16 3 9 9 0 0 -"

# arr = chuyen_chuoi_sang_mang(text11)
# print(arr)
# print(len(arr))



# test4 = "QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL"
# # # test4 = "rider_name ,country ,QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL"
# arr_test4 = test4.split(",")
# print(arr_test4)
# for i in arr_test4:
#     print(f"<option value='{i}'>{i}</option>")