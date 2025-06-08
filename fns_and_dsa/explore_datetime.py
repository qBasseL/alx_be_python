from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    # Format as "YYYY-MM-DD"
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days} day(s): {formatted}")

def main():
    display_current_datetime()
    try:
        days_input = int(input("Enter number of days to add: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
