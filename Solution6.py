distance = 5

if distance<3:
    transport="Walk"
elif distance<=15:
    transport= "bike"
else:
    transport="Car"

print("The transport is", transport)