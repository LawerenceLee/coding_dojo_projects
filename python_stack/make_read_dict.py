
person = {
    "name": "Zach",
    "age": 27,
    "country": "USA",
    "language": "Python",
}


def read_dict(dictionary):
    print("My name is {}".format(dictionary['name']))
    print("My age is {}".format(dictionary["age"]))
    print("My country of birth is the {}".format(dictionary["country"]))
    print("My favorite language is {}".format(dictionary['language']))


read_dict(person)
