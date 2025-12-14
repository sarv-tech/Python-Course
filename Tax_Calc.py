# Q. Write a program that takes salary as input. Using conditional statements, calculate the Final tax Rate based on the following rules:

# If the salary is less than 30,000, the tax rate is 5%.
# If the salary is between 30,000 and 70,000, the tax rate is 15%.
# If the salary is greater than 70,000, the tax rate is 25%.


salary = float(input("Enter the Salary: "))

if(salary < 30000):
    Final_tax_Rate = salary*0.5
elif(salary >= 30000 and salary <= 70000):
    Final_tax_Rate = salary*0.15
elif(salary > 70000):
    Final_tax_Rate = salary*0.25
else:
    print("No Salaries futher defined!!")

print("Salary is: ", salary)
print("Final Tax Rate is: ",Final_tax_Rate)
    