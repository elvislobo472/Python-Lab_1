my_list = [15, 10, 33, 44, 59]

n = len(my_list)

# print(no_elements)

# ad_val = 0
# def add():
#     global ad_val
#     for e in range(0, len(my_list)):
#         ad_val = ad_val + my_list[e]
# add()
# print(ad_val)


# mul_val = 1
# def mul():
#     global mul_val
#     for e in range(0, len(my_list)):
#             mul_val = mul_val * my_list[e]

# mul()
# print(mul_val)


big_num = my_list[0]

# def big():
#      global big_num
#      for e in range(0, n):
#           if my_list[e] > big_num:
#                big_num = my_list[e]

# big()
# print(big_num)


sm_num = my_list[0]
def sma():
    global sm_num
    for e in range(0, n):
          if my_list[e] < sm_num:
               sm_num = my_list[e]

sma()
print(sm_num)
