students={4:{"name":"ARCHI","cgpa":9.1,"dept":"CSE","gen":"FEMALE"},
          5:{"name":"PAVAN","cgpa":8.2,"dept":"CSM","gen":"MALE"},
          9:{"name":"SREEVIDYA","cgpa":9.4,"dept":"CSD","gen":"FEMALE"},
          3:{"name":"SASI","cgpa":8.8,"dept":"CSE","gen":"MALE"},
          8:{"name":"LATHA","cgpa":7.9,"dept":"IT","gen":"FEMALE"},
         }
print("-"*50)
print("| {:<5}| {:<12}| {:<7}| {:<7}| {:<7} |".format("ID","NAME","CGPA","DEPT","GENDER"))
print("-"*50)
for id,info in students.items():
    print("| {:<5}| {:<12}| {:<7}| {:<7}| {:<7} |".format((id),info["name"],info["cgpa"],info["dept"],info["gen"]))
    

print("-"*50)
