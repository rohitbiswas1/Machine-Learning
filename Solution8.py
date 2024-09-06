password="Secure8974y@26"

if len(password)<6:
    strngth="Weak"

elif len(password)<=10:
    strngth="Meium"
else:
    strngth="Strong"

print("Pssword strength is : " , strngth)