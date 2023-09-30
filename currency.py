# Eva D.
# September 27, 2023
# currency calculator to tell user how to give change most efficiently

dollars_and_cents = input("Enter an amount in dollars and cents (eg: 250.60):")
money = float(dollars_and_cents)

# gets amount of hundreds
hundred = money//100
# gets amount of fifties
change_from_hundred = money%100
fifty = change_from_hundred//50
# gets amount of twenties
change_from_fifty = money%50
twenty = change_from_fifty//20
# gets amount of tens
change_from_twenty = change_from_fifty%20
ten = change_from_twenty//10
# gets amount of fives
change_from_ten = money%10
five = change_from_ten//5
# gets amount of ones
change_from_five = money%5
one = change_from_five//1
# gets amount of quarters
change_from_one = money%1
quarter = change_from_one//.25
# gets amount of dimes
change_from_quarter = change_from_one%.25
dime = change_from_quarter//.10
# gets amount of nickels
change_from_dime = change_from_quarter%.10
nickel = change_from_dime//.05
# gets amount of cents
change_from_nickel = change_from_dime%.05
penny = change_from_nickel//.01

# tells user how much of each category they will need
print(money,"can be made with:")
print(hundred,"hundred dollar bill(s)")
print(fifty,"fifty dollar bill(s)")
print(twenty,"twenty dollar bill(s)")
print(ten,"ten dollar bill(s)")
print(five,"five dollar bill(s)")
print(one,"one dollar bill(s)")
print(quarter,"quarter(s)")
print(dime,"dime(s)")
print(nickel,"nickel(s)")
print(penny,"cent(s)")
