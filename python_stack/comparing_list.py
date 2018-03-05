list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
nums_one = [1,2,5,6,5]
nums_two = [1,2,5,6,5,3]
other_one = [1,2,5,6,5,16]
other_two = [1,2,5,6,5]
str_one = ['celery','carrots','bread','milk']
str_two = ['celery','carrots','bread','cream']

lists = [[list_one, list_two], [nums_one, nums_two], [other_one, other_two], [str_one, str_two]]

for val in lists:
    if val[0] == val[1]:
        print("The lists are the same")
    else:
        print("The lists are not the same")