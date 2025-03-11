import stringDifferenceFinder
from calendarRequest import github_push_calendar, github_get_calendar
from icsCalendarManipulation import *
from saveTime import save_time

current_time = save_time("startTime.txt")

recent_calendar_str = get_recent_calendar()

recent_calendar_str = append_to_description(recent_calendar_str, "\n Last updated: " + current_time)

# Load the ICS file
ics_file_path = "old_calendar.ics"
old_calendar_str = get_old_calendar(ics_file_path)



if old_calendar_str == recent_calendar_str:
    print("Same Calendar")

else:
    print("Different Calendar\n"
          "Updating the Calendar")


    save_calendar(ics_file_path, recent_calendar_str)

    github_push_calendar()

    github_calendar_str = github_get_calendar()

    if github_calendar_str != recent_calendar_str:
        input("Saving Calendar to github failed\n"
              "Press enter to continue")

    else:
        print("Saved Calendar")

save_time("endTime.txt")
