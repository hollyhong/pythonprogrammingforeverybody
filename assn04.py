def computepay(h,r):
    if h <= 40:
        p = h * r
    else:
        ot = h - 40.0
        ot_r = r * 1.5
        p = (40 * r) + (ot * ot_r)
    return p

hours = float(raw_input("Enter hours:"))
rate = float(raw_input("Enter rate:"))
pay = computepay(hours,rate)
print "Pay:", pay