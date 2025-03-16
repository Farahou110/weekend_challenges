peso=int(input(f"please enter the price in pesos "))
dola=int(input(f"please enter the price in dollars "))


def toDollar(peso):
    price = peso*0.02
    if (price > dola):
         return dola 
         
    else:
         return peso
         
     
output = toDollar(peso)

print((f"the {output} price is better"))


    

