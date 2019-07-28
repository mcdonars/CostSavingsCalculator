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
        return (YearlyIncome * 0.10)
    elif (YearlyIncome > 9525) and (YearlyIncome <= 38700):
        return (YearlyIncome * 0.12) + (YearlyIncome * 0.10)
    elif (YearlyIncome > 38700) and (YearlyIncome <= 82500):
        return (YearlyIncome * 0.22) + (YearlyIncome * 0.12) + (YearlyIncome * 0.10)


UserPaidTaxes = Fed_Taxes(YearlyIncome)
EarningsAT = YearlyIncome - UserPaidTaxes

print("Your yearly taxes are: ")
print(EarningsAT)

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
