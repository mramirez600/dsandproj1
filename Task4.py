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

unique_list = []
no_incoming = []

for a in texts:
    if a[0] not in unique_list:
        unique_list.append(a[0])
    if a[1] not in unique_list:
        unique_list.append(a[1])

for b in calls:
    if b[1] not in unique_list:
        unique_list.append(b[1])
    if b[0] not in unique_list and b[0] not in no_incoming:
        no_incoming.append(b[0])

no_incoming.sort()

print("These numbers could be telemarketers: ")
for k in no_incoming:
    print(k)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
