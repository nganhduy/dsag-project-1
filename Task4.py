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
outgoingCalls = []
receiveCalls = []
telemarketers = []

for record in calls:
    outgoingNumber = record[0]
    receiveNumber = record[1]
    
    if outgoingNumber not in outgoingCalls:
        outgoingCalls.append(outgoingNumber)

    if receiveNumber not in receiveCalls:
        receiveCalls.append(receiveNumber)

outgoingTexts = []
receiveTexts = []

for record in texts:
    outgoingNumber = record[0]
    receiveNumber = record[1]

    if outgoingNumber not in outgoingTexts:
        outgoingTexts.append(outgoingNumber)

    if receiveNumber not in receiveTexts:
        receiveTexts.append(receiveNumber)

for phoneNum in outgoingCalls:
    if((phoneNum not in receiveCalls) and (phoneNum not in outgoingTexts) and (phoneNum not in receiveTexts)):
        telemarketers.append(phoneNum)

print("These numbers could be telemarketers: ")
print(*sorted(telemarketers), sep='\n')