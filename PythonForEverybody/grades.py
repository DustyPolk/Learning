#!/usr/bin/python3

string1 = input("Enter Score Between 0.0 and 1.0: ")
score = float(string1)
	
if score > 1.0:
	print("Enter a number between 0.0 and 1.0")
	quit()
elif score >= 0.9:
	print ("You got an A!")
elif score >= 0.8:
	print ("You got a B!")
elif score >= 0.7:
	print ("You got a C!")
elif score >= 0.6:
	print ("You got a D!")
elif score < 0.6:
	print ("You failed")

