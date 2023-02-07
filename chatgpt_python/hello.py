# def hello(a):
#     return print(f"this world: {a}")

# hello(a = input("what world?\n"))


# def double(one, two):
#     return print(f"The sum of the numbers you provided are: {one + two}")

# double(int(input("provide the first number: ")), int(input("Proivide second number: ")))

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# user_string = input("Enter a string: ")
# vowel_count = count_vowels(user_string)
# print("Number of vowels in the string:", vowel_count)



# hello = input("provide string")
# count = 0
# for char in hello:
#     vow = "aeiouAEIOU"
#     if char in vow:
#         count += 1
# print(count)


def insert_string(string_input):
    count = 0
    vow = "aeiouAEIOU"
    for char in string_input:
        if char in vow:
            count += 1
    int(count)
    return count

number1 = insert_string(input("Enter in string: "))
# print(f"number of vowels: {number1}")

def num(number1):
    if number1 >= 10:
        print(f"Number is {number1}")
    else:
        print(f"The number is low {number1}")

num(number1)

# if int(insert_string) > 10:
#     a = str(insert_string)
#     print(f"The sum of vowels is large. Output = {a}")
# else:
#     print("The sum is lower")

print("I went to {park} and {store}".format(park="water park", store="seven eleven"))