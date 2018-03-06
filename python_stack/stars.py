# Part 1
def draw_stars(lst):
    for item in lst:
        print(item * "*")


draw_stars([4, 6, 1, 3, 5, 7, 25])
print("")


# Part 2
def draw_starz(lst):
    for item in lst:
        if isinstance(item, int):
            print(item * "*") 
        elif isinstance(item, str):
            print(item[0].lower() * len(item))


draw_starz([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])