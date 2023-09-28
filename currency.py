
#dollars_and_cents = input("Enter an amount in dollars and cents (eg: 250.60):")
dollars_and_cents = input("Enter an amount in dollars and cents (eg: 250.60):")
money = float(dollars_and_cents)
#cents = float(dollars_and_cents)*100
'''''
hundred = round(money/100, 0)

change_from_hundred = money%100
fifty = round(change_from_hundred/50, 0)

change_from_fifty = money%50
twenty = round(change_from_fifty/20, 0)

change_from_twenty = money%twenty
ten = round(change_from_twenty/10, 0)

change_from_ten = money%10
five = round(change_from_ten/5, 0)

change_from_five = money%5
one = round(change_from_five/1, 0)
'''''

hundred = money//100

change_from_hundred = money%100
fifty = change_from_hundred//50

change_from_fifty = money%50
twenty = change_from_fifty//20

change_from_twenty = change_from_fifty%20
ten = change_from_twenty//10

change_from_ten = money%10
five = change_from_ten//5

change_from_five = money%5
one = change_from_five//1

change_from_one = money%1
quarter = change_from_one//.25

change_from_quarter = change_from_one%.25
dime = change_from_quarter//.10

change_from_dime = change_from_quarter%.10
nickel = change_from_dime//.05

change_from_nickel = change_from_dime%.05
penny = change_from_nickel//.01


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
print(penny,"pennies")
