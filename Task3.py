"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    counter = 0
    unique_list = []
    openBracket = 0
    mobile = ["7", "8", "9"]
    mobileLines = 0
    telemarketers = ["140"]
    telemLines = 0
    uniqueCodes = []

    for a in calls:
        if a[0][:4] == "(080" and a[1] not in unique_list:
            unique_list.append(a[1])

    co = []
    for c in calls:
        if c[0][:4] == "(080" and c[1][:4] == "(080":
            counter += 1
        if c[0][:4] == "(080":
            co.append(c[0])

    for b in unique_list:
        if b[:1] == "(" and b[:b.index(")")+1] not in uniqueCodes:
            uniqueCodes.append(b[:b.index(")")+1])
        if b[:1] in mobile and b[:4] not in uniqueCodes:
            uniqueCodes.append(b[:4])
        if b[:3] in telemarketers and b[:3] not in uniqueCodes:
            uniqueCodes.append(b[:3])

uniqueCodes.sort()
print("The numbers called by people in Bangalore have codes:")
for d in uniqueCodes:
    print(d)

callPercentage = float(counter)/len(co)

print("\n" + str(round(callPercentage, 2)) +
      " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
