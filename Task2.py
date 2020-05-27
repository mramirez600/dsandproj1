"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import collections
# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

tele_num = {}
counter = 0

for nums in calls:
    if not tele_num.get(nums[0]):
        tele_num[nums[0]] = int(nums[3])
    else:
        tele_num[nums[0]] += int(nums[3])
    if not tele_num.get(nums[1]):
        tele_num[nums[1]] = int(nums[3])
    else:
        tele_num[nums[1]] += int(nums[3])
        counter += 1


items = tele_num.items()
sorted_items = sorted(
    items, key=lambda key_value: key_value[1], reverse=True)
sorted_by_seconds = collections.OrderedDict(sorted_items)

# print(sorted_by_c)
tuple_list = list(sorted_by_seconds.items())
key_value = tuple_list[0]

print(key_value[0] + " spent the longest time, " + str(key_value[1]) +
      " seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
