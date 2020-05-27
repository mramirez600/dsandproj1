"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_row = texts[0]
    textTime = first_row[2]
    print("First record of texts, " +
          first_row[0] + " texts " + first_row[1] + " at time " + textTime[-8:])
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    callTime = calls[len(calls)-1][2]
    print("Last record of calls, " +
          calls[len(calls)-1][0] + " calls " + calls[len(calls)-1][1] + " at time " + callTime[-8:] + ", lasting " + calls[len(calls)-1][3] + " seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
