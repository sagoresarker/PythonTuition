salary = int(input())
years_of_service = int(input())

if years_of_service > 5:
    #5 % = 5/100 = 1/20 = 0.05
    bonus_percnetange = 0.05
    new_salary = salary + salary*bonus_percnetange

