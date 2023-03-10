
loans = \
    {
    }

interestRates = \
    {
    }


def studentLoans(loans, interestRates, principleCost, years):

    for i in range(years*12):
        interest_cost1 = interestRates[1]*loans[1]
        interest_cost2 = interestRates[2]*loans[2]
        loans[1] += interest_cost1
        loans[2] += interest_cost2

        interest_cost3 = interestRates[3]*loans[3]
        interest_cost4 = interestRates[4]*loans[4]
        loans[3] += interest_cost3
        loans[4] += interest_cost4

        interest_cost5 = interestRates[5]*loans[5]
        interest_cost6 = interestRates[6]*loans[6]
        loans[5] += interest_cost5
        loans[6] += interest_cost6

        # Assuming you're paying of the interest for EVERY Loan FIRST
        loans[1] -= interest_cost1
        loans[2] -= interest_cost2
        loans[3] -= interest_cost3
        loans[4] -= interest_cost4
        loans[5] -= interest_cost5
        loans[6] -= interest_cost6

        # Paying off the Principle

        # Find the highest Interest Rate
        # USE HIGHEST_Interest, find the highest loan WITH the highest interest rate
        # remove WHOLE principle towards that loan until it is less than or equal to zero

        # If it's less than 0, convert the negative balance and add it to the NEXT payment of the next largest loan
        # Then REMOVE that loan from the dictionary

        # Hardcoded
        loans[6] -= principleCost

        # Can be helper function
        totalInterest = interest_cost1 + interest_cost2 + \
                        interest_cost3 + interest_cost4 + \
                        interest_cost5 + interest_cost6

        print(f"MONTH {i+1}\n"
              f"Total Interest {totalInterest}\n")
        print(f"Loan Balances:\n"
              f"Loan 1: {loans[1]:.2f}\n"
              f"Loan 2: {loans[2]:.2f}\n"
              f"Loan 3: {loans[3]:.2f}\n"
              f"Loan 4: {loans[4]:.2f}\n"
              f"Loan 5: {loans[5]:.2f}\n"
              f"Loan 6: {loans[6]:.2f}\n"
              )

studentLoans(loans, interestRates, 500, 2)
