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
first_lst = x[0:len(x)/2]
second_lst = x[len(x)/2:len(x)]
second_lst.insert(0, first_lst)
print(second_lst)