def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    month = month.capitalize()
    month_days = (
        ('January', 31), ('February', 28), ('March', 31), ('April', 30),
        ('May', 31), ('June', 30), ('July', 31), ('August', 31),
        ('September', 30), ('October', 31), ('November', 30), ('December', 31)
    )

    month_days_dict = dict(month_days)

    if month not in month_days_dict:
        return "Invalid month. Please enter valid month."

    if month == 'February' and leap(year):
        return 29

    return month_days_dict[month]

month = input("Enter the name of the month: ")
year = int(input("Enter the year: "))

days = days_in_month(month, year)
print(f"Number of days in {month} of year {year}: {days}")
