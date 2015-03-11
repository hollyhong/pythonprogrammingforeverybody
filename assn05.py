largest = None
smallest = None

while True:

    i = raw_input('Enter a number:')
    if i == "done" : break

    try:
        num = int(i) 

    except:
        print "Invalid input"
        continue

    if largest is None or smallest is None: ## To assign largest and smallest for first input        
        largest = num
        smallest = num 
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num  

print "Maximum is", largest
print "Minimum is", smallest












