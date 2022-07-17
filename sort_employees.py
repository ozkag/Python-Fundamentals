def sort_employees(employees, sort_by):
    name_list = []
    age_list = []
    salary_list = []
    new_list = []

    if sort_by == "name":
        
        for i in range(len(employees)):
            name_list.append(employees[i][0])

        name_list = sorted(name_list)

        for j in range(len(name_list)):
            for k in range(len(employees)):
                if name_list[j] == employees[k][0]:
                    new_list.append(employees[k])


    if sort_by == "age":
        for el in range(len(employees)):
            age_list.append(employees[el][1])

        age_list = sorted(age_list)

        for m in range(len(age_list)):
            for n in range(len(employees)):
                if age_list[m] == employees[n][1]:
                    new_list.append(employees[n])

    if sort_by == "salary":
        for val in range(len(employees)):
            salary_list.append(employees[val][2])

        salary_list = sorted(salary_list)

        for kk in range(len(salary_list)):
            for gt in range(len(employees)):
                if salary_list[kk] == employees[gt][2]:
                    new_list.append(employees[gt])

    return new_list




            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    