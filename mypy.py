##decorator
def divi(a,b):
    print(a/b)

def check(divi):
    def func(a,b):
        if b==0:
            return("it cant divided")
        divi(a,b)
    return func

divi=check(divi) ##decorator
print(divi(4,2))