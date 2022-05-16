# dict1 = {"key1": "val1",
#          "key2": "val2",
#          "key3": "val3"}
#
# print(dict1.items())
# print(dict1["key1"])
#
#
# def send(**kwargs):
#     print(kwargs)
#     for x, y in kwargs.items():
#         print(x)
#         print(y)
#
#
# send(name="sarvesh", age=28, avg_marks=91)


def change_list(list1):
    print("inside function")
    print(list1)
    list1.append("grapes")
    print(list1)


list1 = ["orange", "apple", "banana"]
print("outside function")
print(list1)
change_list(list1)
print(list1)