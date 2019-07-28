# Gather user data
YearlyIncome = int(input("Please enter your yearly income:" ))
MonthlyExpenses = int(input("Please enter your monthly expenses: "))

# Subtract Federal Taxes

def Fed_Taxes(YearlyIncome):
    # Maximum taxable income for each tax bracket
    MTB1 = 9525
    MTB2 = 38700
    MTB3 = 82500
    # Tax rates per tax bracket
    TRB1 = 0.10
    TRB2 = 0.12
    TRB3 = 0.22

    if (YearlyIncome > 0) and (YearlyIncome <= MTB1):
        T1 = (YearlyIncome * TRB1)
        return T1
    elif (YearlyIncome > MTB1) and (YearlyIncome <= MTB2):
        T2 = (YearlyIncome - MTB1) * TRB2
        return T2 + (MTB1 * TRB1)
    elif (YearlyIncome > MTB2) and (YearlyIncome <= MTB3):
        T3 = (YearlyIncome - MTB2) * TRB3
        return T3 + (MTB2 * MTB2) + (MTB1 * TRB1)

        # Example calculation with 40,000 income
            # T3 = (40000 - 38700) = 1300 * 0.22
            # T2 = (38700 - 9525) = 29175 * 0.12
            # T1 = (9525 - 0) = 9525 * 0.10
            # TaxesTotal = T1+T2+T3

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
