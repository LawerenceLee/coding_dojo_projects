# FOO : prime is only divisible by 1 and the number itself
# BAR : perfect square is 8 X 8 = 64
start = 100
end = 100001

is_perfect = False
is_prime = True
for x in range(start, end+1):
    for num in range(2, x-1):
        if x % num == 0:
            is_prime = False
            if x == num ** 2:
                print("Bar")
                is_perfect = True

    if is_prime and x != 1:
        print("Foo")
    elif not is_perfect and not is_prime:
        print("FooBar")
    is_prime = True
    is_perfect = False
