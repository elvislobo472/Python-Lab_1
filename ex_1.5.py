def even_sqr(begin, end):
    print(f"Even numbers and their squares in the range ({begin}, {end}):")
    for num in range(begin, end + 1):
        if num % 2 == 0:
            print(f"{num} : {num**2}")

even_sqr(1, 50)

print("\n") 

even_sqr(1, 100)




