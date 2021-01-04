def computepay(h,r):
    if h > 40:
        pay=h*r
        bonus=(h-40)*(r*0.5)
        grossPay=pay+bonus
    else:
        grossPay=h*r

    return grossPay


hrs = input("Enter Hours:")
rate=input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
