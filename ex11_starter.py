#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
count = len(Belgium)
head1 = "Task1"
print(head1.center(130, "*"))
print("The Belgium String is", count, "Characters Long")
print("-"*count)
print("Hope you enjoyed the", count, "dashes")
print()
print()
head2 = "Task2"
print(head2.center(130, "-"))
print(Belgium)
print("Swap commas with colons")
print(Belgium.replace(',', ':'))
print()
print()
head3 = "Task 3"
print(head3.center(130, "-"))
# Grabbing the direct data from the string into integer, plus them together
BelPop = int(Belgium[8:16])
print("Belgium Population is: ", BelPop)
BrusPop = int(Belgium[26:32])
print("Brussels population is", BrusPop)
print("Direct grab string method, adding together", BrusPop+BelPop, sep=' --- ')
print()

# convert string to list using split, taking the required data into integer variables and print plussed together
list = (Belgium.split(","))
find1 = int(list[1])
print("Belgium Population is: ", find1)
find2 = int(list[3])
print("Brussels Population is: ", find2)
print("Splitting in to list method, adding together", find1+find2, sep=': ')
print()
head1 = "Other Stuff"
print(head1.center(130, "-"))
print(list)

for count, i in enumerate(list):
    print(f"{count:20d} {i:>50s} ")



