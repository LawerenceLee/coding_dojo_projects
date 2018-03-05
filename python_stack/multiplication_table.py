
print("x 1 2 3 4 5 6 7 8 9 10 11 12")
row = ""
for count in range(1, 13):
    row += str(count) + " "
    for x in range(1, 13):
        row += str(count * x) + " "
    print(row)
    row = ""
