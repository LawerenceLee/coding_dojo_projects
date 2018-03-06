students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]


def print_dict(lst):
    for dictionary in lst:
        print("{} {}".format(
            dictionary["first_name"], dictionary['last_name']))


print_dict(students)
print("")

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }


def parse_dict(dictionary):
    for group_name, group_dict in dictionary.items():
        print(group_name)
        for item in group_dict:
            name = item['first_name'] + " " + item['last_name']
            print("{} - {} - {}".format(
                group_dict.index(item)+1, name, len(name)-1))


parse_dict(users)
