import pandas as pd
from datetime import datetime, timedelta

# Load the spreadsheet into a DataFrame
file_path = "C:/Users/Jay Rathod/Documents/Assignment_Timecard.xlsx - Sheet1.csv"
  # Replace with the actual path to your file
df = pd.read_csv(file_path)

# Convert the time columns to datetime objects
df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

# a) Employees who have worked for 7 consecutive days
for name, group in df.groupby('Employee Name'):
    consecutive_days = group['Time'].diff().dt.days
    if any(consecutive_days >= 7):
        print(f"{name} has worked for 7 consecutive days.")

# b) Employees with less than 10 hours between shifts but greater than 1 hour
for name, group in df.groupby('Employee Name'):
    shift_gaps = group['Time'].diff().dt.total_seconds() / 3600
    if any((1 < shift_gaps) & (shift_gaps < 10)):
        print(f"{name} has less than 10 hours between shifts but greater than 1 hour.")

# c) Employees who have worked for more than 14 hours in a single shift
for index, row in df.iterrows():
    shift_duration = (row['Time Out'] - row['Time']).total_seconds() / 3600
    if shift_duration > 14:
        print(f"{row['Employee Name']} has worked for more than 14 hours in a single shift.")

# Save console output to a file
with open("output.txt", "w") as output_file:
    # Redirect print statements to the file
    print = lambda *args: output_file.write(" ".join(map(str, args)) + "\n")

    # Repeat the same logic for printing to console
    # ...

# Note: Make sure to replace 'Employee Name', 'Shift Start Time', 'Shift End Time' with your actual column names.
