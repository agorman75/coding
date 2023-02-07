# def in_list(num):
#     for each in num:
#         new_list = []
#         new_list =+ each
#         print(each)

# in_list(list[input("Provide a list: ")])


# list_1 = []
# new_list = input("provide numbers: ")
# list_1.append(new_list)
# print(list_1)


# def list_5(nums):
#     list_2 = [nums]
#     return print(list_2)

# list_5(input("Provide a list of numbers: "))

# def list_5(nums):
#     list_2 = [nums]
#     for each in list_2:
#         if each % 2 == 0:
#             even_list = [each]
#             return print(even_list)

# list_5(input("Provide a list of numbers: "))

def list_5(nums):
    list_2 = nums.split(',')
    even_list = []
    for each in list_2:
        if int(each) % 2 == 0:
            even_list.append(each)
    return print(even_list)

list_5(input("Provide a list of numbers, separated by commas: "))