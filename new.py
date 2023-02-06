# for i in range(1,11):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")



# def num(n):
#     while n != 5:
#         n = int(input('try again: '))
#         if n == 5:
#             print("Done!")

# num(int(input("try: ")))

import random
# print(random.randint(int(input("provide number: ")), 2))

print(random.randint(2, int(input("provide number: ")) if int(input("provide number: ")) > 2 else 2))
