def sum_digit(num):
    return sum(int(digit) for digit in str(num))

def reverse_number(num):
    return int(str(num)[::-1])

try:
    num = int(input("Enter a four-digit num: "))
    if len(str(num)) != 4:
        raise ValueError("The num must be a four-digit num.")
except ValueError as e:
    print(f"Invalid input: {e}")

    
print(f"Sum of digits: {sum_digit(num)}")
print(f"Reversed num: {reverse_number(num)}")



