a = [2, 3, 1, 7, 4, 12]
b = ['magical', 'unicorns']
c = ['magical unicorns', 19, 'hello', 98.98, 'world']

lsts = [a, b, c]
for lst in lsts:
    lst.sort()
    char = ''
    sumed = 0
    for val in lst:
        if type(val) == int or type(val) == float:
            sumed += val
        else:
            char += " " + val
    if sumed and char:
        print("The list you entered is of mixed type.") 
        print("Sum: {}".format(sumed))
        print("String:{}".format(char))
    elif sumed:
        print("The list you entered is of integer type")
        print("Sum: {}".format(sumed))
    elif char:
        print("The list you entered is of string type")
        print("String: {}".format(char))
    print("")

