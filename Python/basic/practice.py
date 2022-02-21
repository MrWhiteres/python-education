#!/usr/bin/env python3
def hello_world():
    print("Goodbye, World! -> Hello, World!")


def variables_and_types():
    mystring, myfloat, myint = "hello", 10.0, 20
    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)


def lists():
    numbers, strings, names = [1, 2, 3], ['hello', 'world'], ["John", "Eric", "Jessica"]
    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers, strings, "The second name on the names list is %s" % names[1], sep='\n')


def basic_operators():
    x, y = object(), object()

    # TODO: change this code
    x_list, y_list, big_list = [x for _ in range(10)], [y for _ in range(10)], x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(x) == 10 and y_list.count(y) == 10:
        print("Almost there...")
    if big_list.count(x) == 10 and big_list.count(y) == 10:
        print("Great!")


def string_formatting():
    data, format_string = ("John", "Doe", 53.44), "Hello"
    print(f'{format_string} {data[0]} {data[1]}. Your current balance is ${data[-1]}.')
    # or
    format_string = "Hello %s %s. Your current balance is $%s."
    print(format_string % data)


def basic_string_operations():
    s = "Strings are awesome!"
    # Length should be 20
    print("Length of s = %d" % len(s))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % s.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % s.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % s[:5])  # Start to 5
    print("The next five characters are '%s'" % s[5:10])  # 5 to 10
    print("The thirteenth character is '%s'" % s[12])  # Just number 12
    print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
    print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

    # Convert everything to uppercase
    print("String in uppercase: %s" % s.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % s.lower())

    # Check how a string starts
    if s.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if s.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % s.split(" "))


def conditions():
    # change this code
    number = 16
    second_number = None
    first_array = [1, 2, 3]
    second_array = [4, 5]

    if number > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not second_number:
        print("6")


def loops():
    numbers = [
        951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
        615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
        743, 527
    ]

    # your code goes here
    for number in numbers:
        if number == 237:
            break
        elif number % 2 != 0:
            continue
        else:
            print(number)


def functions():
    def list_benefits():
        return ['More organized code', 'More readable code', 'Easier code reuse',
                'Allowing programmers to share and connect code together']

    # Modify this function to concatenate to each benefit - " is a benefit of functions!"
    def build_sentence(benefit):
        return f"{benefit} is a benefit of functions!"

    # or
    #   def build_sentence(benefit):
    #       return "%s is a benefit of functions!" % benefit

    def name_the_benefits_of_functions():
        list_of_benefits = list_benefits()
        for benefit in list_of_benefits:
            print(build_sentence(benefit))

    name_the_benefits_of_functions()


def classes_and_objects():
    class Vehicle:
        def __init__(self):
            pass

        name = ""
        kind = "car"
        color = ""
        value = 100.00

        def description(self):
            desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
            return desc_str

    # your code goes here
    car1, car2 = Vehicle(), Vehicle()
    car1.name, car2.name = "Fer", "Jump"
    car1.color, car2.color = "red", "blue"
    car1.kind, car2.kind = "convertible", "van"
    car1.value, car2.value = 60_000.00, 10_000.00
    # test code
    print(car1.description())
    print(car2.description())


def dictionaries():
    phonebook = {
        "John": 938477566,
        "Jack": 938377264,
        "Jill": 947662781
    }
    # your code goes here
    phonebook["Jake"] = 938273443
    phonebook.pop("Jill", None)

    # testing code
    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not listed in the phonebook.")


def modules_and_packages():
    import re

    # Your code goes here
    print(sorted([i for i in dir(re) if "find" in i]))


def numpy_arrays():
    weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    from numpy import array

    # Create a numpy array np_weight_kg from weight_kg
    np_weight_kg = array(weight_kg)

    # Create np_weight_lbs from np_weight_kg
    np_weight_lbs = np_weight_kg * 2.2

    print(np_weight_lbs)


def pandas_basics():
    # Import cars data
    from pandas import read_csv
    cars = read_csv('cars.csv', index_col=0)

    # Print out observation for Japan
    print(cars.iloc[2])

    # Print out observations for Australia and Egypt
    print(cars.loc[['AUS', 'EG']])


