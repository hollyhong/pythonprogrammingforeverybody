# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fhandle = open(fname)
count = 0
total = 0
prefix = "X-DSPAM-Confidence:"
start = len(prefix) + 1

for line in fhandle:
    # Eliminate lines that do not start with
    if not line.startswith(prefix):
        continue
    # Perform this on the lines not eliminated
    count = count + 1
    num = float(line[start:])   
    total = total + num

avg = total / count
print "Average spam confidence:", avg