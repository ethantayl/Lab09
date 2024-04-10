# this is my first github addition

def decode(password):
    list1 = [int(i) for i in password]
    list1 = [str(i - 3) for i in list1]
    password = "".join(list1)
    return password


