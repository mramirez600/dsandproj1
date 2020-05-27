"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_row = texts[0]
    counter = 0
    unique_list = []
    for a in texts:
        if a[0] not in unique_list:
            unique_list.append(a[0])
            counter += 1
        if a[1] not in unique_list:
            unique_list.append(a[1])
            counter += 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    counter2 = 0
    for a in calls:
        if a[0] not in unique_list:
            unique_list.append(a[0])
            counter2 += 1
        if a[1] not in unique_list:
            unique_list.append(a[1])
            counter2 += 1
    uniqueCount = counter + counter2
    print("There are " + str(uniqueCount) +
          " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
