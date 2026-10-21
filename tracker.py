print("Welcome to the daily health and expense management program!")
name= input("please enter your name:\n ")
hour=float(input ("your available hours for today:\n"))
budget= float(input("your daily budget:\n"))
study= float(input("how many hours are you going to study python?\n"))
practice=float(input("how many hours for your practice?\n"))
activities=float(input("hours for your other activities:\n"))
total_planned_hours= study+practice+activities
print("your total activities planned for the day=", total_planned_hours)
print("please enter your daily expenses accordingly!")
food=float(input("food: "))
transportation=float(input("transportation: "))
others=float(input("others: "))
total_daily_expenses=food+transportation+others
print("your total daily expenses are=", total_daily_expenses)
if hour>= total_planned_hours:
   print("Your daily plans are realistic.\n")
else :print("You have made more plans than your available time.\n")
if budget>=total_daily_expenses:
   print("You are within your daily budget\n")
else :print("You have exceeded your daily budget\n")
print("Here is your final report of the day:\n")
print("your name: ", name)
print("your total planned hours for today:", total_planned_hours)
available_hours= hour-total_planned_hours
if available_hours<0:
   available_hours=0
print("your available hours for today:", available_hours)
print("your daily total expenses:", total_daily_expenses)
remaining_budget= budget-total_daily_expenses
if remaining_budget<0:
   remaining_budget=0
print("your remaining budget for today:", remaining_budget)