def studentLoans(loans, interestRates, amountPaid):
    numOfLoans = len(loans)
    month = 0

    while loans[1] > 0:
        month += 1
        totalInterest = calculateInterest(loans, interestRates)
        highestLoan = findFirstHighestRate(loans, interestRates)

        payLoan(loans, interestRates, highestLoan, amountPaid, totalInterest)
        printLoanInfo(loans, amountPaid, totalInterest, month, numOfLoans)

    print(
          f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
          f"* ALL LOANS HAVE BEEN PAID OFF in ~{month} Months! *\n"
          f"********** Approximately {month / 12:.2f} years! **********\n"
          f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    )


def calculateInterest(loans, interestRates):
    totalInterest = 0
    for key in list(loans.keys()):
        interest_cost = (interestRates[key] / 12) * loans[key]
        loans[key] += interest_cost
        totalInterest += interest_cost
    return totalInterest


def findFirstHighestRate(loans, interestRates):
    keys = list(interestRates.keys())
    highestRateLoanKey = len(interestRates.keys())
    for key in keys:
        if interestRates[key] >= highestRateLoanKey and loans[key] > 0:
            highestRateLoanKey = key
    return highestRateLoanKey


def payLoan(loans, interestRates, highestLoan, amountPaid, totalInterest):
    loans[highestLoan] -= amountPaid - totalInterest

    if highestLoan != 1 and loans[highestLoan] <= 0:
        loans[highestLoan - 1] += loans[highestLoan]
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

    print(f"END OF MONTH {month + 1}\n")


if __name__ == '__main__':
    myLoans = \
        {
            1: 10000,
            2: 10000,
            3: 10000,
            4: 10000,
            5: 10000,
            6: 10000
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

    studentLoans(myLoans, myInterestRates, 750)
