a="The quick Brow Fox"
lower=0
upper=0
for i in a:
 if (i.islower()):
  lower+= 1
 else:
  upper+= 1
 print("the number of lower case letters is:",lower)
 print("the number of upper case letters is:",upper)