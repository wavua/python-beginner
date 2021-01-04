hrs=input("Enter hours:")
rt=input("Enter rate:")
hours=float(hrs)
rate=float(rt)
if hours > 40:
    pay=hours*rate
    bonus=(hours-40)*(rate*0.5)
    grossPay=pay+bonus
else:
    grossPay=hours*rate
print("Pay:",grossPay)
