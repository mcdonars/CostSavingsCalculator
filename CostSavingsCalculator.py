"""
 NOTES: 
    Deductions reduce state and federal taxes only on Traditional 401k and IRA
    No deductions on ROTH 401k and ROTH IRA (Deductions when withdrawn)
    SS and Medicare are not deductable
    401K - Max contribution = 18,500  (Both Traditional and ROTH total)
    IRA - Max contribution = 6,000    (Both Traditional and ROTH total)
"""

Continue = True
while (Continue == True):

    # Gather user data
    YearlyIncome = int(input("Please enter your yearly income:" ))
    MonthlyExpenses = int(input("Please enter your monthly expenses: "))

    '''
    Psuedocode for entering more than one expense (function with array)
    1. Ask for if user has expenses
    2. User enters expense
    3. Expense is entered into array. (objects?)
    4. Loop 1-3
    5. User finally enters no, exit loop
    6. Sums all expenses, at the end displays expense total to the user.

    Enter error checking for all inputs - Regular expressions?

    '''

    # do error checking for above contrib amounts
    UserContributes = str(input("Do you contribute to retirement savings? (Y/N): "))
    if ((UserContributes == "Y") or (UserContributes == "y")):
        boolContinue = False
        while (boolContinue == False):
            ContribT401k = int(input("Please enter your monthly Traditional 401k contributions: "))
            ContribTIRA = int(input("Please enter your monthly Traditional IRA contributions: "))
            ContribR401k = int(input("Please enter your monthly ROTH 401k contributions: "))
            ContribRIRA = int(input("Please enter your monthly ROTH IRA contributions: "))

            
            if ((ContribT401k + ContribR401k <= 18500) and (ContribTIRA + ContribRIRA <=6000)):
                boolContinue = True
            else:
                boolContinue = False
                print("Maximum yearly contribution for 401K is 18,500 and IRA  is 6,000")
                
    else:
        pass

    MonthyContributions = ContribT401k + ContribR401k + ContribTIRA + ContribRIRA
    MonthyContributionsTD = ContribT401k + ContribTIRA

    # Subtract Contributions
    TaxableIncome = YearlyIncome - (MonthyContributionsTD * 12)

    # Subtract Federal Taxes
    def Fed_Taxes(TaxableIncome):
        # Maximum taxable income for each tax bracket
        MTB1 = 9525
        MTB2 = 38700
        MTB3 = 82500
        # Tax rates per tax bracket
        TRB1 = 0.10
        TRB2 = 0.12
        TRB3 = 0.22

        if (TaxableIncome >= 0) and (TaxableIncome <= MTB1):
            T1 = (TaxableIncome * TRB1)
            return T1
        elif (TaxableIncome >= MTB1) and (TaxableIncome <= MTB2):
            T2 = (TaxableIncome - MTB1) * TRB2
            return T2 + (MTB1 * TRB1)
        elif (TaxableIncome >= MTB2) and (TaxableIncome <= MTB3):
            T3 = (TaxableIncome - MTB2) * TRB3
            return T3 + (MTB2 * TRB2) + (MTB1 * TRB1)

            # Example calculation with 40,000 income
                # T3 = (40000 - 38700) = 1300 * 0.22
                # T2 = (38700 - 9525) = 29175 * 0.12
                # T1 = (9525 - 0) = 9525 * 0.10
                # TaxesTotal = T1+T2+T3

    def State_Taxes(TaxableIncome):
        S_MTB1 = 3000
        S_MTB2 = 5000
        S_MTB3 = 17000
        S_MTB4 = TaxableIncome - S_MTB3
        # Tax rates per tax bracket
        S_TRB1 = 0.02
        S_TRB2 = 0.03
        S_TRB3 = 0.05
        S_TRB4 = 0.0575

        if (TaxableIncome >= 0) and (TaxableIncome <= S_MTB1):
            S_T1 = (TaxableIncome * S_TRB1)
            return S_T1
        elif (TaxableIncome >= S_MTB1) and (TaxableIncome <= S_MTB2):
            S_T2 = (TaxableIncome - S_MTB1) * S_TRB2
            return S_T2 + (S_MTB2 * S_TRB1)
        elif (TaxableIncome >= S_MTB2) and (TaxableIncome <= S_TRB3):
            S_T3 = (TaxableIncome - S_MTB2) * S_TRB3
            return S_T3 + (S_MTB2 * S_TRB2) + (S_MTB1 * S_TRB1)
        elif (TaxableIncome >= S_MTB3):
            S_T4 = (TaxableIncome - S_MTB3) * S_TRB4
            return S_T4 + (S_MTB3 * S_TRB3) + (S_MTB2 * S_TRB2) + (S_MTB1 * S_TRB1) 

    def SS_Med_Taxes(YearlyIncome):
        # Tax Rates:
        SS_TR = 0.062
        Med_TR = 0.0145
        Total_SS_Med_Taxes = (YearlyIncome * SS_TR) + (YearlyIncome * Med_TR)

        return Total_SS_Med_Taxes

    UserPaidTaxes = Fed_Taxes(TaxableIncome) + SS_Med_Taxes(YearlyIncome) + State_Taxes(TaxableIncome)
    EarningsAT = TaxableIncome - UserPaidTaxes

    print("Your yearly taxes are: ")
    print(UserPaidTaxes)

    print("Your yearly SS/Med taxes are: ")
    print(SS_Med_Taxes(YearlyIncome))

    print("Your yearly State taxes are: ")
    print(State_Taxes(YearlyIncome))

    YearlyExpenses = MonthlyExpenses * 12
    print("Your yearly expenses are: ")
    print(YearlyExpenses)

    YearlySavings = EarningsAT - YearlyExpenses
    print("Your yearly savings after taxes are: ")
    print(YearlySavings)

    print("Your yearly retirement savings are: ")
    print(MonthyContributions * 12)


    # def User_Expense():
    #     UserInput = input("Do you have any expenses? (Y or N): ")
    #     if (UserInput == "Y"):
    #         UserItemExpense = input("Enter expense name: ")

    UserSavingsGoal = str(input("Are you saving for something? (Y/N): "))

    while ((UserSavingsGoal == 'Y') or UserSavingsGoal == 'y'):
        if ((UserSavingsGoal == 'Y') or UserSavingsGoal == 'y'):
            UserSavingsGoalAmount = int(input("What is the amount needed?: "))
            UserGoalAchieved = UserSavingsGoalAmount / (YearlySavings/12)
            print ("You will have enough saved up in " + str(UserGoalAchieved) + " months " + "(" + str(YearlySavings) + " years)")
        else:
            pass
        UserSavingsGoal = str(input("Calculate another savings goal? (Y/N): "))

UserContinue = str(input("Restart program? (Y/N): "))

if (UserContinue != 'Y') or (UserContinue != 'y'):
    Continue == False




# fix bug with looping always on input (error check) and N input for retirement contributions