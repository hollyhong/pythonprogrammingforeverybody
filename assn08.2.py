fn = raw_input('Enter file name:')
#fh = open(fn)
fh = open('mbox-short.txt')
prefix = "From:"
count = 0

for line in fh:
    # Eliminate lines that do not start with
    if not line.startswith(prefix):
        continue
    # Perform this on the lines not eliminated
    email = line.split()
    count = count + 1
    print email[1]

print "There were", count, "lines in the file with From as the first word"



