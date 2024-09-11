my_list = [15, 10, 33, 44, 59]

ad_val = 0
def add():
    global ad_val
    ad_val = sum(my_list)
add()
print(ad_val)

mul_val = 1
def mul():
    global mul_val
    for e in my_list:
        mul_val *= e
mul()
print(mul_val)

big_num = my_list[0]
def big():
    global big_num
    for e in my_list:
        if e > big_num:
            big_num = e
big()
print(big_num)

sm_num = my_list[0]
def sma():
    global sm_num
    for e in my_list:
        if e < sm_num:
            sm_num = e
sma()
print(sm_num)
