fn = raw_input('Enter file name:')
fh = open(fn)
romeo = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in romeo:
            romeo.append(word)

romeo.sort()
print romeo



