import random

otp = random.randint(1000,9999)
print("YOUR OTP IS-",otp)

user = int(input("Enter the OTP: "))
if (otp == user):
    print("Access granted")
else:
    print("Access denied your otp is wrong ")