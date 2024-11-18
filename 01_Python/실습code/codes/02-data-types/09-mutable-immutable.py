# immutable(불변)
my_str = 'hello'
my_str[0] = 'z' # TyoeError

# mutable(가변)
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]