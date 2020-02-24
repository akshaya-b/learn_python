import json
myJSON = '{"name":"John", "age":31, "city":"New York"}'

#to convert a dictionary to json format: use dumps
print(json.dumps(myJSON)) # dumps can take any collection item(list,tuple,int,float) as argument but except *sets*

with open(r"C:\Users\aksha\OneDrive\Documents\demo_jsoon.json", 'w') as fh:
    fh.write(json.dumps(myJSON))

with open(r"C:\Users\aksha\OneDrive\Documents\demo_jsoon.json", 'r') as fh:
    print ((fh.read())) #type is string
    ff=json.loads(fh.read()) #this parse string to json format
    print(type(ff)) #now the type of ff is dict