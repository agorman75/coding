# Exercise: Print the multiples of 3 from 3 to 30 using a for loop

# for each in range(3,31):
#     a = 3 * each
#     if a % 3 == 0:
#         print(a)

# for each in range(3,31):
#     print(3 * each)

# Exercise: Print all the numbers from 1 to 100 that are divisible by 3 and 5.

# for each in range(1,101):
#     if each % 3 == 0 and each % 5 == 0:
#         print(each)
    

def div(start, end):
    for each in range(start, end):
        if each % 3 == 0 and each % 5 == 0:
            print(each)

div(1,100)