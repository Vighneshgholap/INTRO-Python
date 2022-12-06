#Exercise
# write a weight converter
# convert kg to pound and vice versa

weight = input("Enter Weight: ")
value = input("KG(k) or LBS(l): ")

if value == "k" or value == "K":
    
    weight = float(weight) * 2.204
    print("Weight in lbs: " + str(weight))

elif value == "l" or value == "L":
    
    weight = float(weight) * 0.453
    print("Weight in lbs: " + str(weight))

else:
    print("Value Invalid!")