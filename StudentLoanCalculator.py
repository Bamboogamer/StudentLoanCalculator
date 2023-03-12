import copy


def studentLoans(loans, interestRates, amountPaid):
    numOfLoans = len(loans)
    month = 0

    while loans[1] > 0:
        month += 1
        totalInterest = calculateInterest(loans, interestRates)

        # If payment amount will not be complete within 20 years
        if month > (16*12):
            print("LOAN CANNOT BE PAID OFF WITHIN 16 YEARS, RECONSIDER HOW MUCH YOU CAN PAY PER MONTH")
            return -1

        # Pay amount must be higher than interest
        if totalInterest > amountPaid:
            print(f"Amount {amountPaid} Paid Per Month will not cover interest")
            return -1

        payLoan(loans, amountPaid, totalInterest)
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
        # Assumed interest is added
        totalInterest += interest_cost
    return totalInterest


def findHighestInterestRateWithOutstandingPrinciple(loans, interestRates):
    keys = list(interestRates.keys())
    highestRateLoanKey = len(interestRates.keys())
    for key in keys:
        if interestRates[key] >= highestRateLoanKey and loans[key] > 0:
            highestRateLoanKey = key
    return highestRateLoanKey


def payLoan(loans, amountPaid, totalInterest):
    # Assuming Interest is already paid for
    # Paying Principle and Rollover the over-pay to next biggest loan
    principlePay = amountPaid - totalInterest
    for i in range(len(loans), 0, -1):
        loans[i] -= principlePay
        if loans[i] < 0:
            principlePay = abs(loans[i])
            loans[i] = 0
        else:
            principlePay = 0
        if principlePay == 0:
            break


def printLoanInfo(loans, amountPaid, totalInterest, month, totalNumOfLoans):
    print(f"MONTH {month}\n"
          f"Total Amount Paid this Month: ${amountPaid:.2f}\n"
          f"Principle Paid this Month: ${amountPaid - totalInterest:.2f}\n"
          f"Total Interest Paid this Month: ${totalInterest:.2f}"
          )

    print("Current Loans:\n"
          "===============================")

    for loanNumber in range(1, totalNumOfLoans+1):
        if loans[loanNumber] <= 0:
            print(f"Loan {loanNumber} Balance: [PAID OFF]")
        else:
            print(f"Loan {loanNumber} Balance: ${loans[loanNumber]:.2f}")

    print(f"END OF MONTH {month}\n")


def minimumPaymentPerMonthBruteForce(loans, interestRates, goalYears, accuracy=1.0, startingGuess=100):
    goalMonths = goalYears * 12
    # Starting at a bare minimum of 100 dollars
    amount = startingGuess
    while True:
        amount += accuracy
        testMonths = studentLoans(copy.deepcopy(loans), copy.deepcopy(interestRates), amount)

        if goalMonths >= testMonths > 0:
            break

    print(f"MINIUM AMOUNT PAY PER MONTH REQUIRED TO PAY OFF ALL LOANS WITHIN {goalYears} years --> ${amount:.2f}")
    return amount


if __name__ == '__main__':

    testLoans = \
        {
            1: 30000
        }
    testInterestRates = \
        {
            1: 0.05
        }

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

    # print(calculate_minimum_payment(myNormalLoans, myInterestRates, 10))
    from time import time
    times = []
    t0 = time()
    minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, 2, accuracy=1, startingGuess=1400)
    t1 = time()
    minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, 2, accuracy=0.1, startingGuess=1400)
    t2 = time()
    minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, 2, accuracy=0.01, startingGuess=1400)
    t3 = time()
    print('mPPMBF $1.00 Accuracy starting at $1400 takes %f' % (t1 - t0))
    print('mPPMBF $0.10 Accuracy starting at $1400 takes %f' % (t2 - t1))
    print('mPPMBF $0.01 Accuracy starting at $1400 takes %f' % (t3 - t2))

    # minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, 2, accuracy=0.1, startingGuess=0)
    # minimumPaymentPerMonthBruteForce(testLoans, testInterestRates, 10)
    # studentLoans(myNormalLoans, myInterestRates, 300000)

    # studentLoans(testLoans, testInterestRates, 318.20)
