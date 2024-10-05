from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date and time in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the current date and time
    print(f"Current date and time: {formatted_date}")


# Part 2: Calculate a Future Date
def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()

    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)

    # Format the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")


# Main program
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()

    # Prompt the user to enter the number of days to add to the current date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
