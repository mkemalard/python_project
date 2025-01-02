january = {}
february = {}
march = {}
april = {}
may = {}
june = {}
july = {}
augustus = {}
september = {}
october = {}
november = {}
december = {}

while True:
    month = input("Enter Month (q to quit): ").lower()
    if month == "q":
        break
    elif month == "january" or month == "jan":
        while True:
            expense = input("Enter your JANUARY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                january.update({expense:amount})
    elif month == "february" or month == "feb":
        while True:
            expense = input("Enter your FEBRUARY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                february.update({expense:amount})
    elif month == "march" or month == "mar":
        while True:
            expense = input("Enter your MARCH expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                march.update({expense:amount})
    elif month == "april" or month == "apr":
        while True:
            expense = input("Enter your APRIL expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                april.update({expense:amount})
    elif month == "may" or month == "may":
        while True:
            expense = input("Enter your MAY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                may.update({expense:amount})
    elif month == "june" or month == "jun":
        while True:
            expense = input("Enter your JUNE expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                june.update({expense:amount})
    elif month == "july" or month == "jul":
        while True:
            expense = input("Enter your JULY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                july.update({expense:amount})
    elif month == "augustus" or month == "aug":
        while True:
            expense = input("Enter your AUGUSTUS expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                augustus.update({expense:amount})
    elif month == "september" or month == "sep":
        while True:
            expense = input("Enter your SEPTEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                september.update({expense:amount})
    elif month == "october" or month == "oct":
        while True:
            expense = input("Enter your OCTOBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                october.update({expense:amount})
    elif month == "november" or month == "nov":
        while True:
            expense = input("Enter your NOVEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                november.update({expense:amount})
    elif month == "december" or month == "dec":
        while True:
            expense = input("Enter your DECEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                december.update({expense:amount})

total = "TOTAL EXPENSES: "
jan_total = sum(january.values())
feb_total = sum(february.values())
mar_total = sum(march.values())
apr_total = sum(april.values())
may_total = sum(may.values())
jun_total = sum(june.values())
jul_total = sum(july.values())
aug_total = sum(augustus.values())
sep_total = sum(september.values())
oct_total = sum(october.values())
nov_total = sum(november.values())
dec_total = sum(december.values())
year_total = jan_total + feb_total + mar_total + apr_total + may_total + jun_total + jul_total + aug_total + sep_total + oct_total + nov_total + dec_total


print()
print("----------------- JAN -----------------")
for expense, amount in zip(january.keys(), january.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${jan_total:.2f}")

print("----------------- FEB -----------------")
for expense, amount in zip(february.keys(), february.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${feb_total:.2f}")

print("----------------- MAR -----------------")  
for expense, amount in zip(march.keys(), march.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${mar_total:.2f}")

print("----------------- APR -----------------")
for expense, amount in zip(april.keys(), april.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${apr_total:.2f}")

print("----------------- MAY -----------------")
for expense, amount in zip(may.keys(), may.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${may_total:.2f}")

print("----------------- JUN -----------------")  
for expense, amount in zip(june.keys(), june.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${jun_total:.2f}")

print("----------------- JUL -----------------")
for expense, amount in zip(july.keys(), july.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${jul_total:.2f}")

print("----------------- AUG -----------------")
for expense, amount in zip(augustus.keys(), augustus.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${aug_total:.2f}")

print("----------------- SEP -----------------")  
for expense, amount in zip(september.keys(), september.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${sep_total:.2f}")

print("----------------- OCT -----------------")
for expense, amount in zip(october.keys(), october.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${oct_total:.2f}")

print("----------------- NOV -----------------")
for expense, amount in zip(november.keys(), november.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${nov_total:.2f}")

print("----------------- DEC -----------------")  
for expense, amount in zip(december.keys(), december.values()):
    print(f"{expense:30} ${amount:.2f}")
print(f"{total:30} ${dec_total:.2f}")

tot_year = ("TOTAL EXPENSES THIS YEAR: ")
print("=======================================")
print(f"{tot_year:30} ${year_total:.2f}")
