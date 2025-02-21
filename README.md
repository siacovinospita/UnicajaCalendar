# UnicajaCalendar
 
Events fetched from the Unicaja calendar ics have the following attributes:

"BEGIN", "CLASS", "SUMMARY", "ORGANIZER", "DTSTAMP", "DTSTART", "DTEND", "TRANSP", "DESCRIPTION", "SEQUENCE", "UID", "END"

Example:

BEGIN:VEVENT
CLASS:PUBLIC
SUMMARY:Filou Oostende - Unicaja
ORGANIZER:Filou Oostende
DTSTAMP:20241230T153902Z
DTSTART:20241001T183000Z
DTEND:20241001T203000Z
TRANSP:OPAQUE
DESCRIPTION:Basketball Champions League (Liga Regular, Jornada 1)
SEQUENCE:6
UID:2024-2025-202425035
END:VEVENT

"CLASS" - is always "CLASS:PUBLIC"
"SUMMARY" - The two teams that play in the game
"ORGANIZER" - The first team in Summary
"DTSTAMP" - Time the calendar is fetched
"DTSTART" - Start time of the game
"DTEND" - End time of the game
"TRANSP" - is always "TRANSP:OPAQUE"
"DESCRIPTION" - Contains the competition
"SEQUENCE" - Increased for some reason 
"UID" - 

"DTSTAMP" and "SEQUENCE" are removed