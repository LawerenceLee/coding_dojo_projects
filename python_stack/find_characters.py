word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']

new_list = []
for word in word_list:
    if "o" in word:
        new_list.append(word)

print(new_list)