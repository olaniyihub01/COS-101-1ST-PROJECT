print("Yusuf and sons limited")

principal = float(input("kindly enter the initial principal amount: ")) 

rate = float(input("kindly enter the interest rate: "))

time = float(input("kindly enter the time period in years: "))

n = int(input("kindly enter the number of times interest is applied per time period: ")) 

simple_interest = principal * (1 + rate * time)

compound_interest = principal * (1 + rate / n) ** (n * time)

print("Business Name: Yusuf and Sons limited") 

print("Simple Interest: ", simple_interest) 

print("Compound Interest: ", compound_interest)