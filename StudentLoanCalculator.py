import copy


def studentLoans(loans, interestRates, amountPaid):
    numOfLoans = len(loans)
    month = 0

    while loans[1] > 0:
        month += 1

        # If payment amount will not be complete within 20 years
        if month > (16*12):
            print("LOAN CANNOT BE PAID OFF WITHIN 16 YEARS, RECONSIDER HOW MUCH YOU CAN PAY PER MONTH")
            return -1

        totalInterest = calculateInterest(loans, interestRates)
        highestLoan = findHighestInterestRateWithOutstandingPrinciple(loans, interestRates)

        if (totalInterest > amountPaid):
            print(f"Amount {amountPaid} Paid Per Month will not cover interest")
            return -1
        payLoan(loans, interestRates, highestLoan, amountPaid, totalInterest)
        printLoanInfo(loans, amountPaid, totalInterest, month, numOfLoans)

    print(
          f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
          f"* ALL LOANS HAVE BEEN PAID OFF in ~{month} Months! *\n"
          f"********** Approximately {month / 12:.2f} years! **********\n"
          f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    )
    return month


def calculateInterest(loans, interestRates):
    totalInterest = 0
    for key in list(loans.keys()):
        interest_cost = (interestRates[key] / 12) * loans[key]
        loans[key] += interest_cost
        totalInterest += interest_cost
    return totalInterest


def findHighestInterestRateWithOutstandingPrinciple(loans, interestRates):
    keys = list(interestRates.keys())
    highestRateLoanKey = len(interestRates.keys())
    for key in keys:
        if interestRates[key] >= highestRateLoanKey and loans[key] > 0:
            highestRateLoanKey = key
    return highestRateLoanKey


def payLoan(loans, interestRates, highestLoan, amountPaid, totalInterest):

    # # Paying Interest of all the leftover loans
    # for key in list(loans.keys()):
    #     loans[key] -= ((interestRates[key] / 12) * loans[key])

    # Paying Principle
    loans[highestLoan] -= (amountPaid - totalInterest)

    # If the "HighestLoan" amount goes negative, rollover the payment to the next largest loan
    if highestLoan != 1 and loans[highestLoan] <= 0:
        nextHighest = findHighestInterestRateWithOutstandingPrinciple(loans, interestRates)
        loans[nextHighest] += loans[highestLoan]
        print(
              f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
              f"LOAN {highestLoan} PAID OFF! :D\n"
              f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        del loans[highestLoan]
        del interestRates[highestLoan]


def printLoanInfo(loans, amountPaid, totalInterest, month, totalNumOfLoans):

    print(f"MONTH {month}\n"
          f"Total Amount Paid this Month: ${amountPaid:.2f}\n"
          f"Principle Paid this Month: ${amountPaid - totalInterest:.2f}\n"
          f"Total Interest Paid this Month: ${totalInterest:.2f}"
          )

    print("Current Loans:\n"
          "===============================")

    for loanNumber in range(1, totalNumOfLoans+1):

        try:
            if loans[1] <= 0:
                print(f"Loan {loanNumber} Balance: [PAID OFF]")
            else:
                print(f"Loan {loanNumber} Balance: ${loans[loanNumber]:.2f}")
        except KeyError:
            print(f"Loan {loanNumber} Balance: [PAID OFF]")

    print(f"END OF MONTH {month}\n")


def minimumPaymentPerMonth(loans, interestRates, goalYears):
    goalMonths = goalYears * 12

    # Starting at a bare minimum of 100 dollars
    amount = 100
    while True:
        amount += 1
        testMonths = studentLoans(copy.deepcopy(loans), copy.deepcopy(interestRates), amount)

        if goalMonths >= testMonths > 0:
            break

    print(f"TESTING DANNY: MINIUM AMOUNT REQUIRED --> {amount}")
    return amount




if __name__ == '__main__':
    myNormalLoans = \
        {
            1: 10000,
            2: 10000,
            3: 10000,
            4: 10000,
            5: 10000,
            6: 10000
        }

    myForgivenLoans = \
        {
        }

    myInterestRates = \
        {
            1: 0.0275,
            2: 0.0275,
            3: 0.0373,
            4: 0.0373,
            5: 0.0499,
            6: 0.0499
        }

    # studentLoans(myNormalLoans, myInterestRates, 750)
    #
    # # studentLoans(myForgivenLoans, myInterestRates, 750)
    minimumPaymentPerMonth(myNormalLoans, myInterestRates, 2)
