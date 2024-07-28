# To print Alphabet pyramid
def print_pattern(x):
    length = x 
    
    for i in range(length):
       
        for j in range(length - i - 1):
            print(' ', end='')
        
        for k in range(i + 1):
            print(chr(65 + k), end='')
        print()

max = int(input("Give your maximum number of length to be displayed in pattern:"))
print_pattern(max)



#To print * pattern
def pyramid(n):
    if n > 0:
        pyramid(n - 1)
        
        print('*' * n)

r = int(input("Enter the number of rows you want to display: "))

pyramid(r)

