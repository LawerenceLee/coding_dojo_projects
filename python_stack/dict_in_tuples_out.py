my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def dict_to_tuple(dictionary):
    lst = []
    for key, value in dictionary.items():
        lst.append((key, value))
    return lst


print(dict_to_tuple(my_dict))
