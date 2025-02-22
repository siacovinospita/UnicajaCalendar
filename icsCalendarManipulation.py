from ics import Calendar
import calendarRequest

# Convert the calendars to strings without DTSTAMP
def remove_dtstamp(calendar_str):
    return remove_lines_starting_with(calendar_str, "DTSTAMP:")

def remove_sequence(calendar_str):
    return remove_lines_starting_with(calendar_str, "SEQUENCE:")

def remove_lines_starting_with(calendar_str, start_of_line):
    return "\n".join(
        line for line in str(calendar_str).splitlines() if not line.startswith(start_of_line)
    )

def change_line_ending(calendar_str):
    return calendar_str.replace("\r\n", "\n")

def checkValidCalendar(calendar_str, errorMessage = "Error Pasing Calendar - Origin Unknown"):
    try:
       Calendar(calendar_str)
    except:
        print(errorMessage)
        input()

def get_recent_calendar():
    recent_calendar_str = calendarRequest.most_recent_calendar()

    recent_calendar_str = change_line_ending(recent_calendar_str)
    recent_calendar_str = remove_dtstamp(recent_calendar_str)
    recent_calendar_str = remove_sequence(recent_calendar_str)

    checkValidCalendar(recent_calendar_str, "Error Parsing Calendar from request")

    return recent_calendar_str

def get_github_calendar():
    return calendarRequest.github_calendar()



def get_old_calendar(ics_file_path):
    with open(ics_file_path, 'r') as f:
        old_calendar_str = f.read()

    old_calendar_str = remove_dtstamp(old_calendar_str)
    old_calendar_str = remove_sequence(old_calendar_str)
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

import subprocess

def git_push(commit_message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Example usage
git_push("Updated ICS file")

