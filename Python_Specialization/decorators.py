def decor(func):
    def wrap(x):
        print("***")
        func(x)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input())