# Author: Michael Sheridan
# QAP 5: The Final Frontier
# Program that takes the policies.dat file and formats it into a detailed policy report

import datetime

# Initializing policy date to current date
currDate = datetime.datetime.today()
policyDate = currDate.strftime("%d" "-" "%b" "-" "%y")

# Opening policies.dat
f = open("policies.dat", "r")

# Report header
print()
print("ONE STOP INSURANCE COMPANY")
print(f'POLICY LISTING AS OF {policyDate}')
print()
print(f'POLICY CUSTOMER {" " * 12} INSURANCE {" " * 2} EXTRA {" " * 4} TOTAL')
print(f'NUMBER NAME {" " * 17} PREMIUM {" " * 3} COSTS {" " * 3} PREMIUM')
print("=" * 60)

# Initializing Arrays
totalPolicyArray = []
totalInsureArray = []
totalExtraCostArray = []
totalPremArray = []

# Loop that assigns elements in policies.dat to variables as it goes through the file, appends certain 
# variable to above lists, does extra cost and total premium calculations, and formats it to be printed
for PolicyInfo in f:

    PolicyCustomer = PolicyInfo.split(", ")
    
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
    totalInsureArray.append(InsurePrem)

    fullName = (firstName + " " + lastName) + " " * (20 - len(firstName + " " + lastName))

    # Above mentioned calculations
    extraCost = liabCost + glassCost + loanCost
    totalExtraCostArray.append(extraCost)
    totalPrem = extraCost + InsurePrem
    totalPremArray.append(totalPrem)
   
   # Print statements for formatted file information
    print(f' {policyNum}  {fullName} {"${:,.2f}" .format(InsurePrem):>10} {"${:,.2f}" .format(extraCost):>10} {"${:,.2f}" .format(totalPrem):>10}')

totalInsure = totalInsureArray[0]
totalExtraCost = totalExtraCostArray[0]
totalPrem = totalPremArray[0]

# Calculations for footer values
i=2
while i <= len(totalInsureArray):
    totalInsure += totalInsureArray[i-1]
    i += 1

i=2
while i <= len(totalExtraCostArray):
    totalExtraCost += totalExtraCostArray[i-1]
    i += 1

i=2
while i <= len(totalPremArray):
    totalPrem += totalPremArray[i-1]
    i += 1

totalPolicy = len(totalPolicyArray)

# Formatted footer print statement
print("=" * 60)
print(f'Total policies: {totalPolicy:>3} {"${:,.2f}" .format(totalInsure):>18} {"${:,.2f}" .format(totalExtraCost):>10} {"${:,.2f}" .format(totalPrem):>10}')
print()

# Closing policies.dat
f.close()
quit()
