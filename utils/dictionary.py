import sys

def main():
    # list comprehension to print
    # all the dictionary methods
    dict_methods = [method for method in dir(dict) if not method.startswith("__")]
    print(dict_methods)

    # dictionary object containing three
    # key: value pairs initially
    my_dict = {
        'C': 'Dennis Ritchie ',
        'C++': 'Bjarne Stroustrup',
        'Python': 'Guido van Rossum',
        'Java': 'James Gosling'
            }
    print(my_dict['Java'])

    # clear all the items
    #  inside my_dict
    my_dict.clear()
    print(my_dict)

    my_dict = {
        'C': 'Dennis Ritchie ',
        'C++': 'Bjarne Stroustrup',
        'Python': 'Guido van Rossum',
        'Java': 'Assaf Badiri'
            }
    #Python dictionaries are indexed by keys, and it is mutable in nature. Except its keys are immutable types and values can support either mutable or immutable types.
    # copy my_dict items into my_2nd_dict
    my_2nd_dict = my_dict.copy()
    print(my_dict['Java'])
    print(my_2nd_dict['Java'])

    my_dict['Java'] = "Yogev"
    print(my_dict['Java'])
    print(my_2nd_dict['Java'])

    my_2nd_dict['Java'] = "Arazi"
    print(my_dict['Java'])
    print(my_2nd_dict['Java'])

    # tuple items as keys
    dict_keys = ("C", "C++", "Python", "Java")
    dict_values = {'Assaf1','Badiri1','Yogev2','Arazi2'}
    d = dict(zip(dict_keys, dict_values))
    print(d)
    print([*d])
    print(*d,)
    print({*d})
    # create my_dict from fromkeys() methods
    # with default value: None
    my_dict = dict.fromkeys(dict_keys)
    print("All keys value set to None")
    print(my_dict) # contains all values as None
    # with value: Programmer
    my_dict = dict.fromkeys(dict_keys, "Programmer")
    print("All keys value set to Programmer")
    print(my_dict) # contains all values as Programmer

    # change get() default value
    swift_value = my_2nd_dict.get("C++", "Not exist")
    print(swift_value)

    # use items() method in my_dict
    my_dict_items = my_dict.items()
    print(my_dict_items)

    # use values() method in my_dict
    my_dict_values = my_dict.values()
    print(my_dict_values)

    # use keys() method in my_dict
    my_dict_keys = my_dict.keys()
    print(my_dict_keys)

    # use pop() to remove Python
    # and return its value
    remove_python = my_dict.pop("Python")
    print(remove_python)
    # check if Python remove
    print(my_dict)

    # popitem() remove last item inserted
    last_item = my_dict.popitem()
    print("Last item ->", last_item)
    print("my_dict updated as Java removed")
    print(my_dict)

    # add new key JavaScript with value
    my_dict.setdefault("JavaScript", "Brendan Eich")
    # add new key Kotlin without value
    my_dict.setdefault("Kotlin")
    # new key: value are added
    print(my_dict)

    # create new dict object to pass
    # as iterable
    new_dict = {'C': 'Sir Dennis', 'Python': 'Van Rossum'}
    # use update() to update values in my_dict
    my_dict.update(new_dict)
    print("Update the value with keys already existed")
    print(my_dict)

if __name__ == '__main__':
    main()
