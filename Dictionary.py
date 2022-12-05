"""
> key:value
> key always unique
> changeable

"""

my_dict = {}
print(type(my_dict))  # <class 'dict'>
print(my_dict)

my_dict_2 = dict()
print(type(my_dict_2))  # <class 'dict'>
print(my_dict_2)

my_dict = {
    # key : value,
    "name": ["Hasan Mahmud", "Mahmud Hasan"],
    'courseName': "Python",
    "rollNum": 151010,
    1: 505,
    'permissionId': [1, 2, 3, 4, 5],
    2: 505
    # [1, 2, 3, 4]: 1 -> Invalid
}

print(my_dict['name'][1])
print(my_dict.get("name"))

print(my_dict.get("age"))  # None
# print(my_dict['age'])  # KeyError: 'age'

my_dict["name"] = "Mahmud Hasan"
print(my_dict)

my_dict["age"] = 27
print(my_dict)

my_dict.pop("name")
print(my_dict)

my_dict.clear()
print(my_dict)
