def add_function(dictionary,key,value):
    if dictionary.get(key):
        x=False
    else:
        dictionary[key]=value
        x=dictionary
    return x
def remove_function(dictionary,key,value):
    if dictionary.get(key):
        if dictionary.get(key)==value:
            dictionary.pop(key)
            x=dictionary
        else:
            print("the submitted value is invalid!")
            x=False
    else:
        print("the submitted key value does not exist!")
        x=False
    return x
dictionary={}
for i in range(5):
    key=input("please enter the key: ")
    value=input("please enter the value:")
    y=add_function(dictionary,key,value)
    if y==False:
        print(f"error:the {key} key alreary exists in the dictionary!")
    else:
        print(f"the key {key} and value {value} has been succesfully added to the dictionary!")
print(dictionary)
key = input("please enter the key: ")
value = input("please enter the value:")
operator = input(f"which operator do you want to execute on {key} and {value}:")
if operator=='add':
    y = add_function(dictionary, key, value)
    if y==False:
        print(f"error:the {key} key alreary exists in the dictionary!")
    else:
        print(f"the key {key} and value {value} has been succesfully added to the dictionary!")
        print(dictionary)
if operator=='remove':
    y=remove_function(dictionary,key,value)
    if y!=False:
        print(f"the key {key} and the value {value} has been deleted from the dictionary succesfully!")
print(dictionary)













