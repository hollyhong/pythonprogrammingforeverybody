hours = float(raw_input("Enter hours:"))
rate = float(raw_input("Enter rate:"))

if hours <= 40:
	pay = hours * rate
else:
	ot = hours - 40.0
	ot_rate = rate * 1.5
	pay = (40 * rate) + (ot * ot_rate)	
print pay
