List_Color = [
    ["Black", "Red", "Maroon", "Yellow"], 
    ["000000", "FF0000", "800000", "FFFF00"]
]

col_name = List_Color[0]
col_code = List_Color[1]

dict_color = [{'colorName': name, 'colorCode': code} for name, code in zip(col_name, col_code)]

print(dict_color)
