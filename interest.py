#Eva D
#september 27 2023
# Compund interest calculator
principal_amount_p = 10000
n = 12
interest_rate_r = .08
years_t = 10

final_amount_a = principal_amount_p*(1+(interest_rate_r/n))**(n*years_t)
print("The amount of compound interest is",final_amount_a,"dollars.")