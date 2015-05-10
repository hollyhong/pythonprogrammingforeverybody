text = "X-DSPAM-Confidence:    0.8475";
start = text.find(':') + 1
num = float(text[start:])
print num

