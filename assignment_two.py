# Eva D
# 10/03/2023
# chatbot to calculate total cost of car and monthly payments, including interest

# defines chatbot and user's name, greets user with them
chatbot_name = "CostBot"
user_name = input("Welcome to the Car Cost Calculator! What is your name?")
print("Nice to meet you, {}!".format(user_name),"My name is {}.".format(chatbot_name))
# finds out where user is from, comments on it
user_location = input("Where are you from, {}?".format(user_name))
print("That's nice!",user_location,"is my favorite vacation spot.")
# finds out user's favorite number, responds with a value relating user's favorite number to my favorite number
user_favorite_number = float(input("I love numbers! What is your favorite number?"))
eva_favorite_number = 56
favorite_number_response = eva_favorite_number/user_favorite_number
print("You would need",favorite_number_response,"of your favorite number to make up my favorite number, 56.")
# finds out user's dream car and price
dream_car = input("What is your dream car? (eg: Ford Flex)")
print("Wow! I got to rent a",dream_car,"on vacation in",user_location,"once, and it was so fun to drive!")
car_cost = float(input("How much does a {} cost? (eg:15000)".format(dream_car)))
# comments on car's price with one of two responses depending on how expensive it is
if car_cost > 30000:
    print("Wow, that's expensive... I could go on so many vacations to",user_location,"with that money!")
elif car_cost <= 30000:
    print("Wow, that's a steal!")
# finds remaining information needed to perform calculations
loan_length_yr = float(input("If you had to take out a loan to buy the {}, how many years "
                             "would you take the loan out for?".format(dream_car)))
interest_rate_yr = float(input("How much is the annual interest rate on the car loan? It must be between 0 and 20!"))

# calculations needed to find total cost (rounded to two decimals) and monthly cost
loan_length_month = loan_length_yr*12
interest_rate_month = (interest_rate_yr/100)/12
monthly_payment = (interest_rate_month*car_cost)/(1-(1+interest_rate_month)**(-loan_length_month))
total_cost = round(float(monthly_payment)*loan_length_month,2)

# tells user total cost and monthly payment (rounded to two decimals) in currency format
print("Your monthly payment for a",dream_car,"would be ${},".format(round(monthly_payment,2)),"which would come to a total of ${}.".format(total_cost))
# says goodbye to user
print("I hope you're able to get your dream car! It would be so cool to have a",dream_car,"to drive around in.")
print("Anyways, I have to go plan my next vacation to {}. It was so nice to meet you,".format(user_location),"{}! Goodbye.".format(user_name))
