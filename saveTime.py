import datetime

def save_time(file_name):

    # Get the current time
    current_time = datetime.datetime.now()
    # Write the current time to the file
    with open(file_name, "w") as file:
        file.write(f"Current time: {current_time}\n")

    return current_time.strftime("%Y-%m-%d %H:%M:%S")
