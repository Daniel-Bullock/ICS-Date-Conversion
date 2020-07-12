# Author: Daniel Bullock
# 6/16/2020
# Ics File Shifter



from icalendar import Calendar, Event
from icalendar import vDatetime, vDate
from datetime import datetime, timedelta, date
from pytz import UTC  # timezone



def process_data(input_data,input_date):


    cal = Calendar.from_ical(input_data.decode('utf-8'))

    change = change_in_days(cal, input_date)


    output_data = shift_dates(cal,change)

    return output_data





# Input: calendar, user inputted date
# Output: days between the inputted date and the first event in the calendar
def change_in_days(cal, input_date):
    min = datetime(9999, 12, 31).date()         #earliest date to compare to find the first date in input calendar

    for event in cal.walk('vevent'):  #loops through calendar events
        sdates = event.get('dtstart').dt
        if hasattr(sdates, 'date'):     #this if statement converts to correct date format
            sdate = sdates.date()
        else:
            sdate = sdates
        if sdate < min:
            min = sdate
    return (input_date - min).days


#Input: Calendar file to be shifted and the change in days from the new and old starting dates
#Output: Text of calendar file
def shift_dates(cal, change):

    for event in cal.walk('vevent'):    #loops through calendar events

        start_date = event.get('dtstart').dt
        start_new_date = start_date + timedelta(days=change)    #gets initial date and applies shift

        if hasattr(start_new_date, 'tzinfo'):               #converts to correct format for calendar file
            start_shifted_date = vDatetime(start_new_date)
        else:
            start_shifted_date = vDate(start_new_date)

        event['dtstart'] = start_shifted_date           #applies new date to event


        end_date = event.get('dtend').dt
        end_new_date = end_date + timedelta(days=change)
        if hasattr(end_new_date, 'tzinfo'):
            end_shifted_date = vDatetime(end_new_date)
        else:
            end_shifted_date = vDate(end_new_date)

        event['dtend'] = end_shifted_date


    output_calendar = cal.to_ical()     #converts calendar file to text

    return output_calendar





