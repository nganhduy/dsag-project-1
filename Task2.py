"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def mapDuration(dictionary, phoneNumber, timeSpend):
	if dictionary.get(phoneNumber)==None:
		dictionary[phoneNumber]= int(timeSpend)
	else:
		dictionary[phoneNumber] = dictionary.get(phoneNumber)+ int(timeSpend)
	return dictionary

def getDate(call, month, year):
	timeStamp= call[2]
	date = datetime.strptime(timeStamp, '%d-%m-%Y %H:%M:%S')
	callYear = date.year
	callMonth = date.month

	if callYear == year and callMonth == month:
		return True
	else:
		return False

records = filter(lambda x: getDate(x,9,2016),calls)
dictionary={}

for record in records:
	outgoingNumber = record[0]
	incomingNumber = record[1]
	timeSpend = record[3]
	dictionary = mapDuration(dictionary, outgoingNumber, timeSpend)
	dictionary = mapDuration(dictionary, incomingNumber, timeSpend)

phoneNumber = max(dictionary.items(), key=lambda str: int(str[1]))

print(f"{phoneNumber[0]} spent the longest time, {phoneNumber[1]} seconds, on the phone during September 2016.")
