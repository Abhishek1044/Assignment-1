gross=int(input("Enter your Gross Income in U.S. $ : \n \t"))
dep=int(input("Enter number of dependents : \n \t "))
taxable_income= ( (gross - 10000) - dep*3000 )
Tax= taxable_income*(0.2)   # as tax rate is 20 % i.e. 20/100 which is 0.2 as factor for multiplication
print(f"Your Tax is : {Tax}")
