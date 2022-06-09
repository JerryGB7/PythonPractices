from operator import itemgetter

def sort_employees(employees, sort_by):
    if sort_by == "name":
        name_sort = sorted(employees, key=itemgetter(0))
        return name_sort
    elif sort_by == "age":
        age_sort = sorted(employees, key=itemgetter(1))
        return age_sort
    elif sort_by == "salary":
        salary_sort = sorted(employees, key=itemgetter(2))
        return salary_sort