# ICS-Date-Conversion
Takes as arbitrary input of an ICS file and start date and generates output: ICS file that is shifted such that the first calendar event is https://github.com/Daniel-Bullock/ISC-Date-Conversionon the new input date and the rest of the events follow accordingly to the shift amount.

(note: unfortunately currently the only way to run the program is to download the program, working on a fix)

Packages: I used several python packages to create this- [icalendar](https://pypi.org/project/icalendar/), pytz, and datetime, which you might need to install.  A bulk of the code utilizes the icalendar library. 

Directions for running:


1. Download files to computer and unzip
2. Run iscShifter.py in preffered IDE or other method
3. Input the input calendar in format 'input_calendar.ics' to console
4. Input year, month, and date to console
5. Output will be in unzipped folder.
