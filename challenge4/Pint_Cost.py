def calculations(b):
    calculated = 40 + (b * 5)
    tax = 0.1 * calculated
    total = calculated + tax
    return round(total)  

b = int(input("Please enter the number of colours you need: "))  
total = calculations(b)  

print(f"Your total expenditure is Ksh {total}") 
