import datetime

# Printing current date

today = datetime.datetime.now()     # Assigning variable today as current datetime

week_day = today.strftime('%A')
month = today.strftime('%B')
date = today.strftime('%d')
year = today.strftime('%Y')

print(f'Today is {week_day}, {month} {date}, {year}')

# Printing my bday

bday = datetime.date(1999, 4, 20)                   
print(f'My birthday is {bday.strftime('%m/%d/%Y')}') # Formatting it to have mm/dd/yyyy

# Printing what date would 90 days from today

ninety_d = today + datetime.timedelta(days=90)      # adding 90 days from today
print(f'90 days from today is {ninety_d.strftime('%B %d, %Y')}')

# Printing a dinner time 

dinner_time = datetime.time(18, 30)         # specified time in military 
print(f'Let\'s meet for dinner at {dinner_time.strftime('%I:%M %p')}') # formatted with am or pm
