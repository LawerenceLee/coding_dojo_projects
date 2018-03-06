words = "It's thanksgiving day. It's my birthday,too!"
x = [2, 54, -2, 7, 12, 98]
y = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print(words.find("day"))
new_words = words.replace("day", "month")
print(new_words)
print(min(x))
print(max(x))
print(y[0], y[-1])
new_y = [y[0], y[-1]]
print(new_y)
x.sort()


def split_list(arr):
    if len(arr) % 2 == 0:
        half = len(arr) / 2
    else:
        half = (len(arr) - 1) / 2

    first_lst = x[:half]
    second_lst = x[half:len(arr)]
    second_lst.insert(0, first_lst)
    return second_lst


print(split_list(x))
