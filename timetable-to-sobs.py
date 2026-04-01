# Converts the Timetabling Solutions output into a format suitable for SOBS
# Requires the pandas library (pip install pandas)
#
# Marcus Wynwood
# 2 April 2026

# Timetabling Solutions give us this:
# 1. Period
# 2. ClassName
# 3. Room
# 4. Teacher
# 5. SDayName
# 6. FDayName
# 7. Subject
# 8. YearLevel

# SOBS Expects this:
# 1. Day_No     : This is day number from the timetable
# 2. Period     : The period import code
# 3. RollClass  : The first part of the booking description
# 4. ClassName  : The second part of the booking description
# 5. Room       : The room import code
# 6. Teacher    : The staff member import code

import pandas as pd

filename_input = "eMinervaTTable.txt"
filename_output = filename_input + ".output.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(filename_input)

# Remove columns not needed by SOBS
df = df.drop(['FDayName'], axis=1)
df = df.drop(['YearLevel'], axis=1)

# Rename the columns to what SOBS expects
# Current name on the left, new name on the right.
df = df.rename(columns={
    'Period'    :   'Period', 
    'ClassName' :   'ClassName', 
    'Room'      :   'Room',
    'Teacher'   :   'Teacher',
    'SDayName'  :   'Day_No',
    'Subject'   :   'RollClass'
    })

# Set the order of the colums to what SOBS expects
new_order = [
    'Day_No', 
    'Period', 
    'RollClass', 
    'ClassName', 
    'Room', 
    'Teacher']
# Do the reorder
df = df[new_order]

# Add "DO-" to the front of the room number in the 'Room' field
df['Room'] = 'DO-' + df['Room'].astype(str)

# Save the renamed and reordered DataFrame to a new CSV file
df.to_csv(filename_output, index=False)

# Import into SOBS
# Profit