result="none"
a= int(input("no1:"))
b= int(input("no2:"))

try:
    result=a/b
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else: #else statement can be used only when except block is defined. Without except block the code thows error
    print("__else__")
finally: #finally is independent of except block, it doesnot throw error even if the except is not defined.4
    print("__finaly__") #it is used in order to close the file or to close/re establish the DB connection

print("result: {}".format(result))