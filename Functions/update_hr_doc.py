hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'), 
    ('0121', 'IT', 'Mark Blick', '67000'), 
    ('0068', 'IT', 'Kahna Larsen', '112000'), 
    ('0234', 'OPS', 'Jim Smith', '54000')
] 

# ∗ Mark just reported a name change. Update Mark’s last name to Blick-Hawley. 

emp1, emp2, emp3, emp4 = hr_list    # Unpacking the list in individual tuples and assigning them variables

emp2_list = list(emp2)              # Converting emp2 for mark's info into a list to edit (can't edit tuples)
emp2_list[2]= 'Mark Blick-Hawley'   # Changed Mark's last name

emp2 = tuple(emp2_list)             # Converting it back into a tuple and reassigning it back to emp2
hr_list[1] = emp2                   # Changing the old tuple to the edited tuple in the og list


# ∗ Change Jim’s department code from OPS to CS and update his salary to 60000. 

emp4_list = list(emp4)              # Converting emp4 for Jim's info into a list to edit 

emp4_list[1] = 'CS'                 # Changing dept code from OPS to CS
emp4_list[3] = '60000'              # Changing Jim's salary to 60000

emp4 = tuple(emp4_list)             # Converting it back into a tuple and reassigning it back to emp4
hr_list[3] = emp4                   # Changing the old tuple to the edited tuple in the og list

# Using for loop to print each tuple in list

for emp in hr_list:                     
    emp_num, dept_code, name, salary = emp  # Unpacking the tuple to print individual values 
    print (f'{emp_num} | {dept_code} | {name} | ${int(salary):,}')