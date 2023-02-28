# def sum_list(list_1):
#     a = 0
#     for each in list_1.split(','):
#         each = int(each)
#         a += int(each)
#     print(a)

# sum_list(input("Provide a list of numbers: "))

# def word(words):
#     larger = ""
#     for word in words:
#         if len(words) > len(larger):
#             larger = word
#     print(larger)

# word(input("Provide a list of words: ").split())

# def rev(rev_list):
#     rev_list = rev_list.split(',')
#     rev_list.reverse()
#     print(rev_list)

# rev(input())

# def even(num):
#     even_each = 0
#     for each in num:
#         each = int(each)
#         if each % 2 == 0:
#             even_each += each
#     print(even_each)

# even(input().split(','))

# def lists(l1, l2):
#     l3 = []
#     for each in l1:
#         if each in l2 and each != ',':
#             l3.append(each)
#     print(l3)

# lists(input(), input())

# def lists(l1):
#     new_list = []
#     for each in l1.split(','):
#         if len(each) >= 3:
#             new_list.append(each)
#     print(new_list)

# lists(input())

def long_words(words):
    new_list = []
    for word in words.split(','):
        if len(word) >= 3:
            new_list.append(word)
    print(new_list)

long_words(input("Enter a comma-separated list of words: "))
