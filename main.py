import stringDifferenceFinder
from calendarRequest import github_push_calendar, github_get_calendar
from icsCalendarManipulation import *
from saveTime import save_time
from time import sleep


current_time = save_time("startTime.txt")

recent_calendar_str = calendarRequest.most_recent_calendar()

recent_calendar_str = append_to_description(recent_calendar_str, "\n Last updated: " + current_time)
recent_calendar_str = format_recent_calendar(recent_calendar_str)

# Load the ICS file
ics_file_path = "old_calendar.ics"
old_calendar_str = get_old_calendar(ics_file_path)

if old_calendar_str == recent_calendar_str:
    print("Same Calendar")

else:
    print("Different Calendar\n"
          "Updating the Calendar")


    save_calendar_to_file(ics_file_path, recent_calendar_str)

    github_push_calendar()

    correctlySavedToGitHub = False
    for i in range(0, 1000):
        correctlySavedToGitHub = (github_get_calendar() == recent_calendar_str)
        if correctlySavedToGitHub:
            print("Successful get on attempt" + i)
            break
        sleep(0.05)  #sleep for 50 ms



    if not correctlySavedToGitHub:
        input("Could not confirm saving Calendar to github\n"
              "Press enter to check again")
        github_calendar_str = github_get_calendar()
        if github_calendar_str != recent_calendar_str:
            print("Calendar still different")
        else:
            print("Saved Calendar")

    else:
        print("Saved Calendar")

save_time("endTime.txt")
