name = input()
salary = float(input())
sales_amount = float(input())

increment = (sales_amount * 15) /100

new_salary = salary + increment

print("TOTAL = R$ {:.2f}".format(new_salary))
