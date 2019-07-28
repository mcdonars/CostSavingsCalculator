# Gather user data
YearlyIncome = int(input("Please enter your yearly income:" ))
MonthlyExpenses = int(input("Please enter your monthly expenses: "))

# Subtract Federal Taxes and expenses

#
##
### Does not work, need to create function for Federal taxes deminishing
##
#
def Fed_Taxes(YearlyIncome):
    if (YearlyIncome > 0) and (YearlyIncome <= 9525):
        T1 = (YearlyIncome * 0.10)
        return T1
    elif (YearlyIncome > 9525) and (YearlyIncome <= 38700):
        T2 = (YearlyIncome - 9525) * 0.12
        return T2 + 952.5
        #return (YearlyIncome * 0.12) + (YearlyIncome * 0.10)
    elif (YearlyIncome > 38700) and (YearlyIncome <= 82500):
        T3 = (YearlyIncome - 38700) * 0.22
        return T3 + 3501.0 + 952.5
        # Calculate current bracket differential
        # Take away the previous brackets
        # Calculate remaining against Taxable rate

        # T3 = (40000 - 38700) = 1300 * 0.22
        # T2 = (38700 - 9525) = 29175 * 0.12
        # T1 = (9525 - 0) = 9525 * 0.12
        # TaxesTotal = T1+T2+T3



        #return (YearlyIncome * 0.22) + (YearlyIncome * 0.12) + (YearlyIncome * 0.10)


UserPaidTaxes = Fed_Taxes(YearlyIncome)
EarningsAT = YearlyIncome - UserPaidTaxes

print("Your yearly taxes are: ")
print(UserPaidTaxes)

YearlyExpenses = MonthlyExpenses * 12
print("Your yearly expenses are: " )
print(YearlyExpenses)

YearlySavings = EarningsAT - YearlyExpenses
print("Your yearly savings after taxes are: ")
print(YearlySavings)


# def User_Expense():
#     UserInput = input("Do you have any expenses? (Y or N): ")
#     if (UserInput == "Y"):
#         UserItemExpense = input("Enter expense name: ")
