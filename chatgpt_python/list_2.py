# def sum_list(list_1):
#     a = 0
#     for each in list_1.split(','):
#         each = int(each)
#         a += int(each)
#     print(a)

# sum_list(input("Provide a list of numbers: "))

def word(words):
    new = []
    for [each] in words.split(','):
        print(each)

word(input("Provide a list of words: "))