import calendar

print("--- Python Calendar Tool ---")

yy = int(input("Year (যেমন: 2025): "))
mm = int(input("Month (1-12): "))

print("\n", calendar.month(yy, mm))

print("---------------------------")