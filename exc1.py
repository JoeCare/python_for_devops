def fib_rec(i: int) -> int:
    if i == 0 or i == 1:
        return i
    else:
        return fib_rec(i - 1) + fib_rec(i - 2)
 
squares = list(map(lambda x: x**2, range(10)))
fib_sequence = list(map(fib_rec, range(20)))

print(squares, fib_sequence)
print(squares, fib_sequence)
print(squares, fib_sequence)

my_list = [("apple", 5), ("lemon", 2), ("orange", 1)]
my_dict = dict(my_list)
print(my_dict)
print()

my_list_sorted = sorted(list(map(lambda x: x[1], my_dict.items())))
my_dict_sorted_by_key = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(list(zip(my_dict.values(), my_dict.keys())))

