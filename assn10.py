prefix = "From "
delimiter = ":"
counts = dict()

name = raw_input("Enter file name:")
handle = open(name)

for line in handle:
    if not line.startswith(prefix):
        continue
    words = line.split()
    time = words[5]
    #split time sting by the colon and extract hour
    hour = time.split(delimiter)[0]
    counts[hour] = counts.get(hour, 0) + 1

for key, value in sorted(counts.items()):
    print key, value