
def ask_list(even):
    even_list = [even]
    for each in even_list:
        new_even_list = []
        if int(each) % 2 == 0:
            new_even_list.append(each)
    print(new_even_list)

ask_list(input("Provide a list: "))