p = float(input("Enter the principal amount "))
r= float(input("Enter the rate "))
t = float(input("Enter the time period "))

ci = p*(1+(r/100))**t - p

print("Compound Interest is ", ci)

amount = ci+p

print(f"Total Amount after athe compound interest {amount}")
