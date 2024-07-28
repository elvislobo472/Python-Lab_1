def last_element(inp_tup):
    return [element[-1] for element in inp_tup]

inp_tup = ("python", "tuple", "includehelp", "Database", "Networks")
op = last_element(inp_tup)
print(op)
