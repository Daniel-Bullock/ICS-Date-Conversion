#Author: Daniel Bullock
#6/16/2020
#Ics File Shifter

from icalendar import Calendar, Event
from icalendar import vDatetime, vDate
from datetime import datetime, timedelta, date
from pytz import UTC # timezone


#opens the calendar file
file_to_open = input("File Name (include .ics): ")
print(file_to_open)
calfile = open(file_to_open,'rb')
cal = Calendar.from_ical(calfile.read())

#user inputs for input date
print("Where would you like the new calendar to start?\n")
year = input("Year: ")
month = input("Month (as number): ")
day = input("Day: ")
input_date = datetime(int(year), int(month), int(day)).date()


#Input: calendar, user inputted date
#Output: days between the inputted date and the first event in the calendar
def change_in_days(cal,input_date):
    min = datetime(9999, 12, 31).date()

    for event in cal.walk('vevent'):       #finds the first event date
        sdates = event.get('dtstart').dt
        if hasattr(sdates, 'date'):
            sdate = sdates.date()
        else:
            sdate = sdates
        if sdate < min:
            min = sdate
    return (input_date - min).days


change = change_in_days(cal,input_date)     #calls change in days function to find the days between
shifts_to_do = {}    #initializes dictionary for the old and shifted dates


#Input: calendar, change in days between inputted date and first event date
#Output: none
#Action: shifts all of the dates accordingly
def shift_dates(cal,change):
    for event in cal.walk('vevent'):

        start_date = event.get('dtstart').dt
        start_new_date = start_date+timedelta(days=change)
        if hasattr(start_new_date, 'tzinfo'):
            start_shifted_date = vDatetime(start_new_date).to_ical()
        else:
            start_shifted_date = vDate(start_new_date).to_ical()
        original_date = event.get('dtstart').to_ical()
        shifts_to_do[original_date] = start_shifted_date

        end_date = event.get('dtend').dt
        end_new_date = end_date + timedelta(days=change)
        if hasattr(end_new_date, 'tzinfo'):
            end_shifted_date = vDatetime(end_new_date).to_ical()
        else:
            end_shifted_date = vDate(end_new_date).to_ical()
        end_original_date = event.get('dtend').to_ical()
        shifts_to_do[end_original_date] = end_shifted_date


shift_dates(cal,change)  #calling shift dates function


#Input: text to search over, what to search for
#Output: returns new text with edits
def replace_words(base_text, device_values):
    for key, val in device_values.items():
        base_text = base_text.replace(key.decode('utf-8'), val.decode('utf-8'))
    return base_text

#opens file to read then closes
t = open(file_to_open, 'rt')
tempstr = t.read()
t.close()

#generates outputted ics file text
output = replace_words(tempstr, shifts_to_do)

#opens up the output file and write final calendar onto it
fout = open('icsShifterOutput.ics', 'wt')
fout.write(output)
fout.close()

