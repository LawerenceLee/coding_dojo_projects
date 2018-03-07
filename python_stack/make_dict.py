name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = [
    "horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(lst1, lst2):
    animal_dict = {}
    for x in range(len(lst1)):
        animal_dict[lst1[x]] = lst2[x]
    print(animal_dict)


make_dict(name, favorite_animal)
