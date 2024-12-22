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
