import copy


def studentLoans(loans, interestRates, amountPaid):
    numOfLoans = len(loans)
    month = 0

    while loans[1] > 0:
        month += 1
        totalInterest = calculateInterest(loans, interestRates)

        # If payment amount will not be complete within 20 years
        if month > (20*12):
            # print(f"Loan cannot be paid of within 20 years with a Monthly payment of {amountPaid}, "
            #       "RECONSIDER HOW MUCH YOU CAN PAY PER MONTH OR CONSIDER A DIFFERENT PAYMENT PLAN")
            return -1

        # Pay amount must be higher than interest
        if totalInterest > amountPaid:
            # print(f"Amount ({amountPaid}) paid per month will NOT cover interest")
            return -1

        payLoan(loans, amountPaid, totalInterest)
        # printLoanInfo(loans, amountPaid, totalInterest, month, numOfLoans)

    # print(
    #       f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    #       f"* ALL LOANS HAVE BEEN PAID OFF in ~{month} Months! *\n"
    #       f"********** Approximately {month / 12:.2f} years! **********\n"
    #       f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    # )
    return month


def calculateInterest(loans, interestRates):
    totalInterest = 0
    for key in list(loans.keys()):
        interest_cost = (interestRates[key] / 12) * loans[key]
        # Assumed interest is added, then paid for later on in payLoan()
        totalInterest += interest_cost
    return totalInterest


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
    end_string = f"MONTH {month} ====================================\n" \
                 f"Total Amount Paid this Month: ${amountPaid:.2f}\n" \
                 f"Principle Paid this Month: ${amountPaid - totalInterest:.2f}\n" \
                 f"Total Interest Paid this Month: ${totalInterest:.2f}\n\n" \
                 f"Current Loans:\n"

    for loanNumber in range(1, totalNumOfLoans+1):
        if loans[loanNumber] <= 0:
            end_string += f"Loan {loanNumber} Balance: [PAID OFF]\n"
        else:
            end_string += f"Loan {loanNumber} Balance: ${loans[loanNumber]:.2f}\n"

    print(end_string + f"\nEND OF MONTH {month} =============================\n")
    return -1


def minimumPaymentPerMonthBruteForce(loans, interestRates, goalYears, accuracy=1.0, startingGuess=150):
    goalMonths = goalYears * 12
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
            1: 10000,  # $20000 of STUDENT LOANS FORGIVEN
            3: 10000,
            4: 10000,
            5: 10000 - 10000,
            6: 10000 - 10000
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

    myPaymentPerMonth = 525
    payments = studentLoans(myNormalLoans, myInterestRates, myPaymentPerMonth)
    print(f"Paying ${myPaymentPerMonth} per Month based on given Loans + Interest Rates\n"
          f"    It will take approximately {payments} monthly payments, or ~{payments/12:.2f} years")


    # from time import time
    # guess = 0
    # years = 1.5
    # t0 = time()
    # a = minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, years, accuracy=1.0, startingGuess=guess)
    # t1 = time()
    # b = minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, years, accuracy=0.1, startingGuess=guess)
    # t2 = time()
    # c = minimumPaymentPerMonthBruteForce(myNormalLoans, myInterestRates, years, accuracy=0.01, startingGuess=guess)
    # t3 = time()
    # print(f'mPPMBF $1.00 Accuracy starting at ${guess:.2f} takes {t1 - t0:.2f} seconds, Result -> ${a:.2f}')
    # print(f'mPPMBF $0.10 Accuracy starting at ${guess:.2f} takes {t2 - t1:.2f} seconds, Result -> ${b:.2f}')
    # print(f'mPPMBF $0.01 Accuracy starting at ${guess:.2f} takes {t3 - t2:.2f} seconds, Result -> ${c:.2f}')

