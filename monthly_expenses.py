jan_exp = []
feb_exp = []
mar_exp = []
apr_exp = []
may_exp = []
jun_exp = []
jul_exp = []
aug_exp = []
sep_exp = []
oct_exp = []
nov_exp = []
dec_exp = []

jan_amou = []
feb_amou = []
mar_amou = []
apr_amou = []
may_amou = []
jun_amou = []
jul_amou = []
aug_amou = []
sep_amou = []
oct_amou = []
nov_amou = []
dec_amou = []

jan_tot = 0
feb_tot = 0
mar_tot = 0
apr_tot = 0
may_tot = 0
jun_tot = 0
jul_tot = 0
aug_tot = 0
sep_tot = 0
oct_tot = 0
nov_tot = 0
dec_tot = 0
year_tot = 0

while True:
    month = input("Enter Month (q to quit): ").lower()
    if month.lower() == "q":
        break
    elif month == "january":
        while True:
            expense = input("Enter your JANUARY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                jan_amou.append(amount)
                jan_exp.append(expense)
                
    elif month == "february":
        while True:
            expense = input("Enter your FEBRUARY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                feb_amou.append(amount)
                feb_exp.append(expense)
    elif month == "march":
        while True:
            expense = input("Enter your MARCH expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                mar_amou.append(amount)
                mar_exp.append(expense)
    elif month == "april":
        while True:
            expense = input("Enter your APRIL expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                apr_amou.append(amount)
                apr_exp.append(expense)
    elif month == "may":
        while True:
            expense = input("Enter your MAY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                may_amou.append(amount)
                may_exp.append(expense)
    elif month == "june":
        while True:
            expense = input("Enter your JUNE expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                jun_amou.append(amount)
                jun_exp.append(expense)
    elif month == "july":
        while True:
            expense = input("Enter your JULY expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                jul_amou.append(amount)
                jul_exp.append(expense)
    elif month == "augustus":
        while True:
            expense = input("Enter your AUGUSTUS expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                aug_amou.append(amount)
                aug_exp.append(expense)
    elif month == "september":
        while True:
            expense = input("Enter your SEPTEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                sep_amou.append(amount)
                sep_exp.append(expense)
    elif month == "october":
        while True:
            expense = input("Enter your OCTOBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                oct_amou.append(amount)
                oct_exp.append(expense)
    elif month == "november":
        while True:
            expense = input("Enter your NOVEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                nov_amou.append(amount)
                nov_exp.append(expense)
    elif month == "desember":
        while True:
            expense = input("Enter your DECEMBER expense (q to quit): ").lower()
            if expense == "q":
                break
            else:
                amount = float(input(f"Enter your expense for {expense}: $"))
                dec_amou.append(amount)
                dec_exp.append(expense)
            
        
for amount in jan_amou:
    jan_tot += amount
for amount in feb_amou:
    feb_tot += amount  
for amount in mar_amou:
    mar_tot += amount        
for amount in apr_amou:
    apr_tot += amount
for amount in may_amou:
    may_tot += amount  
for amount in jun_amou:
    jun_tot += amount  
for amount in jul_amou:
    jul_tot += amount
for amount in aug_amou:
    aug_tot += amount  
for amount in sep_amou:
    sep_tot += amount  
for amount in oct_amou:
    oct_tot += amount
for amount in nov_amou:
    nov_tot += amount  
for amount in dec_amou:
    dec_tot += amount    

print()

print("----------------- JAN -----------------")
for expense, amount in zip(jan_exp, jan_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${jan_tot:.3f}")

print("----------------- FEB -----------------")
for expense, amount in zip(feb_exp, feb_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${feb_tot:.3f}")

print("----------------- MAR -----------------")
for expense, amount in zip(mar_exp, mar_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${mar_tot:.3f}")

print("----------------- APR -----------------")
for expense, amount in zip(apr_exp, apr_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${apr_tot:.3f}")

print("----------------- MAY -----------------")
for expense, amount in zip(may_exp, may_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${may_tot:.3f}")

print("----------------- JUN -----------------")
for expense, amount in zip(jun_exp, jun_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${jun_tot:.3f}")

print("----------------- JUL -----------------")
for expense, amount in zip(jul_exp, jul_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${jul_tot:.3f}")

print("----------------- AUG -----------------")
for expense, amount in zip(aug_exp, aug_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${aug_tot:.3f}")

print("----------------- SEP -----------------")
for expense, amount in zip(sep_exp, sep_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${sep_tot:.3f}")
           
print("----------------- OCT -----------------")
for expense, amount in zip(oct_exp, oct_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${oct_tot:.3f}")

print("----------------- NOV -----------------")
for expense, amount in zip(nov_exp, nov_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${nov_tot:.3f}")

print("----------------- DES -----------------")
for expense, amount in zip(dec_exp, dec_amou):
    print(f"{expense:30} ${amount}")
print(f"TOTAL: ${dec_tot:.3f}")

year_tot = year_tot + jan_tot + feb_tot + mar_tot + apr_tot + may_tot + jun_tot+ jul_tot + aug_tot + sep_tot+ oct_tot + nov_tot + dec_tot
print("=======================================")
print(f"Your Total expenses this year is: ${year_tot}")




