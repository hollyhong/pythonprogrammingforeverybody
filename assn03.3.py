rawstr = raw_input("Enter score:")

try:
	score = float(rawstr)
	if score > 1 or score < 0:
		print 'Score must be between 0 and 1'
	else:
		if score >= 0.9:
			print 'A'
		elif score >= 0.8:
			print 'B'
		elif score >= 0.7:
			print 'C'
		elif score >= 0.6:
			print 'D'
		else:
			print 'F'	
except:
	print 'Score must be between 0 and 1'