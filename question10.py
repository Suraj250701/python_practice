# Print no. of days in given list of Months e.g ['April','February','May'] output April - 30 Days February - 28 or 29 days,May 31 Days

month_days = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


for month in month_days:
    if month == 'February': 
        print(f"{month} - 28 or 29 days")
    elif month in ['April', 'June', 'September', 'November']:
        print(f"{month} - 30 days")
    else:
        print(f"{month} - 31 days")