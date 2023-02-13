# def c_list(grocery, new):
#     grocery.append(new)
#     return grocery

# grocery = []
# print(c_list(grocery, input()))

# def grocery(list):
#     list = []
#     new_items = input("What would you like in your grocery list: ")
#     list.append(new_items)
#     return

# print(grocery(list))


# def grocery(list):
#     list = []
#     new_items = input("What would you like in your grocery list (separated by commas): ")
#     items = new_items.split(",")
#     done = 'done'
#     done.lower()
#     if new_items != done:
#         for item in items:
#             list.append(item.strip())
#         return list
#     return "You cancelled."

# print(grocery([]))

# def counters(x = int(input("Provide the ending: "))):
#     for each in range(x):
#         print(each)

# print(counters())

# def add_two(a, b, c):
#     if a > b or a > c:
#         return print(f"{a} is the larger number of the three.")
#     elif b > a and b > c:
#         return print(f"{b} is the larger number of the three.")
#     else:
#         return print(f"{c} is the larger number of the three.")

# add_two(int(input("Provide first number: ")), int(input("Provide second number: ")), int(input("Provide third number: ")))

# # a = int(input())
# # b = int(input())
# # print(a + b)

def find_largest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

largest = find_largest_number(int(input("Provide first number: ")), int(input("Provide second number: ")), int(input("Provide third number: ")))
print(f"The largest number of the three is: {largest}")
