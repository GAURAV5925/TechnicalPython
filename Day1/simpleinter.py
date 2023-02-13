p = float(input("Enter the principal amount "))
r = float(input("Enter the rate "))
t = float(input("Enter the time "))

si = (p*r*t)/100

print("Simple Interest is", si)

amount = p + si

print(f"Total Amount after{t} years will be {amount}")

#another way to print
# print(f"Simple Interest is {si}")
# print("Simple Interest is {}".format(si))
