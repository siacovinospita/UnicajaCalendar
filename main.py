import ics
from ics import Calendar
import calendarRequest
import difflib
import saveTime

# Convert the calendars to strings without DTSTAMP
def remove_dtstamp(calendar):
    return "\n".join(
        line for line in str(calendar).splitlines() if not line.startswith("DTSTAMP:")
    )

def diff_two_string(string_1, string_2):
    # Get differences
    diff = difflib.ndiff(string_1.splitlines(), string_2.splitlines())

    # Print differences
    print("\n".join(diff))

saveTime.save_time("startTime.txt")

recent_calendar_str = calendarRequest.most_recent_calendar()
recent_calendar_str = recent_calendar_str.replace("\r\n", "\n")
recent_calendar_str = remove_dtstamp(recent_calendar_str)
recent_calendar = Calendar(recent_calendar_str)

# Load the ICS file
ics_file_path = "old_calendar.ics"

with open(ics_file_path, 'r') as f:
    old_calendar_str = f.read()
    old_calendar_str = remove_dtstamp(old_calendar_str)
    try:
        old_calendar = Calendar(old_calendar_str)
    except:
        print("Error Parsing old_calendar.ics")
        input()

if old_calendar_str == recent_calendar_str:
    print("Same Calendar")
else:
    print("Different Calendar")
    input("\nMake sure to update the calendar")

# Save the calendar to a file
with open(ics_file_path, "w") as f:
    # print(recent_calendar_str)
    f.write(recent_calendar_str)
    print("Saved Calendar")

saveTime.save_time("endTime.txt")

# # Iterate through events and print details
# for event in calendar.events:
#     print(f"Event: {event.name}")
#     print(f"Start: {event.begin}")
#     print(f"End: {event.end}")
#     print(f"Location: {event.location}")
#     print(f"Description: {event.description}")
#     print("-" * 40)

