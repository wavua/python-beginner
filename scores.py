score = input("Enter Score:   range=0.0 - 1.0")
score2=float(score)
if score2 >1.0:
    print("Score out of range") 
elif score2 >= 0.9:
    print('A')   
elif score2 >= 0.8:
    print('B') 
elif score2 >= 0.7:
    print('C') 
elif score2 >= 0.6:
    print('D') 
else:
    print('F') 