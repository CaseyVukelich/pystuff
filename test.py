import json, re

string = ""
file_name = input("Enter JSON file: ")
file = open(file_name, "r")

def concat(input):
    global string
    string += " " + "".join(input)

content = json.loads(file.read())
file.close()

for i in content:
    for k, v in i.items():        
        if type(v) == dict:            
            for item in v:
                concat(v[item])    
        else:
            concat(v)

for elmt in ["a*", "a?", "a+", "a{3}", "(a){2}"]:
    print(re.findall(elmt, string))