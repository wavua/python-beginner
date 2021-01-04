hrs=input("Enter hours:")
rt=input("Enter rate:")
try:
    hours=float(hrs)
    rate=float(rt)
except:
    print("Error,please enter a numeric input")
    quit()

print(hours,rate)
if hours > 40:
    pay=hours*rate
    bonus=(hours-40)*(rate*0.5)
    grossPay=pay+bonus
else:
    grossPay=hours*rate
print("Pay:",grossPay)
