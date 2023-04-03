# Author: Michael Sheridan
# QAP 5: The Final Frontier
# Program that takes the policies.dat file, only keeps monthly payment policies, and formats it into a detailed policy report

import datetime

# Initializing policy date to current date
currDate = datetime.datetime.today()
policyDate = currDate.strftime("%d" "-" "%b" "-" "%y")

# Opening policies.dat
f = open("policies.dat", "r")

# Report header
print()
print("ONE STOP INSURANCE COMPANY")
print(f'MONTHLY PAYMENT LISTING AS OF {policyDate}')
print()
print(f'POLICY CUSTOMER {" " * 11} TOTAL {" " * 15} TOTAL {" " * 5} MONTHLY')
print(f'NUMBER NAME {" " * 14} PREMIUM {" " * 4} HST {" " * 5} COST {" " * 6} PAYMENT')
print("=" * 70)

# Initializing Arrays
totalPolicyArray = []
HSTArray = []
totalCostArray = []
totalPremArray = []
monthlyPayArray = []

# Loop that assigns elements in policies.dat to variables as it goes through the file, appends certain 
# variable to above lists, does extra cost and total premium calculations, and formats it to be printed
for PolicyInfo in f:
   
    PolicyCustomer = PolicyInfo.split(", ")
    if PolicyCustomer[12] == "M":
    
        policyNum = PolicyCustomer[0]
        totalPolicyArray.append(policyNum)
        
        firstName = PolicyCustomer[1]
        lastName = PolicyCustomer[2]
        StAdd = PolicyCustomer[3]
        City = PolicyCustomer[4]
        Prov = PolicyCustomer[5]
        PostalCode = PolicyCustomer[6]
        PhoneNum = PolicyCustomer[7]
        NumOfCar = int(PolicyCustomer[8])
        
        xtra_liab = PolicyCustomer[9]
        if xtra_liab == "Y":
            liabCost = 130.00 * NumOfCar
        elif xtra_liab == "N":
            liabCost = 0
        
        glass_cover = PolicyCustomer[10]
        if glass_cover == "Y":
            glassCost = 86.00 * NumOfCar
        elif glass_cover == "N":
            glassCost = 0
        
        loaner = PolicyCustomer[11]
        if loaner == "Y":
            loanCost = 58.00 * NumOfCar
        elif loaner == "N":
            loanCost = 0
        
        payOption = PolicyCustomer[12]
        
        loanAmt = int(PolicyCustomer[13])
        InsurePrem = float(PolicyCustomer[14])

        fullName = (firstName + " " + lastName) + " " * (20 - len(firstName + " " + lastName))

        # Above mentioned calculations
        extraCost = liabCost + glassCost + loanCost
        totalPrem = extraCost + InsurePrem
        HST = round(totalPrem * .15, 2) 
        totalCost = totalPrem + float(HST)
        monthlyPay = (totalCost + 39.99) / 12
        
        totalPremArray.append(totalPrem)
        HSTArray.append(HST)
        totalCostArray.append(totalCost)
        monthlyPayArray.append(monthlyPay)
    
    # Print statements for formatted file information
        print(f' {policyNum}  {fullName}{"${:,.2f}" .format(totalPrem)} {"${:,.2f}" .format(HST):>9} {"${:,.2f}" .format(totalCost):>11} {"${:,.2f}" .format(monthlyPay):>10}')


totalHST = HSTArray[0]
totalCost = totalCostArray[0]
totalPrem = totalPremArray[0]
totalMonthly = monthlyPayArray[0]

# Calculations for footer values
i=2
while i <= len(HSTArray):
    totalHST += HSTArray[i-1] 
    i += 1

i=2
while i <= len(totalCostArray):
    totalCost += totalCostArray[i-1]
    i += 1

i=2
while i <= len(totalPremArray):
    totalPrem += totalPremArray[i-1]
    i += 1

i=2
while i <= len(monthlyPayArray):
    totalMonthly += monthlyPayArray[i-1]
    i += 1

totalPolicy = len(totalPolicyArray)

# Formatted footer print statement
print("=" * 70)
print(f'Total policies: {totalPolicy:>3} {"${:,.2f}" .format(totalPrem):>16} {"${:,.2f}" .format(totalHST):>9} {"${:,.2f}" .format(totalCost):>11} {"${:,.2f}" .format(totalMonthly):>10}')
print()

# Closing policies.dat
f.close()
quit()

