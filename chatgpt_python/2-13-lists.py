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

# def find_largest_number(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# largest = find_largest_number(int(input("Provide first number: ")), int(input("Provide second number: ")), int(input("Provide third number: ")))
# print(f"The largest number of the three is: {largest}")


# def multi(x):
#     if x <= 10:
#         x = int(input("Provide a number between 1 - 9: "))
#     if x > 9:
#         for v in range(1,10):
#             print(v * x)

# x = multi(int(input("Provide a number between 1 - 9: ")))

# def multi(x):
#     while x not in range(1,10) or x == '':
#         x = int(input("Invalid input. Provide a number between 1 - 9: "))
#     if x in range(1,10):
#         for v in range(1,10):
#             print(v * x)

# multi(input("Provide a number between 1 - 9: "))

# import random

# def guess(x):
#     num = random.randint(1,100)
#     while x != num:
#         x = int(input(f"Try again: "))
#         if x > num:
#             print("Too high!")
#         if x < num:
#             print("Too low!")
#     if x == num:
# #         print("You got it!")

# # guess(input("Guess the number: "))

# def rev(a):
#     print(''.join(reversed(a)))
# rev(input("Enter in a string: "))

# def rev(a):
#     print(a[::-1])
# rev(input("Enter in a string: "))

# def string1(words):
#     count = 0
#     vow = 'aeiouAEIUO'
#     while type(words) != str:
#         words = input("Invalid input. Please provide a string: ")
#     for each in words:
#         if each in vow:
#             count += 1
#     print(count)

# string1(input("Provide string: "))

# def string1(words):
#     count = 0
#     vowels = 'aeiouAEIUO'
#     words = input("Enter a string: ")
#     while not isinstance(words, str):
#         words = input("Invalid input. Please provide a string: ")
#     for each in words:
#         if each in vowels:
#             count += 1
#     print(count)

# string1(input("Provide string: "))


# def count_vowels(words):
#     count = 0
#     vowels = 'aeiouAEIOU'
#     for char in words:
#         if char in vowels:
#             count += 1
#     print(count)

# count_vowels(input("Provide a string: "))

def first(word):
    new = word.split(' ')
    return print(new[0])

first(word = input("Provide a string: "))