from icsCalendarManipulation import *
from saveTime import save_time

save_time("startTime.txt")

recent_calendar_str = get_recent_calendar()

# Load the ICS file
ics_file_path = "old_calendar.ics"
old_calendar_str = get_old_calendar(ics_file_path)

if old_calendar_str == recent_calendar_str:
    print("Same Calendar")

else:
    print("Different Calendar\n"
          "Make sure to update the calendar")
    input("Press enter to continue")

    save_calendar(ics_file_path, recent_calendar_str)

    print("Saved Calendar")

save_time("endTime.txt")
