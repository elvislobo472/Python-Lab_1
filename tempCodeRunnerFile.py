A = ['abc', 'xyz', 'aba', '1221', 57, 'xoy', 'pop', 'Troy', 656]

def string_check(n):
    palin = []
    
    for index, element in enumerate(n):
        if isinstance(element, str) and element[0] == element[-1]:
            palin.append((element, index))
    
    if palin:
        print("Strings with identical first and last characters and their index position:")
        for string, index in palin:
            print(f"Index: {index}, String: '{string}'")
    else:
        print("No strings found with identical first and last characters.")

string_check(A)
