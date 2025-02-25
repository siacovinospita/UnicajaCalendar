import subprocess

import requests

def most_recent_calendar():

    url = "https://www.unicajabaloncesto.com/calendario/ics"
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        input("Please check request")

def github_get_calendar():
    url = "https://siacovinospita.github.io/UnicajaCalendar/old_calendar.ics"
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        input("Please check request")

import subprocess
import datetime
def github_push_calendar():
    current_time = datetime.datetime.now()
    commit_message = f"Update Calendar + {current_time}"
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
