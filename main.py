# this is my first github addition

def decode(password):
    list1 = [int(i) for i in password]
    list2 = []
    for i in list1:
        if i >= 3:
            list2.append(i - 3)
        else:
            list2.append((i - 3) + 10)
    password = list2
    return password

