#Eva D
#date
#chatbot to calculate total cost of car, including interest

chatbot_name = "CostBot"
user_name = input("Welcome to the Car Cost Calculator! What is your name?")
print("Nice to meet you,",user_name,"! My name is",chatbot_name,".")
user_location = input("Where are you from, {}?".format(user_name))
print("That's nice!",user_location,"is my favorite vacation spot.")
user_favorite_number = float(input("I love numbers! What is your favorite number?"))
favorite_number_divided = 56/user_favorite_number
print("You would need",favorite_number_divided,"of your favorite number to make up my favorite number, 56.")
dream_car = input("What is your dream car? (eg: Ford Flex)")
print("Wow! I got to rent a",dream_car,"on vacation in",user_location,"once, and it was so fun to drive!")
car_cost = float(input("How much does a {} cost?".format(dream_car)))
if car_cost > 30000:
    print("Wow, that's expensive... I could go on so many vacations to",user_location,"with that money!")
elif car_cost <= 30000:
    print("Wow, that's a steal!")
loan_length_yr = float(input("If you had to take out a loan to buy the {}, how many years "
                             "would you take the loan out for?".format(dream_car)))
interest_rate_yr = float(input("What is the annual interest rate for the car loan?"))


loan_length_month = loan_length_yr*12
interest_rate_month = (interest_rate_yr/100)/12
monthly_payment = (interest_rate_month*car_cost)/(1-(1+interest_rate_month)**(loan_length_month*-1))
dream_car_total_cost = round(float(monthly_payment)*loan_length_month,2)

print("Your monthly payment for a",dream_car,"would be",round(monthly_payment,2),"dollars, which would come to a total of",dream_car_total_cost,"dollars.")
print("I hope you're able to get your dream car! It would be so cool to have a",dream_car,"to drive around in.")
print("Anyways, I have to go plan my next vacation to {}. It was so nice to meet you,".format(user_location),"{}! Goodbye.".format(user_name))
