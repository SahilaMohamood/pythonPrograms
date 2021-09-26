employees = [{"e.id":101,"e_name":"Ram","salary":25000,"department":"Testing","Exp":1},
            {"e.id":102,"e_name":"kalam","salary":35000,"department":"project manager","Exp":5},
            {"e.id":103,"e_name":"Raghav","salary":15000,"department":"Trainee","Exp":0},
            {"e.id":104,"e_name":"Remya","salary":25000,"department":"Developer","Exp":1},
            {"e.id":105,"e_name":"Abhi","salary":20000,"department":"Data Analyst","Exp":1}]

e_names = list(map(lambda employee:employee["e_name"],employees))
print(e_names)
# print employee names only
# for employee in employees:          # map case
#     print(employee["e_name"])

# print employee names in uppercase
# for employee in employees:          # map case
#     print(employee["e_name"].upper())

e_upper = list(map(lambda employee:employee["e_name"].upper(),employees))
print(e_upper)
# print employee name who working as Developer
# for employee in employees:          # filter case
#     if (employee["department"]=="Developer"):
#         print("Developer",employee["e_name"])

developers=list(filter(lambda employee:employee["department"]=="Developer",employees))
print(developers)

developer_name=list(map(lambda developer:developer["e_name"],developers))
print(developer_name)

# total sum of salary
summ=0           # reduce case
for employee in employees:
    summ+=employee["salary"]
print(summ)

salary=sum(list(map(lambda emp:emp["salary"],employees)))
print(salary)


lst=list()      #list is a class
lst.append(10)
print(lst)

#builtins.py
#map(),sum(),print(),..
# reduce directly not available we have to import that module functools


# print employee names name starting with "a" #map case

# print highest salary # reduce case
# lowest salary # reduce case
# add bonus of 5000rd for developer #filter