def generators():
    def fib():
        a, b = 1, 1
        while 1:
            yield a
            a, b = b, a + b

    # testing code
    from types import GeneratorType
    if type(fib()) == GeneratorType:
        print("Good, The fib function is a generator.")

        counter = 0
        for n in fib():
            print(n)
            counter += 1
            if counter == 10:
                break


def list_comprehensions():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = [i for i in numbers if i >= 0]
    print(newlist)


def lambda_functions():
    l = [2, 4, 7, 3, 14, 19]
    for i in l:
        # your code here
        func = lambda x: x % 2 != 0
        print(func(i))


def multiple_function_arguments():
    # edit the functions prototype and implementation
    def foo(a, b, c, *args):
        return len(args)

    def bar(a, b, c, **kwargs):
        return kwargs['magicnumber'] == 7

    # test code
    if foo(1, 2, 3, 4) == 1:
        print("Good.")
    if foo(1, 2, 3, 4, 5) == 2:
        print("Better.")
    if bar(1, 2, 3, magicnumber=6) == False:
        print("Great.")
    if bar(1, 2, 3, magicnumber=7) == True:
        print("Awesome!")


def regular_expressions():
    from re import compile, match
    def test_email(your_pattern):
        pattern = compile(your_pattern)
        emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
        for email in emails:
            if not match(pattern, email):
                print(f"You failed to match {email}")
            elif not your_pattern:
                print("Forgot to enter a pattern!")
            else:
                print("Pass")

    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"  # Your pattern here!
    test_email(pattern)


def exception_handling():
    # Setup
    actor = {"name": "John Cleese", "rank": "awesome"}

    # Function to modify!!!
    def get_last_name():
        return actor["name"].split()[1]

    # Test code
    print("All exceptions caught! Good job!")
    print(f"The actor's last name is {get_last_name()}")


def sets():
    a, b = set("Jake", "John", "Eric"), set("John", "Jill")
    print(a.difference(b))


def serialization():
    from json import loads, dumps

    # fix this function, so it adds the given name
    # and salary pair to salaries_json, and return it
    def add_employee(salaries_json, name, salary):
        # Add your code here
        salaries = loads(salaries_json)
        salaries[name] = salary
        return dumps(salaries)

    # test code
    salaries = '{"Alfred" : 300, "Jane" : 400 }'
    new_salaries = add_employee(salaries, "Me", 800)
    decoded_salaries = loads(new_salaries)
    print(decoded_salaries["Alfred"])
    print(decoded_salaries["Jane"])
    print(decoded_salaries["Me"])


def partial_functions():
    # Following is the exercise, function provided:
    from functools import partial
    def func(u, v, w, x):
        return u * 4 + v * 3 + w * 2 + x

    sol = partial(func, 5, 6, 7)
    print(sol(8))
    # Enter your code here to create and print with your partial function


def code_introspection():
    # Use the help function to see what each function does.
    # Delete this when you are done.
    # help(dir)
    # help(hasattr)
    # help(id)

    # Define the Vehicle class.
    class Vehicle:
        name = ""
        kind = "car"
        color = ""
        value = 100.00

        def description(self):
            desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
            return desc_str

    # Print a list of all attributes of the Vehicle class.
    # Your code goes here
    a = Vehicle()
    print(dir(a))


def closures():
    # your code goes here
    def multiplier_of(x):
        def multiplier(number):
            return number * x

        return multiplier

    multiplywith5 = multiplier_of(5)
    print(multiplywith5(9))


def decorators():
    def type_check(correct_type):
        # put code here
        def check(old_function):
            def new_function(arg):
                if (isinstance(arg, correct_type)):
                    return old_function(arg)
                else:
                    print("Bad Type")

            return new_function

        return check

    @type_check(int)
    def times2(num):
        return num * 2

    print(times2(2))
    times2('Not A Number')

    @type_check(str)
    def first_letter(word):
        return word[0]

    print(first_letter('Hello World'))
    first_letter(['Not', 'A', 'String'])


def map_filter_reduce():
    from functools import reduce

    # Use map to print the square of each numbers rounded
    # to three decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    # Fix all three respectively.
    map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)
