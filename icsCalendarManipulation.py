from ics import Calendar

# Convert the calendars to strings without DTSTAMP
def remove_dtstamp(calendar_str):
    return "\n".join(
        line for line in str(calendar_str).splitlines() if not line.startswith("DTSTAMP:")
    )

def change_line_ending(calendar_str):
    return calendar_str.replace("\r\n", "\n")

def checkValidCalendar(calendar_str, errorMessage = "Error Pasing Calendar - Origin Unknown"):
    try:
       Calendar(calendar_str)
    except:
        print(errorMessage)
        input()


def get_old_calendar(ics_file_path):
    with open(ics_file_path, 'r') as f:
        old_calendar_str = f.read()

    old_calendar_str = remove_dtstamp(old_calendar_str)
    checkValidCalendar(old_calendar_str, "Error Parsing Calendar from file")

    return old_calendar_str

def save_calendar(ics_file_path, calendar_str):
    # Save the calendar to a file
    with open(ics_file_path, "w") as f:
        f.write(calendar_str)

# # Iterate through events and print details
# for event in calendar.events:
#     print(f"Event: {event.name}")
#     print(f"Start: {event.begin}")
#     print(f"End: {event.end}")
#     print(f"Location: {event.location}")
#     print(f"Description: {event.description}")
#     print("-" * 40)

