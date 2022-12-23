#!/usr/bin/python3

string1 = input("How many hours did you work this week? ")
string2 = input("How much do you make per hours? ")
try:
	hours = float(string1)
	rate = float(string2)
except: 
	print("Enter numeric value")
	quit()

if hours > 40:
	reg = hours * rate
	otp = (hours - 40.0) * (rate * 0.5)
	xp = reg + otp
else:
	xp = hours * rate

print("Pay: ", xp)
