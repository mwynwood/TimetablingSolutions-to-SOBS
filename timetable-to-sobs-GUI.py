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
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_file(filename_input, filename_output):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(filename_input)

    # Remove columns not needed by SOBS
    df = df.drop(['FDayName', 'YearLevel'], axis=1)

    # Rename the columns to what SOBS expects
    df = df.rename(columns={
        'Period'    : 'Period',
        'ClassName' : 'ClassName',
        'Room'      : 'Room',
        'Teacher'   : 'Teacher',
        'SDayName'  : 'Day_No',
        'Subject'   : 'RollClass'
    })

    # Set the order of the columns
    new_order = [
        'Day_No',
        'Period',
        'RollClass',
        'ClassName',
        'Room',
        'Teacher'
    ]
    df = df[new_order]

    # Add "DO-" to the front of the room number
    df['Room'] = 'DO-' + df['Room'].astype(str)

    # Save output
    df.to_csv(filename_output, index=False)


def select_and_run():
    # Step 1: Select input file
    filename_input = filedialog.askopenfilename(
        title="Select eMinervaTTable.txt file",
        filetypes=[("eMinerva timetable", "eMinervaTTable.txt"), ("CSV/TXT files", "*.csv *.txt")]
    )

    if not filename_input:
        return

    # Build a suggested output filename
    input_dir = os.path.dirname(filename_input)
    suggested_name = "eMinervaTTable_SOBS.csv"
    suggested_path = os.path.join(input_dir, suggested_name)

    # Step 2: Ask where to save output (with pre-filled filename)
    filename_output = filedialog.asksaveasfilename(
        title="Save output CSV file",
        initialfile=suggested_name,
        initialdir=input_dir,
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )

    if not filename_output:
        return

    try:
        process_file(filename_input, filename_output)
        messagebox.showinfo(
            "Success",
            "Timetable converted successfully!\n\n"
            "You can now import the CSV into SOBS."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI ----------
root = tk.Tk()
root.title("Timetable to SOBS Converter")
root.resizable(False, False)

tk.Label(
    root,
    text="Timetable to SOBS Converter",
    font=("Segoe UI", 12, "bold")
).pack(pady=(12, 5))

tk.Button(
    root,
    text="Select eMinervaTTable.txt file and Convert",
    width=40,
    height=2,
    command=select_and_run
).pack(pady=10)

tk.Label(
    root,
    text="A SOBS‑ready CSV filename will be suggested automatically",
    font=("Segoe UI", 9)
).pack(pady=(0, 10))

root.mainloop()