from typing_extensions import final


print("Welcome to the tip calculator!")
bill = float(input("what was your total bill? $"))
tip = int(input("what Percentage would you like to give tip? 10, 12, or 15?"))
people = int(input("How many people are there to split the bill?"))

bill_with_tip = tip / 100 * bill + bill

bill_per_person = bill_with_tip / people
final_ammount = (round(bill_per_person, 2))
final_ammount = "{:.2f}".format(bill_per_person)
print(f"Each Person should pay ${final_ammount}")
