prefix = "From:"
counts = dict()
bigcount = None
bigemail = None

name = raw_input("Enter file name:")
handle = open(name)

for line in handle:
    if not line.startswith(prefix):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email

print bigemail, bigcount