import math

# Invest interest formula key and calculations:
# A = total amount once interest is applied
# P = amount user deposits
# t = number of years invested
# r = interest rated divided by 100, e.g 2% is 0.02 
# Simple interest: A = P(1 + r * t)
# Compound interest: A = P(1 + r) ^ t

# Bond repayment formula key and calcuation:
# P = is the present value of the house.
# i = is the monthly interest rate, calculated by dividing the annual interest rate by 12.
# n = is the number of months over which the bond will be repaid.
# x = amount to be paid on loan each month
# x = (i.P) / (1 - (1+i)^(-n))

# I.D 1
# This program is a financial tool that allows the user to access two financial calculators:
# 1) an investment calculator (investment)
# 2) a home loan repayment calculator (bond)
# the user chooses which type of calculation they would like to run and should not be affected by 
# upper or lower case input, an error message should print if the input is invalid

# I.D 2 - Investment 
# If the user selects "investment", they should be asked to input the following:
# 1) amount of money they are depositing
# 2) interest percentage as a "number"
# 3) number of years for the investment
# 4) type of interest, "simple" or "compound"
# 5) Output the amount they will return on their investment 

# I.D 3 - Bond
# if the user selects "bond", they should be asked to input the following:
# 1) value of the property
# 2) interest percentage as a "number" 
# 3) months they plan to make repayment for e.g "120"

# This first statement below checks which type of calculator the user would like to use, if they dont select an option then 
# an error message occurs and they have to try again until the select a correct option. 
# They will only be able to proceed once they have inputted a valid answer 

while True:
    finance_type = input("Choose either ""investment"" or ""bond"" from the menu below to proceed: \n"
"investment - to calculate the amount of interest you'll earn on your investment \n"
"bond       - to calculate the amount you'll have to pay on a home loan \n"
": ")
    finance_type = finance_type.lower()
    if finance_type == "investment".lower() or finance_type == "bond".lower():
        break
    else:
        print("ERROR! YOU HAVE NOT SELECTED AN OPTION! PLEASE TRY AGAIN")

# The if statement below is for users selecting the "investment" option. They are then given the choice of the type
# of interest the require. If they don't select an option, they will be asked to try again until the select a correct option.
# Once they have selected an interest option, they will receive the answer rounded down to 2 decimal places

if finance_type == "investment".lower():
    invest_amount = float(input("please enter the amount you wish to invest as a number only: "))
    invest_interest = float(input("please enter the interest rate amount as a number only: "))
    invest_years = float(input("please enter the years you wish to invest a number only: ")) 
    simple_interest = invest_amount * (1 + ((invest_interest/100))*invest_years)
    compound_interest = invest_amount * (math.pow((1 + invest_interest/100), invest_years))
    while True:
        interest_type = (input("which type of interest would you like? ""compound"" or ""simple"": "))
        interest_type = interest_type.lower()
        if interest_type == "simple".lower():
            print("Your total interest earnt is ", (simple_interest - invest_amount).__round__(2))
            break
        elif interest_type == "compound".lower():
            print("Your total iinterest earnt is ", (compound_interest - invest_amount).__round__(2))
            break
        else: 
            print("You have not selected an interest type")

# The if statement below is for users selecting the "bond" option. Once they input all the information required
# they will receive the answer rounded down to 2 decimal places. 

elif finance_type == "bond".lower():
                bond_amount = float(input("please enter the value of the property as a number only: "))
                bond_interest = float(input("please enter the interest rate amount as a number only: "))
                bond_interest = (bond_interest/100)/12
                bond_months = float(input("please enter the months you wish to repay the bond as a number only: ")) 
                bond_repay = (bond_amount * bond_interest) / (1 -(1 + bond_interest)**(-bond_months))
                print("Your total repayment is: ", (bond_repay).__round__(2))