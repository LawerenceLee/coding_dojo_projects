def odd_even():
    even_or_odd = ""
    for x in range(1, 2001):
        if x % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
        print("Number is {}.  This is an {} number.".format(x, even_or_odd))


def multiply(lst, multiplier):
    for num, val in enumerate(lst):
        lst[num] = val * multiplier
    return lst


def layered_multiples(arr):
    full_lst = [] 
    for val in arr:
        lst_of_lst = []
        for _ in range(val):
            lst_of_lst.append(1)
        full_lst.append(lst_of_lst)
    return full_lst


odd_even()
print(multiply([2, 4, 10, 16], 5))
print(layered_multiples(multiply([2, 4, 5], 3)))
