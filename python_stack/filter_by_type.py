sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1, 7, 4, 21]
mL = [3, 5, 7, 34, 3, 2, 113, 65, 8, 89]
lL = [4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']

values = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]
for val in values:
    if type(val) == int:
        if val >= 100:
            print("That's a big number!")
        else:
            print("That's a small number")
    elif type(val) == str:
        if val >= 50:
            print("Long sentence")
        else:
            print('Short Sentence')
    elif type(val) == list:
        if len(val) >= 10:
            print("Big list!")
        else:
            print("Small list")



