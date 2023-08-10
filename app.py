import calendar

# Create a TextCalendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)  # Start the week on Sunday

# Print the full calendar for the year 2023
year = 2023
for month in range(1, 13):
    print(cal.formatmonth(year, month))
    print("=" * 20)  # Separate each month
