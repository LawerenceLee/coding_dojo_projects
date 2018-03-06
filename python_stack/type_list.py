a = [2, 3, 1, 7, 4, 12]
b = ['magical', 'unicorns']
c = ['magical unicorns', 19, 'hello', 98.98, 'world']

lsts = [a, b, c]
for lst in lsts:
    char = ''
    summed = 0
    for val in lst:
        if type(val) == int or type(val) == float:
            summed += val
        else:
            char += " " + val
    if summed and char:
        print("The list you entered is of mixed type.")
        print("Sum: {}".format(summed))
        print("String:{}".format(char))
    elif summed:
        print("The list you entered is of number type")
        print("Sum: {}".format(summed))
    elif char:
        print("The list you entered is of string type")
        print("String: {}".format(char))
    print("")
