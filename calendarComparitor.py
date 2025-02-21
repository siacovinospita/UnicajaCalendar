from icsCalendarManipulation import *
from stringDifferenceFinder import diff_two_string


def get_and_compare_the_calendars():
    recent_calendar_str = get_recent_calendar()

    # Load the ICS file
    ics_file_path = "old_calendar.ics"
    old_calendar_str = get_old_calendar(ics_file_path)

    if old_calendar_str == recent_calendar_str:
        print("Same Calendar")

    else:
        diff_two_string(old_calendar_str, recent_calendar_str)



get_and_compare_the_calendars()