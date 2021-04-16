income = float(input("enter your income per year in $:"))
if income > 30000:
    work_period = int(input("How long have you been working in years:"))
    if work_period >= 2:
        print("You qualify for a loan")
    else:
        print("You do not qualify for a loan")
    print('Still inside the first if for 30000')
else:
    print("You do not qualify for a loan")