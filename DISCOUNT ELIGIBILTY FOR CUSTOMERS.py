# plan  basic/standard/premium
# year   1/2/3
# discount 5%/10/20%
plan = input("please enter your plan:").lower()
year = int(input("please enter number of years:"))
if plan == "basic" and year == 1:
    print("you are elogible for 5% discount")
elif plan == "standard" and year == 2:
    print("you are eligible for 10% discount")
elif plan == "premium" and year == 3:
    print("you are eligible for 20% discount")
else:
    print("sorry you are not eligible for any discount")
