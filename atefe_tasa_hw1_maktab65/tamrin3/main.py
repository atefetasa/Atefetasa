def check_validation(password):
    check={'length':0,'upper':0,'lower':0,'number':0,'character':0}
    characters=['$','#','@']
    length=len(password)
    if length>=6 and length<=12:
        check.update({'length':1})
    for i in password:
        if i.isdigit()==True:
            check.update({'number':1})
        elif i.islower() == True:
            check.update({'lower': 1})
        elif i.isupper() == True:
            check.update({'upper': 1})
        elif i in characters:
            check.update({'character':1})
    return check
output=''
new_list=[]
passwords=input("please enter the passwords:").split(',')
for password in passwords:
    v=check_validation(password)
    v_list=list(v.values())
    counter=0
    for i in range(0,len(v_list)):
        if v_list[i]==1:
            counter+=1
    if counter==5:
        new_list.append(password)
if new_list==[]:
    print("none of these passwords are valid!")
else:
    for password in new_list:
        if new_list[0] == password:
            output += password
        else:
            output += ','
            output += password
    print(f"the valid passwords are:\n{output}")





