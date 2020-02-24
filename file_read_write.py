#file_handler= open(r"C:\Users\aksha\OneDrive\Documents\newfile.txt", 'w')
file_handler= open(r"C:\Users\aksha\OneDrive\Documents\newfile.txt", 'a')
try:
    for i in range(10):
        file_handler.write("line number {}\n".format(i+1))
finally:
    file_handler.close()

#instead of above set of code.. python provide us a short cut that includes try and
# finally blocks built inside within the particular set of code.

with open(r"C:\Users\aksha\OneDrive\Documents\newfile.txt", 'a') as file_handler:
    for i in range(10):
        file_handler.write("line number {}\n".format(i+1))

#read file
with open(r"C:\Users\aksha\OneDrive\Documents\newfile.txt", 'r') as file_handler:
    print(file_handler.readlines()[4])

